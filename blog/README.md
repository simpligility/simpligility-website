# Blog

Drafts for posts published on the simpligility.ca WordPress blog. Posts are
authored in Markdown here, then converted to HTML and published to WordPress.

## Folder naming

One folder per post, named `YYYYMM-<kebab-slug>`. The prefix is the target year
and month, and the slug is a short identifying kebab-case name. For example,
`202608-maven-build-requirements`.

## Files in each folder

- `post.md` — the article in Markdown, the source of truth.
- `post.html` — the generated HTML pasted into WordPress. Regenerate it from
  `post.md`; never hand-edit or wrap it.
- `notes.md` — a working file for ideas, title suggestions, an outline, and open
  items.
- `assets/` — the hero image and any scripts that generate it.

## Process

The full process — writing, the hero image, the Markdown-to-HTML conversion and
its WordPress paste traps, and the post-publish cross-linking — lives in the
`simpligility-blog` skill, which is the source of truth. Read it before drafting
or publishing a post.
