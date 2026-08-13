---
name: simpligility-blog
description: >-
  Draft, convert, and publish blog posts for the simpligility.ca WordPress blog.
  Covers the per-post repo layout, the Markdown-to-HTML conversion and the
  WordPress paste method that avoids its formatting traps, the hero image, and
  the post-publish cross-linking. Use when writing a new post or taking one
  through to publication.
---

# Blog post publishing

This skill covers the full pipeline for a simpligility.ca blog post, from a
Markdown draft in the repo to a published WordPress post. It is the source of
truth for the process; `blog/README.md` only points here.

**Read [`simpligility-site`](../simpligility-site/SKILL.md) first**, which in
turn extends the `manfred-writing` skill. The voice, sentence-case headings,
80-column wrap, two-domain link rule, and `STATUS.md` conventions all still
apply. This skill adds what is specific to the
blog. Unlike the log pages, a post is not a single HTML fragment: it is a
Markdown source plus a generated HTML artifact, and it is published as a real
WordPress post rather than pasted into one page.

## What belongs here

Full articles published on the simpligility.ca blog, written in Manfred's own
first-person voice. Anything that is a talk, a published article elsewhere, or a
standalone video belongs in the event, write, or video log instead, not here.

## Per-post repo layout

One folder per post under `blog/`, named `YYYYMM-<kebab-slug>`, where the prefix
is the target year and month and the slug is a short identifying name, for
example `202608-maven-build-requirements`. Each folder holds:

- `post.md` — the article in Markdown, the human-edited source of truth,
  hard-wrapped at 80 columns like every other Markdown file in the repo.
- `post.html` — the generated artifact pasted into WordPress. **Never
  hand-wrap it**, see the conversion section. Regenerate it from `post.md`
  rather than editing it by hand, and edit prose in `post.md`.
- `notes.md` — a working file with sections for ideas, title suggestions, a
  draft outline, and a running list of open items. Always keep a title
  suggestions section so alternatives are captured while drafting.
- `assets/` — the hero image and any scripts that generate it.

## Writing the post

- Follow the `manfred-writing` voice throughout, in the first person.
- Headings are sentence case, one blank line after each.
- Open with a **teaser** of one or two paragraphs, then a `<!--more-->` line.
  The teaser is shown in full at the top of the post and reused as the excerpt
  in the post list and social previews, so write it to stand on its own.
- The post title lives in the WordPress title field, not in the body. Keep the
  `# Title` heading in `post.md` for readability, but drop it from `post.html`.

## The hero image

Every post gets **one** main image, used as the WordPress featured image and in
the list and social previews. Keep it to a single image; an embedded video or
other inline media is separate from the hero.

- **Size it to the theme.** Twenty Twenty-Five's wide content slot is 1340px, so
  render the image 1340px on its binding dimension. Do not double it for retina;
  that only inflates the file.
- **Keep the file small.** Flat-color or diagram images compress hard as a small
  palette. Shrink with `pngquant` or ImageMagick to a 64-color PNG, aiming well
  under 100KB. Keep an SVG master alongside it when the image is generated, so
  it can be re-rendered sharper.
- **Generate data-driven images from a script in `assets/`** rather than by
  hand, so they are reproducible. If the script is generally useful, upstream it
  into the relevant source repository and keep the `assets/` copy as the post's
  source of truth.
- Upload the image to WordPress and set it as the post's featured image in the
  admin UI. It is not referenced inline in `post.html`.

## Converting Markdown to HTML

When the post is final, convert `post.md` to a clean, self-contained HTML
fragment saved as `post.html`. No WordPress Markdown plugin is involved, so the
Markdown stays the source and WordPress holds the rendered HTML, the same
pattern the log pages use.

Rules that keep the paste clean:

- **One block element per line. Never hard-wrap inside a block.** WordPress runs
  `wpautop` on pasted content and turns every newline inside a paragraph into a
  `<br>`, which shreds the formatting. A wrapped `post.html` is the single most
  common way to break a post. This is the one file in the repo that is not
  wrapped at 80.
- **Omit the `<h1>`.** The title goes in the WordPress title field. Body
  headings start at `<h2>`.
- **Keep the `<!--more-->`** teaser break where the teaser ends.
- **Own-site links are root-relative**, starting with `/`, per the two-domain
  rule in `simpligility-site`. External links keep their full `https://` URL.
- **Escape `<` and `>`** in inline code, for example `&lt;dependencies&gt;`.
- **A bare video URL on its own line** becomes an embed when pasted through the
  block editor. Leave the YouTube watch URL alone on its own line rather than
  wrapping it in a link.
- **Code samples** use the site's SyntaxHighlighter Evolved shortcodes rather
  than Markdown fences, matching the rest of the site.

## Pasting into WordPress

Paste through the **block editor**, not the classic editor:

1. In the post editor, open the Options menu, the three dots at the top right,
   and choose **Code editor**.
2. Paste the whole `post.html`.
3. Switch back to **Visual editor**.

The switch parses the one-line-per-block HTML into native paragraph, heading,
list, and quote blocks with the theme's normal spacing, and a bare video URL on
its own line becomes an embed. Then set the featured image in the UI.

Two things to avoid:

- **A single Custom HTML block for the whole post.** It renders without the
  theme's block typography, so the post looks cramped, and a bare URL in it does
  not auto-embed.
- **The classic editor.** Its `wpautop` turns intra-paragraph newlines into
  `<br>` and mangles the post.

After a paste, view the live post and confirm paragraphs read as prose with no
mid-sentence breaks, the video shows as a player rather than a link, and the
featured image is set.

## After publishing

Cross-link the post with its sources in both directions, so a reader arriving at
any one of them can find the rest:

- From the post to the tool, talk, or episode it is about.
- From each source back to the post: the source repository README, the linked
  video's description, and any related page.

Record these as open items in `notes.md` while drafting, since most can only be
done once the post is live and has a URL, and tick them off as they land.

## Working process and Git

- Draft on a short-lived branch off `main`, following `manfred-git`.
- Commit in focused steps while drafting, then **squash the branch into a single
  commit at publish time** with a short message describing what ships, not a
  concatenation of every drafting step.
- Keep `notes.md` and `blog/STATUS.md` current, removing items as they are done.

## Checklist

- [ ] Folder is `blog/YYYYMM-slug/` with `post.md`, `post.html`, `notes.md`, and
      `assets/`.
- [ ] Teaser is one or two paragraphs followed by `<!--more-->`.
- [ ] `post.html` has one block element per line and is not wrapped, has no
      `<h1>`, keeps `<!--more-->`, uses root-relative own-site links, and leaves
      the video URL bare on its own line.
- [ ] Hero image is a single 1340px file, palette-shrunk under 100KB, with an
      SVG master when generated, uploaded and set as the featured image.
- [ ] Pasted through the block editor code view, then switched to visual; the
      live post reads as prose, the video embeds, and the image is set.
- [ ] Cross-links are in place from the post and back to it from its sources.
- [ ] Branch squashed into one commit at publish with a short shipping message.
