# Blog

Drafts for posts published on the simpligility.ca WordPress blog. Posts are
authored in Markdown here, then published to WordPress.

## Folder naming

One folder per post, named `YYYYMM-<kebab-slug>`. The prefix is the target year
and month, and the slug is a short identifying kebab-case name. For example,
`202608-maven`.

## Files in each folder

- `post.md` is the article itself, written in Markdown.
- `notes.md` is a working file with sections for ideas, title suggestions, a
  draft outline, and a running list of open items to address. Always keep a
  title suggestions section so alternatives are captured while drafting.
  Iterate here alongside the post.

## Post structure

Every post should include:

- A **main image** used as the featured image and in the social and list
  previews on the site.
- An **opening teaser** of one or two paragraphs before anything else. It is
  shown in full at the top of the post and reused as the excerpt in the list of
  all posts on the site home page, so write it to stand on its own and draw the
  reader in.

## Publishing

Posts are drafted and iterated as Markdown in `post.md`. When a post is final,
convert it to a simple, self-contained HTML fragment stored alongside it as
`post.html`, matching the plain HTML style of the existing log pages. Paste that
HTML into the WordPress blog through the admin editor.

No WordPress Markdown plugin is involved. The Markdown here stays the source,
and WordPress holds the rendered HTML, the same pattern the logs use.

When a post includes code samples, convert them to the site's existing
SyntaxHighlighter Evolved shortcodes rather than leaving Markdown fences, so
they match the rest of the site.
