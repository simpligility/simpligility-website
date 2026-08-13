---
name: simpligility-site
description: >-
  Shared facts and conventions for the simpligility.ca WordPress site: the
  platform and theme, how page fragments are published, and site-wide link
  rules. Base skill for the per-section simpligility skills. Load it for the
  shared site context before working on any page.
---

# simpligility.ca site

Base skill holding the shared facts for maintaining the simpligility.ca site.
The per-section skills for the event log, write log, video log, Manfred mentors,
and blog build on this shared context.

## Platform and theme

- The site runs on WordPress 7, using the **Twenty Twenty-Five** theme.
- Twenty Twenty-Five is a block theme, so page content is constrained to a
  narrow content column by default.

## Page width

Twenty Twenty-Five constrains page content to a narrow column, 645px by default,
with 1340px for wide alignment. Pasted HTML fragments inherit the 645px column,
so a wide archive or list looks cramped.

The reliable way to widen a single page is a scoped CSS override in the Site
Editor under Styles, Additional CSS. Raise the content size for that page by its
`page-id-<id>` body class:

```css
.page-id-1743 {
  --wp--style--global--content-size: 1100px;
}
```

This affects only that page, so the rest of the site keeps its 645px column. The
Manfred mentors page is `page-id-1743`. Adjust the value up toward 1340px or
beyond to taste.

The block editor alternative is to wrap the content in a Group and set its
alignment to Wide width. On its own that widens the group but not the content
inside it, because the group keeps a constrained inner layout. To make the
content fill the wide group, also turn off "Inner blocks use content width" in
the group's Layout panel. The CSS override is more predictable, so prefer it.

## Publishing model

- Page content is authored in this repo as HTML fragments and pasted into the
  WordPress page code view. Fragments carry no `<html>`, `<head>`, or `<body>`
  wrapper.
- Installed plugins are minimal: SyntaxHighlighter Evolved for code. No Markdown
  plugin is used, so Markdown drafts are converted to simple HTML before they go
  into a page.

## Site-wide link rule

The site is served under both simpligility.ca and simpligility.com, so internal
links must be root-relative, starting with `/`, and must never hard-code a
domain. External links keep their full `https://` URLs.

## Section skills

Per-section maintenance lives in the sibling skills: `simpligility-event-log`,
`simpligility-write-log`, `simpligility-video-log`, and
`simpligility-manfred-mentors`.
