---
name: simpligility-site
description: >-
  Shared facts and conventions for the simpligility.ca WordPress site: the
  platform and theme, page width, how page fragments are published, the page
  inventory and writing voice, the two-domain link rule, and the entry format
  the event, write, and video logs have in common. Base skill for the
  per-section simpligility skills. Load it for the shared site context before
  working on any page.
---

# simpligility.ca site

Base skill holding the shared facts for maintaining the simpligility.ca site, so
the per-section skills do not each carry their own copy. It extends the
`manfred-writing` skill: the voice, formatting, and markdown conventions there
still apply, and this skill adds what is specific to the site.

Activate it when the `manfred` skill is already active or when Manfred asks for
it by name, together with the section skill for the page being worked on.

## Section skills

Each maintained page has its own skill for what only that page needs: what
belongs on it, its middle slot, its link labels, its sources already swept, and
its process. Invoke the matching one through the Skill tool:

| Page | Skill |
|------|-------|
| `event-log/event-log.html` | `simpligility-event-log` |
| `write-log/write-log.html` | `simpligility-write-log` |
| `video-log/video-log.html` | `simpligility-video-log` |
| `manfred-mentors/manfred-mentors.html` | `simpligility-manfred-mentors` |

Where a section skill repeats a rule from here, this file is the source of
truth. The sections on the fragment skeleton, year navigation, ordering, and
entry format below describe the **three log pages**; the Manfred mentors archive
has no year blocks and defines its own entry format.

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

Only some of the site is managed in this repo:

- **In the repo** are the page fragments, their `STATUS.md` files, and these
  skills. Page content is authored here as HTML fragments and pasted into the
  WordPress page code view. Fragments carry no `<html>`, `<head>`, or `<body>`
  wrapper.
- **In WordPress only** are the profile pages `/about/`, `/writing/`, `/teach/`,
  `/community/`, and `/code/`, the parts of `/manfred-mentors/` above the
  archive, and the blog. Changes to those are made in the WordPress admin, so
  the deliverable is reviewed copy to paste rather than a commit.
- Installed plugins are minimal: SyntaxHighlighter Evolved for code. No Markdown
  plugin is used, so Markdown drafts are converted to simple HTML before they go
  into a page.

The profile pages cross-link the logs, so a change to what a page covers can
leave a profile page wrong. When the scope of a log changes, check whether
`/writing/`, `/teach/`, `/community/`, or `/code/` needs its wording updated
too.

## Voice

The site mixes two voices on purpose, split by whether a page describes Manfred
or is written by him:

- **Third person** on the profile pages `/about/`, `/writing/`, `/teach/`,
  `/community/`, and `/code/`. These read as the company's description of
  Manfred, which `/about/` sets up with "simpligility technologies inc. is the
  one man company of Manfred Moser".
- **First person** in the blog, in the three logs, and on the Manfred mentors
  page. These are Manfred's record of his own work, so the write log opens
  "Over the years I have written for many sites and publications" and the video
  log matches.

**Never mix the two within one page.** A profile page that slips into "I have
led all of these" is the defect to fix, not a style to preserve. Crossing from a
profile page into a log changes the voice, and that is fine, because the reader
crosses a clear line from "about Manfred" to "by Manfred" at the same time.

## Internal links must be root-relative

The site is served under **both** `simpligility.ca` and `simpligility.com`, so
every link to the site's own content must be **root-relative**. Start it with
`/` and never hard-code a domain.

- Correct: `<a href="/wp-content/uploads/2026/05/talk.pdf">Slide deck</a>`
- Wrong: `<a href="https://simpligility.ca/wp-content/uploads/2026/05/talk.pdf">`

Hard-coding a domain forces one of the two on a visitor who arrived at the
other. This applies to uploads, to the log pages, and to the profile pages
alike. External links keep their full `https://` URLs.

## The log fragment skeleton

Every log fragment has the same shape:

