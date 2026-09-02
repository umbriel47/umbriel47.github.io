#!/usr/bin/env python3
"""Import a novel's chapters into a Jekyll fiction collection.

    python3 script/import_novel.py <source chapters dir> <slug> [--lang zh]

Source chapters are `NN-title.md` files whose first line is a `# ...` heading.
The heading is dropped (the layout renders the title), and a lone `*` line —
a scene break — becomes a styled element rather than an accidental list item.
"""
import argparse
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Chapter number -> volume key. Extend per novel as needed.
VOLUMES = {
    "chenbi": {1: "v1", 2: "v1", 3: "v1", 4: "v2", 5: "v2", 6: "v2",
               7: "v3", 8: "v3", 9: "v3", 10: "v4", 11: "v4", 12: "v4",
               13: "v4", 14: "v5", 15: "v5", 16: "v5", 17: "v6", 18: "v6",
               19: "v6", 20: "v7", 21: "v7", 22: "v7", 23: "v7", 24: "v7",
               25: "v7", 26: "v7"},
}


def chapter_title(heading, fallback):
    """`# 第一章 · 验骨人` -> `验骨人`."""
    t = heading.lstrip("#").strip()
    for sep in ("·", "・", "|"):
        if sep in t:
            return t.split(sep, 1)[1].strip()
    return t or fallback


def convert(body):
    out = []
    for line in body.split("\n"):
        if line.strip() == "*":
            # Kramdown would read a bare "*" as an empty list item.
            out.append('<p class="scene-break" aria-hidden="true">*</p>')
        else:
            out.append(line)
    return "\n".join(out).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("slug")
    ap.add_argument("--lang", default="zh", choices=["en", "zh"])
    args = ap.parse_args()

    dest = os.path.join(ROOT, "_fictions_%s" % args.lang, args.slug)
    os.makedirs(dest, exist_ok=True)

    files = sorted(f for f in os.listdir(args.src) if re.match(r"\d+.*\.md$", f))
    if not files:
        sys.exit("no NN-*.md chapters in %s" % args.src)

    vols = VOLUMES.get(args.slug, {})
    for f in files:
        n = int(re.match(r"(\d+)", f).group(1))
        raw = open(os.path.join(args.src, f), encoding="utf-8").read()
        lines = raw.split("\n")
        heading, rest = "", raw
        if lines and lines[0].startswith("#"):
            heading, rest = lines[0], "\n".join(lines[1:])
        title = chapter_title(heading, os.path.splitext(f)[0])

        fm = ["---", 'title: "%s"' % title.replace('"', '\\"'),
              "novel: %s" % args.slug, "order: %d" % n]
        if vols.get(n):
            fm.append("volume: %s" % vols[n])
        fm.append("---")

        path = os.path.join(dest, "%02d.md" % n)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write("\n".join(fm) + "\n\n" + convert(rest) + "\n")
        print("%02d  %s" % (n, title))

    print("\n%d chapters -> %s" % (len(files), os.path.relpath(dest, ROOT)))


if __name__ == "__main__":
    main()
