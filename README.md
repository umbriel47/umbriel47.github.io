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

Add an entry to `_data/publications.yml`. Sorted by `year`, newest first. The
title links to `links.journal`, falling back to `links.preprint`, then
`links.pdf`.

### A novel

1. Add the novel to `_data/fictions.yml` with a `slug`, `status`, `cover`,
   `title` and `blurb`.
2. Create the detail pages `en/fictions/<slug>.md` and `zh/fictions/<slug>.md`
   (front matter only — copy an existing one).
3. Drop chapters into `_fictions_en/<slug>/` and `_fictions_zh/<slug>/`. Each
   chapter needs `title:`, `novel: <slug>` and `order: <n>`. The sidebar
   navigation and the previous/next links are derived from `order`.

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