```html
<!-- <Name> Log for simpligility.ca/<name>-log/ -->
<!-- Managed in the simpligility-website repo; edit there, then copy this into the WordPress page code view -->
<!-- Last updated: YYYY-MM-DD -->

<p>Intro paragraph ...</p>

Check out specific years:
<p><a href="#2026">2026</a>, <a href="#2025">2025</a>, ...</p>

<h2 id="2026">2026</h2>

<dl>

  <dt><strong>Title</strong><br> Middle slot &mdash; Date</dt>
  <dd>
    Description sentence or two.
    <a href="...">Leading link</a> &bull; <a href="...">Other link</a>
    <br><br>
  </dd>

</dl>
<h2 id="2025">2025</h2>

<dl>
  ...
</dl>
```

Bump the `<!-- Last updated: YYYY-MM-DD -->` comment to today's date on every
edit.

### Year navigation

Each `<h2>` year heading carries `id="YYYY"`, and the "Check out specific years"
navigation `<p>` below the intro is a single line of comma-separated
`<a href="#YYYY">` links, kept on one line to save vertical space. **When you
add a year block you must also give its `<h2>` the matching `id` and add a
comma-separated link for it in that navigation line**, in the same newest-first
order.

### The sticky year navigation block

Each log fragment ends with a self-contained sticky year navigation block, a
floating scroll-aware jump list built from the year headings, with inline CSS
and JS and a `Top` link. Its lead comment says to keep it identical across the
three logs, and it currently is, byte for byte.

Treat it as one shared asset: never edit it in a single log. A change goes into
all three fragments in the same commit, and the blocks are verified identical
afterwards. Adding or renaming a year block needs no change here, because the
list is built from the headings at runtime.

## Ordering rules

- **Years descending**, newest year first.
- **Within a year, reverse chronological**, newest entry at the top of the
  `<dl>` and oldest at the bottom.
- Insert at the correct position by date rather than appending. If the year has
  no `<h2>` and `<dl>` block yet, create one in the right spot relative to the
  other years.

## Entry format

Each entry is a `<dt>` and `<dd>` pair indented two spaces, with a blank line
between entries.

### The `<dt>` line

```html
  <dt><strong>Title</strong><br> Middle slot &mdash; Date</dt>
```

- Title is wrapped in `<strong>`.
- **Title uses sentence case.** Capitalize only the first word and proper nouns
  such as Trino, Maven, Java, Python, JavaScript, DevOps, Chainguard, Starburst,
  Sonatype, Kubernetes, Android, OneOps, and AWS. Do not title-case every word,
  and preserve the established casing of proper nouns and acronyms. Use the real
  title of the thing and adjust only the casing.
- **A colon starts a new sentence.** Capitalize the first word after a `:`, as
  in `Attacks rewritten: Where malware enters the build`.
- After the closing `</strong>` comes `<br> `, a line break and a space, so what
  follows drops to its own line under the title. Later segments are separated by
  ` &mdash; `, an em dash with a space on each side.
- **The middle slot** is what each log puts between the title and the date: a
  location in the event log, the publication in the write log, and the
  series or channel in the video log. Each section skill defines its own, and
  each says when to omit it. It holds a clean human name, never a bare URL.
- **Date** is the last segment, in the most precise form known:
  - Full date: `5 June 2025`, day month year, no comma and no ordinal suffix.
  - Date range: `5&ndash;6 August 2025`.
  - Month only: `April 2026`.
  - Approximate: `Late 2025`, `April/May 2025`.

### The `<dd>` block

```html
  <dd>
    One or two sentences describing it.
    <a href="...">Leading link</a> &bull; <a href="...">Other link</a>
    <br><br>
  </dd>
```

- Content indented four spaces.
- Start with a short description of what it was and what it covered.
- **Never name Manfred.** He is the author, presenter, or host of every entry on
  every log, so naming him adds nothing. Public co-presenters, co-authors,
  partners, hosts, and guests may be named, and they are woven into the
  description prose rather than put on a separate line.
- **Never name customers or prospects**, and never include registration or
  attendance numbers. Those are internal metrics and do not belong on a public
  page.
