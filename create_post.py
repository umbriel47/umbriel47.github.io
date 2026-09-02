#!/usr/bin/env python3
"""Scaffold a matching pair of bilingual posts.

    python3 create_post.py my-article-slug
    python3 create_post.py my-article-slug --en "English title" --zh "中文标题"
    python3 create_post.py my-article-slug --date 2026-09-05

Writes _posts/en/<date>-<slug>.md and _posts/zh/<date>-<slug>.md. Both carry the
same `ref:`, which is what pairs them for the language switcher and the hreflang
tags — keep it identical, and keep the slug ASCII so the URLs stay shareable.
"""
import argparse
import os
import re
import sys
from datetime import datetime

ROOT = os.path.dirname(os.path.abspath(__file__))

TEMPLATE = """---
layout: post
title: "{title}"
date: {date} {time} +0800
lang: {lang}
ref: {slug}
tags: [{tag}]
description: "{description}"
---

{body}
"""

BODY = {
    "en": "Write the English version here.",
    "zh": "在这里写中文版本。",
}
DESCRIPTION = {
    "en": "One sentence for search results and the post list.",
    "zh": "一句话摘要，用于搜索结果和文章列表。",
}


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slug", help="ASCII slug, e.g. on-evolution-of-intelligence")
    ap.add_argument("--en", default=None, help="English title")
    ap.add_argument("--zh", default=None, help="Chinese title")
    ap.add_argument("--date", default=None, help="YYYY-MM-DD (default: today)")
    ap.add_argument("--tag", default="notes", help="tag (default: notes)")
    args = ap.parse_args()

    slug = args.slug.strip().strip("/")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
        sys.exit("slug must be lowercase ASCII words joined by hyphens: %r" % slug)

    now = datetime.now()
    date = args.date or now.strftime("%Y-%m-%d")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
        sys.exit("--date must be YYYY-MM-DD")
    time = now.strftime("%H:%M:%S")

    titles = {"en": args.en or slug.replace("-", " ").capitalize(),
              "zh": args.zh or slug}

    written = []
    for lang in ("en", "zh"):
        path = os.path.join(ROOT, "_posts", lang, "%s-%s.md" % (date, slug))
        if os.path.exists(path):
            sys.exit("already exists: %s" % path)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(TEMPLATE.format(title=titles[lang], date=date, time=time,
                                    lang=lang, slug=slug, tag=args.tag,
                                    description=DESCRIPTION[lang], body=BODY[lang]))
        written.append(path)

    for p in written:
        print("created %s" % os.path.relpath(p, ROOT))
    print("\nURLs: /en/blog/%s/  and  /zh/blog/%s/" % (slug, slug))


if __name__ == "__main__":
    main()
