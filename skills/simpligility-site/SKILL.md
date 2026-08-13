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

Pasted HTML fragments inherit the theme's narrow content column. To make a page
wider:

- Native and update-safe: wrap the content in a Group block and set its
  alignment to **Wide width**, or **Full width** for edge-to-edge coverage.
- Alternatively, scope custom CSS to the page by its body class, for example
  `.page-id-1743`, in the Site Editor under Styles, Additional CSS.

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