- **Links line**: one or more `<a>` links joined by ` &bull; `, all on a
  **single line** with **no leading `<br>`**, so they flow directly after the
  description. Follow the last link with `<br><br>` on its own line. Keep the
  whole list on one line, because a break around a separator wraps awkwardly in
  the rendered `<dd>`.

### Link rules

Each section skill defines its own canonical link order, led by the artifact the
page is a list of: the recording in the event log, the post in the write log,
and the video in the video log. Across all of them:

- **No two links in one entry may share the same link text.** When a second
  supporting page appears, drop the generic `Details` label and give each a
  short specific label instead.
- **Never link something a visitor cannot open.** A deck behind a login or a
  private video is not a link, whatever it is labelled.
- **Never add internal tracking issue links.** They point at private GitHub
  issues. Older entries still carry some; they are being removed over time, so
  do not add new ones, and confirm with Manfred before removing an existing one.

## Broken and dead links

Many entries are old and their links rot. The standing rules:

- **Never delete an entry, and never silently strip its link, just because a URL
  no longer resolves.** The talk, post, or video still happened, so the record
  stays. A dead link is a per-entry decision for Manfred.
- **Try to find a better URL first**: the current location of the page, a
  republished copy, or an archived snapshot from the Wayback Machine at
  `web.archive.org`. Prefer a live link and fall back to an archive link when
  that is all that survives.
- If nothing works, **flag the entry for Manfred and leave it as is**.

For a video, check liveness before linking. A removed or private video fails a
YouTube oEmbed request at
`https://www.youtube.com/oembed?url=<watch-url>&format=json`.

## HTML entity conventions

Use named entities in every fragment:

- `&mdash;` for the em dash separator in the `<dt>` line.
- `&ndash;` for ranges, including date and time ranges.
- `&bull;` for the separator between links.
- `&amp;` for an ampersand in text, as in `Q&amp;A`.
- `&#39;` for an apostrophe in attribute-adjacent text, as in `Trino&#39;s`.
- `<em>...</em>` for a title quoted inside a description.

## STATUS files

Each maintained page has a `STATUS.md` next to it, and the repo root has one for
work that spans more than one page or the site as a whole. They are living to-do
lists, not historical logs:

- When a task is finished, **remove it** rather than marking it done.
- Bump the "Last updated" line, with a short note of what changed, on every
  edit.
- Check the relevant file at the start of a session and keep it current as work
  is deferred or completed.
- A settled decision or a swept source is **not** status. Move it into the
  matching skill under *Sources already swept*, *Channels already swept*, or
  *Standing decisions*, so it is not re-proposed later.

## Committing changes

The fragments, the `STATUS.md` files, and these skills live in the
`simpligility-website` git repo. Commit each completed change as its own focused
commit and push it to `main`. Fold the `STATUS.md` update into the same commit
as the work it covers. Commit message conventions come from `manfred-git`.

## Checklist for any log edit

- [ ] Entry is in the right year block and in reverse-chronological position.
- [ ] `<dt>` uses a `<strong>` sentence-case title, `<br> ` after the closing
      `</strong>`, ` &mdash; ` before the date, and a correct date form.
- [ ] The middle slot is a clean human name, and the full URL is in the link.
- [ ] Links use the spaced ` &bull; ` separator, the artifact leads, and no two
      links share the same link text.
- [ ] The links list is on a single line with no leading `<br>`, followed by
      `<br><br>` on its own line.
- [ ] Manfred is not named, no customers or prospects are named, and no
      attendance numbers appear.
- [ ] No internal tracking issue links were added.
- [ ] Named HTML entities are used rather than raw characters.
- [ ] Own-site links are root-relative and start with `/`.
- [ ] Indentation and blank-line spacing match the surrounding entries.
- [ ] The `<!-- Last updated -->` comment is bumped.
- [ ] A new year block has an `id="YYYY"` on its `<h2>` and a matching link in
      the "Check out specific years" line.
- [ ] The sticky year navigation block is untouched, or changed identically in
      all three fragments.
- [ ] No `<html>`, `<head>`, or `<body>` wrapper was introduced.
