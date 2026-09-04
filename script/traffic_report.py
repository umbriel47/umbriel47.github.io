#!/usr/bin/env python3
"""Pull page views from GoatCounter and report them merged across languages.

    export GOATCOUNTER_SITE=aicracker          # your subdomain
    export GOATCOUNTER_TOKEN=...               # Settings -> API tokens
    python3 script/traffic_report.py [--days 30] [--by section|content]

The site publishes every article twice, at /en/blog/<slug>/ and
/zh/blog/<slug>/. Analytics counts those as two pages; this merges them on the
shared slug so one article reads as one number, and still shows the language
split, which is the useful signal for deciding what is worth translating.
"""
import argparse
import collections
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from datetime import date, timedelta

SITE = os.environ.get("GOATCOUNTER_SITE", "")
TOKEN = os.environ.get("GOATCOUNTER_TOKEN", "")

# /en/blog/<slug>/ and /zh/blog/<slug>/ are one piece of content.
PATH = re.compile(r"^/(en|zh)/(blog|fictions|hobbies|publications)/?(.*?)/?$")


def api(path, params):
    if not SITE or not TOKEN:
        sys.exit("set GOATCOUNTER_SITE and GOATCOUNTER_TOKEN first (see --help)")
    url = "https://%s.goatcounter.com/api/v0/%s?%s" % (
        SITE, path, urllib.parse.urlencode(params))
    req = urllib.request.Request(url, headers={
        "Authorization": "Bearer " + TOKEN,
        "Content-Type": "application/json",
    })
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def classify(path):
    """-> (section, content_key, lang). lang is None for non-localised paths."""
    m = PATH.match(path)
    if not m:
        if path.startswith("/art/"):
            return "arts-item", path[len("/art/"):], None
        if path.startswith("/music/"):
            return "music-item", path[len("/music/"):], None
        return "other", path, None
    lang, section, rest = m.group(1), m.group(2), m.group(3)
    return section, rest or "(index)", lang


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--days", type=int, default=30)
    ap.add_argument("--by", choices=["content", "section"], default="content")
    ap.add_argument("--limit", type=int, default=40)
    args = ap.parse_args()

    start = (date.today() - timedelta(days=args.days)).isoformat()
    data = api("stats/hits", {"start": start, "limit": 500})

    merged = collections.defaultdict(lambda: collections.Counter())
    sections = collections.Counter()
    total = 0
    for hit in data.get("hits", []):
        path, count = hit.get("path", ""), hit.get("count", 0)
        section, key, lang = classify(path)
        merged[(section, key)][lang or "-"] += count
        sections[section] += count
        total += count

    print("last %d days — %d page views\n" % (args.days, total))

    if args.by == "section":
        for section, n in sections.most_common():
            print("  %-14s %6d  %5.1f%%" % (section, n, 100.0 * n / max(total, 1)))
        return 0

    rows = sorted(merged.items(), key=lambda kv: -sum(kv[1].values()))
    print("  %-10s %-42s %6s %6s %6s" % ("section", "content", "total", "en", "zh"))
    print("  " + "-" * 72)
    for (section, key), langs in rows[:args.limit]:
        print("  %-10s %-42s %6d %6d %6d" % (
            section, key[:42], sum(langs.values()), langs.get("en", 0), langs.get("zh", 0)))
    if len(rows) > args.limit:
        print("\n  … %d more (raise --limit)" % (len(rows) - args.limit))
    return 0


if __name__ == "__main__":
    sys.exit(main())
