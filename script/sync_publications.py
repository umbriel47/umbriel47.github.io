#!/usr/bin/env python3
"""Regenerate _data/publications.yml from script/publications_source.yml.

    python3 script/sync_publications.py [--only KEY ...] [--dry-run]

The source file carries the curated fields (which papers to list, in what
order, under what venue label). This script fills in the abstract and the
outbound link for each one, from — in order of preference — PubMed, Crossref,
arXiv, bioRxiv and OpenReview.

Preference matters: Crossref strips JATS markup badly for some publishers,
producing artefacts like "K ATP" for a subscript, so PubMed's plain-text
abstract is used whenever the paper is indexed there.

Abstracts are cached in script/.publications_cache.json so a re-run after
adding one paper does not re-fetch the other twenty-six. Delete the cache to
force a full refresh.
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from xml.etree import ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE = os.path.join(ROOT, "script", "publications_source.yml")
CACHE = os.path.join(ROOT, "script", ".publications_cache.json")
OUT = os.path.join(ROOT, "_data", "publications.yml")
UA = {"User-Agent": "Mozilla/5.0 (compatible; aicracker-site/1.0)"}


# --- tiny YAML reader ------------------------------------------------------
# The source file is a flat list of scalar-valued maps, so a full YAML parser
# is not worth a dependency here.

def read_source(path):
    entries, cur = [], None
    for raw in open(path, encoding="utf-8"):
        line = raw.rstrip("\n")
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith("- "):
            cur = {}
            entries.append(cur)
            line = "  " + line[2:]
        if cur is None:
            continue
        m = re.match(r"\s+([A-Za-z_]+):\s*(.*)$", line)
        if not m:
            continue
        k, v = m.group(1), m.group(2).strip()
        if len(v) > 1 and v[0] == v[-1] == '"':
            v = v[1:-1].replace('\\"', '"').replace("\\\\", "\\")
        elif re.fullmatch(r"-?\d+", v):
            v = int(v)
        cur[k] = v
    return entries


# --- fetching --------------------------------------------------------------

def get(url, tries=3):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
                return r.read()
        except Exception as exc:
            if i == tries - 1:
                print("      ! %s" % exc, file=sys.stderr)
                return None
            time.sleep(1.5)


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()


def clean(text):
    text = re.sub(r"<[^>]+>", " ", text or "")
    for a, b in (("&amp;", "&"), ("&lt;", "<"), ("&gt;", ">"), ("&quot;", '"')):
        text = text.replace(a, b)
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"^(Abstract|ABSTRACT)[:\s]+", "", text)
    text = re.sub(r"\s+([,.;:])", r"\1", text)
    text = re.sub(r"\(\s+", "(", text).replace(" )", ")")
    # Some publishers deposit a broken hyphen join ("SUR2- containing").
    # Rejoin those, but leave a suspended hyphen alone ("pre- and post-").
    text = re.sub(r"(\w)- (?!and\b|or\b|to\b|but\b|nor\b)([a-z]\w)", r"\1-\2", text)
    return text


def pubmed(title):
    # NCBI rejects a quoted phrase inside a [Title] term; pass the words bare.
    term = urllib.parse.quote(re.sub(r"[^\w\s-]", " ", title) + "[Title]")
    raw = get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
              "?db=pubmed&retmode=json&retmax=5&term=" + term)
    if not raw:
        return None
    ids = json.loads(raw).get("esearchresult", {}).get("idlist", [])
    if not ids:
        return None
    time.sleep(0.4)
    xml = get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
              "?db=pubmed&retmode=xml&id=" + ",".join(ids))
    if not xml:
        return None
    for art in ET.fromstring(xml).findall(".//PubmedArticle"):
        node = art.find(".//ArticleTitle")          # an Element is falsy when
        got = "".join(node.itertext()) if node is not None else ""   # childless
        if norm(got)[:55] != norm(title)[:55]:
            continue
        parts = []
        for a in art.findall(".//Abstract/AbstractText"):
            label, body = a.get("Label"), clean("".join(a.itertext()))
            parts.append("%s: %s" % (label.capitalize(), body) if label else body)
        if not parts:
            continue
        doi = next((e.text for e in art.findall(".//ArticleIdList/ArticleId")
                    if e.get("IdType") == "doi"), None)
        return {"abstract": " ".join(parts), "doi": doi, "via": "pubmed"}
    return None


def crossref(title):
    raw = get("https://api.crossref.org/works?rows=3&query.bibliographic="
              + urllib.parse.quote(title))
    if not raw:
        return None
    for it in json.loads(raw).get("message", {}).get("items", []):
        got = (it.get("title") or [""])[0]
        if norm(got)[:55] != norm(title)[:55]:
            continue
        abstract = clean(it.get("abstract") or "")
        if abstract:
            return {"abstract": abstract, "doi": it.get("DOI"), "via": "crossref"}
    return None


def arxiv(title=None, aid=None):
    if aid:
        url = "http://export.arxiv.org/api/query?id_list=" + aid
    else:
        url = ("http://export.arxiv.org/api/query?max_results=5&search_query=ti:%22"
               + urllib.parse.quote(title[:120]) + "%22")
    raw = get(url)
    if not raw:
        return None
    ns = {"a": "http://www.w3.org/2005/Atom"}
    for e in ET.fromstring(raw).findall("a:entry", ns):
        got = e.findtext("a:title", "", ns)
        if not aid and norm(got)[:45] != norm(title)[:45]:
            continue
        return {"abstract": clean(e.findtext("a:summary", "", ns)),
                "url": e.findtext("a:id", "", ns), "via": "arxiv"}
    return None


def biorxiv(doi):
    raw = get("https://api.biorxiv.org/details/biorxiv/" + doi)
    if not raw:
        return None
    coll = json.loads(raw).get("collection") or []
    if not coll:
        return None
    return {"abstract": clean(coll[-1].get("abstract")), "doi": doi, "via": "biorxiv"}


def openreview(oid, title):
    # The notes?id= endpoint is 403 for anonymous callers; search by title and
    # pick the note whose id matches.
    raw = get("https://api.openreview.net/notes/search?limit=10&term="
              + urllib.parse.quote(title))
    if not raw:
        return None
    for n in json.loads(raw).get("notes", []):
        if n.get("id") != oid:
            continue
        abstract = clean(n.get("content", {}).get("abstract", ""))
        if abstract:
            return {"abstract": abstract,
                    "url": "https://openreview.net/forum?id=" + oid,
                    "via": "openreview"}
    return None


def resolve(entry):
    """Return {abstract, doi?, url?, via} or None."""
    title, doi = entry["title"], entry.get("doi")
    if entry.get("openreview"):
        r = openreview(entry["openreview"], title)
        if r:
            return r
    if entry.get("arxiv"):
        r = arxiv(aid=entry["arxiv"])
        if r:
            return r
    if doi and doi.startswith("10.1101/"):
        r = biorxiv(doi)
        if r and r["abstract"]:
            return r
    for fn in (lambda: pubmed(title), lambda: crossref(title), lambda: arxiv(title=title)):
        r = fn()
        if r and r["abstract"]:
            if doi:
                r["doi"] = doi          # a hand-given DOI always wins
            return r
    return None


# --- rendering -------------------------------------------------------------

def yq(s):
    return '"%s"' % str(s).replace("\\", "\\\\").replace('"', '\\"')


def folded(text, indent):
    import textwrap
    pad = " " * indent
    # break_on_hyphens=False: a folded block rejoins lines with a space, so a
    # break inside "encoder-decoder" would become "encoder- decoder".
    lines = textwrap.wrap(text, 78 - indent, break_on_hyphens=False,
                          break_long_words=False)
    return ">-\n" + "\n".join(pad + l for l in lines)


HEADER = """# Publications, newest first (sorted by `year` at render time).
#
# GENERATED by script/sync_publications.py from script/publications_source.yml.
# Edit the source file and re-run rather than editing this one.
#
# Titles and abstracts are kept in English in both languages: a paper title is
# a citable string, and a translated one cannot be searched for. Only `venue`
# carries a per-language value; the surrounding UI comes from _data/i18n.yml.
"""


def render(entries):
    out = [HEADER]
    for e in entries:
        links, seen = [], set()

        def add(kind, url):
            if url and (kind, url) not in seen:
                seen.add((kind, url))
                links.append((kind, url))

        primary = ("https://doi.org/" + e["doi"]) if e.get("doi") else e.get("url")
        add("preprint" if e.get("kind") == "preprint" else "journal", primary)
        if e.get("kind") != "preprint":
            add("preprint", e.get("preprint_url"))
            if e.get("url") and e["url"] != primary:
                add("preprint", e["url"])

        out.append("- key: %s" % e["key"])
        out.append("  year: %d" % e["year"])
        out.append("  authors: %s" % yq(e["authors"]))
        out.append("  title:")
        out.append("    en: %s" % yq(e["title"]))
        out.append("    zh: %s" % yq(e["title"]))
        out.append("  venue:")
        out.append("    en: %s" % yq(e["venue"]))
        out.append("    zh: %s" % yq(e.get("venue_zh") or e["venue"]))
        out.append("  abstract:")
        out.append("    en: " + folded(e["abstract"], 6))
        out.append("    zh: " + folded(e["abstract"], 6))
        out.append("  links:")
        for kind, url in links:
            out.append("    %s: %s" % (kind, yq(url)))
        out.append("")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*", metavar="KEY",
                    help="refetch just these keys (ignoring the cache)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    entries = read_source(SOURCE)
    cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}

    missing = []
    for e in entries:
        key = e["key"]
        stale = args.only and key in args.only
        hit = cache.get(key)
        if hit and not stale:
            e.update({k: v for k, v in hit.items() if k in ("abstract", "doi", "url", "via")})
            print("  = %-32s cached (%s)" % (key, hit.get("via")))
            continue
        print("  * %s" % key)
        res = resolve(e)
        if not res:
            missing.append(key)
            print("      MISSING — add a doi/arxiv/openreview hint to the source")
            continue
        e["abstract"] = res["abstract"]
        e["doi"] = res.get("doi") or e.get("doi")
        e["url"] = res.get("url") or e.get("url")
        e["via"] = res["via"]
        cache[key] = {k: e.get(k) for k in ("abstract", "doi", "url", "via")}
        print("      ok via %s (%d chars)" % (res["via"], len(res["abstract"])))
        time.sleep(0.5)

    ready = [e for e in entries if e.get("abstract")]
    ready.sort(key=lambda e: (-e["year"], e["key"]))
    text = render(ready)

    if args.dry_run:
        print("\n--dry-run: would write %d entries to %s" % (len(ready), OUT))
    else:
        open(OUT, "w", encoding="utf-8").write(text)
        json.dump(cache, open(CACHE, "w"), ensure_ascii=False, indent=1)
        print("\nwrote %d entries to %s" % (len(ready), os.path.relpath(OUT, ROOT)))
    if missing:
        print("unresolved: %s" % ", ".join(missing))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
