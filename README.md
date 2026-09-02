# aicracker.com — Stochastic Path

Personal site of Lipeng Lai. Jekyll 4, no theme gem — all layouts and CSS live
in this repo. Every section exists in English (`/en/…`) and Chinese (`/zh/…`).

## Running it locally

```sh
bundle install
bundle exec jekyll serve      # http://127.0.0.1:4000
```

## How the two languages are wired together

A document declares `lang:` (`en` or `zh`) and `ref:` (a shared translation
key). Two documents with the same `ref` and different `lang` are a translation
pair: the language switch in the header links them, `<link rel="alternate"
hreflang>` is emitted for both, and the post page shows a link to the other
version. A document with no counterpart still works — the switcher falls back to
the other language's home page.

UI strings (nav labels, buttons, dates) come from `_data/i18n.yml`. Nothing in a
layout should contain user-visible English or Chinese text directly.

## Adding content

### A blog post

```sh
python3 create_post.py my-article-slug --en "English title" --zh "中文标题"
```

Writes `_posts/en/<date>-<slug>.md` and `_posts/zh/<date>-<slug>.md`, which
publish at `/en/blog/<slug>/` and `/zh/blog/<slug>/`. Keep slugs ASCII — the
pre-2026 posts used Chinese titles in the URL, which produced unshareable
percent-encoded links.

### A publication

`_data/publications.yml` is **generated** — edit
`script/publications_source.yml` instead and run:

```sh
python3 script/sync_publications.py
```

Add an entry with `key`, `year`, `kind` (`journal` or `preprint`), `authors`,
`title`, `venue` and `venue_zh`. The script fills in the abstract and the link
from PubMed, Crossref, arXiv, bioRxiv or OpenReview, preferring PubMed because
Crossref mangles subscripts and markup for some publishers. Supply a `doi`,
`arxiv` or `openreview` hint when you have one; the script reports anything it
cannot resolve by title.

Abstracts are cached in `script/.publications_cache.json` (untracked), so
adding one paper does not re-fetch the rest. `--only KEY` refreshes one entry,
`--dry-run` writes nothing.

Titles and abstracts stay in English on both language pages: a paper title is a
citable string, and a translated one cannot be searched for.

### A novel

A novel is written in one language and is **not** translated. Both
`/en/fictions/` and `/zh/fictions/` list every novel; an entry whose language
differs from the current interface is tagged with its language and links into
its own language tree.

1. Add the novel to `_data/fictions.yml` with `slug`, `lang`, `status`,
   `cover`, `title` and `blurb` — `title` and `blurb` are plain strings in the
   novel's own language. `series`, `meta` and `volumes` are optional.
2. Create the detail page `<lang>/fictions/<slug>.md` (front matter only —
   copy an existing one).
3. Put chapters in `_fictions_<lang>/<slug>/`. Each needs `title:`,
   `novel: <slug>`, `order: <n>` and, if the novel has `volumes`, a `volume:`
   naming one of their keys. The sidebar, the table of contents and the
   previous/next links all derive from `order`.

To import chapters that already exist as `NN-title.md` files with a `# ...`
heading on the first line:

```sh
python3 script/import_novel.py <chapters dir> <slug> --lang zh
```

It strips the heading (the layout renders the title) and turns a lone `*`
scene-break line into a styled element — Kramdown would otherwise read it as an
empty list item. Volume assignments live in the `VOLUMES` table in that
script.

### Art and music

Edit `_data/arts.yml` and `_data/music.yml`. Art images go in
`assets/img/arts/` (keep them web-sized). A music release uses exactly one of
`audio:` (a file under `assets/audio/`), `embed:` (an embeddable player URL) or
`link:` (a plain outbound link).

GitHub Pages caps a site at roughly 1 GB with a 100 MB limit per file, so host
large audio externally and use `embed:`.

## Deployment

Pushing to `branch2022` runs `.github/workflows/pages.yml`: build with Jekyll,
run `script/check_links.rb` (fails the build on a broken internal link), deploy
to GitHub Pages. The custom domain comes from `CNAME`.

The repo's **Settings → Pages → Build and deployment → Source** must be set to
**GitHub Actions**.

## Old URLs

The pre-2026 posts were published at percent-encoded Chinese paths. Each
migrated post carries a `redirect_from:` entry, so the old links still resolve.
Do not delete those entries.
