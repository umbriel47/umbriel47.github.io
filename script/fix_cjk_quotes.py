#!/usr/bin/env python3
"""Turn straight double quotes in Chinese posts into proper 「curly」 pairs.

    python3 script/fix_cjk_quotes.py [--dry-run]

Kramdown's smart-quote pass infers direction from the surrounding whitespace.
Chinese has no spaces around a quoted phrase, so it guesses wrong and emits a
closing quote at both ends — 」四十年」 rather than 「四十年」. Converting the
source to the correct characters sidesteps the guess entirely, and leaves
English posts (where the inference works) untouched.

Code and HTML are masked before substitution: a straight quote inside a shell
command, a Ruby snippet or an HTML attribute is syntax, not punctuation, and
must survive untouched.
"""
import argparse
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OPEN, CLOSE = "\u201c", "\u201d"
PAIR = re.compile(r'"([^"<>\n]{1,120})"')

# Anything here is syntax rather than prose and is masked out first.
PROTECT = [
    re.compile(r"^```.*?^```", re.S | re.M),                 # fenced code
    re.compile(r"\{%\s*highlight.*?\{%\s*endhighlight\s*%\}", re.S),
    re.compile(r"^(?:\t| {4,}).*$", re.M),                   # indented code
    re.compile(r"`[^`\n]*`"),                                # inline code
    re.compile(r"<[^>]*>"),                                  # html tags
]


def convert(text):
    chunks = []

    def mask(m):
        chunks.append(m.group(0))
        return "\x00%d\x00" % (len(chunks) - 1)

    masked = text
    for pat in PROTECT:
        masked = pat.sub(mask, masked)
    # A doubled straight quote is a typo in the source; collapsing it first
    # keeps the pairing below aligned.
    masked = masked.replace('""', '"')
    masked, n = PAIR.subn(lambda m: OPEN + m.group(1) + CLOSE, masked)
    restored = re.sub(r"\x00(\d+)\x00", lambda m: chunks[int(m.group(1))], masked)
    return restored, n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    total = 0
    for path in sorted(glob.glob(os.path.join(ROOT, "_posts", "zh", "*.md"))):
        raw = open(path, encoding="utf-8").read()
        m = re.match(r"^(---\n.*?\n---\n)(.*)$", raw, re.S)
        if not m:
            continue
        front, body = m.group(1), m.group(2)

        # Front matter: an escaped \"…\" inside a quoted scalar becomes a
        # curly pair, which also removes the need for the escaping.
        front2, fn = re.subn(r'\\"([^"\n]{1,120})\\"',
                             lambda x: OPEN + x.group(1) + CLOSE, front)
        body2, bn = convert(body)
        if fn + bn == 0:
            continue
        total += fn + bn
        print("  %-52s %d" % (os.path.basename(path), fn + bn))
        if not args.dry_run:
            open(path, "w", encoding="utf-8").write(front2 + body2)
    print("\n%d quote pairs%s" % (total, " (dry run)" if args.dry_run else " converted"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
