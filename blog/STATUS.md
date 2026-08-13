# Blog — work status and next steps

Working notes for the blog post drafts in this directory and for the WordPress
blog publishing setup. This is a living to-do list: delete items as they are
done, and bump the "Last updated" date on edits. The folder and file
conventions are in [`README.md`](README.md).

Last updated: 2026-08-12 (added the blog layout and archive task)

---

## 1. Take the first post through the publishing pipeline

The publishing approach is decided: draft in Markdown here, convert to a simple
HTML fragment by hand, and paste it into the WordPress blog through the admin.
No WordPress plugins are involved. The full workflow is in
[`README.md`](README.md).

The Maven post in `202608-maven/` is the first one through this pipeline. Once
it is drafted and converted, paste it into WordPress, check how the rendered
result looks, and note any adjustments the conversion approach needs for future
posts.

## 2. Improve the blog layout and expose the archive

Tidy up the blog layout on the site and surface the post archive far better.
The full list of posts is currently hard to find. Make it easy to reach and
browse, with each entry showing its title and teaser excerpt rather than a bare
link. This is a WordPress area, so the work happens in the WordPress admin and
theme, not in this repo.
