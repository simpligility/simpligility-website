---
name: write-log
description: >-
  Maintain the write log HTML fragment at write-log/write-log.html for
  simpligility.ca/write-log/. Use when adding newly discovered blog posts or
  articles Manfred has written, or keeping the layout and formatting consistent.
---

# Write log maintenance

This skill keeps `write-log/write-log.html` consistent when adding or editing
entries. The write log is the companion to the [event log](../../event-log/):
the event log tracks public events, the write log tracks written blog posts and
articles across the various sites Manfred has written for. The two share their
structure and conventions, and the source research overlaps.

The file is published as an HTML fragment at <https://simpligility.ca/write-log/>
— it is embedded in a WordPress page, so it has **no** `<html>`, `<head>`, or
`<body>` wrapper. Never add one.

## Target file

- **Path (from repo root):** `write-log/write-log.html`
- It is a standalone fragment: a lead comment, a repo-management comment, a
  `<!-- Last updated -->` comment, an intro `<p>`, a one-line "Check out specific
  years" navigation `<p>`, then one `<h2>` + `<dl>` block per year.

## Deferred work: `write-log/STATUS.md`

`write-log/STATUS.md` is a tracked, living to-do list of deferred work and next
steps for the write log (chiefly the harvesting of posts from each site). It is
**not** a historical log: when a task is finished, **remove it** from the file
rather than marking it done. Check it at the start of a session, keep it current,
and bump its "Last updated" date when you edit it.

## Committing changes

The write log, this skill, and `STATUS.md` live in the `simpligility-website`
git repo. Commit each completed change as its own focused commit and push it to
`main`. Fold any `STATUS.md` update into the same commit as the work it covers.

## File structure

```html
<!-- Write Log for simpligility.ca/write-log/ -->
<!-- Managed in the simpligility-website repo; edit there, then copy this into the WordPress page code view -->
<!-- Last updated: YYYY-MM-DD -->

<p>Over the years I have written many blog posts and articles ...</p>

Check out specific years:
<p><a href="#2026">2026</a>, <a href="#2025">2025</a>, ...</p>

<h2 id="2026">2026</h2>

<dl>

  <dt><strong>Post title</strong><br> Publication &mdash; Date</dt>
  <dd>
    Description sentence(s).
    <a href="...">Read on example.com</a> &bull; <a href="...">Video</a>
    <br><br>
  </dd>

</dl>
<h2 id="2025">2025</h2>

<dl>
  ...
</dl>
```

### Year navigation

Each `<h2>` year heading carries `id="YYYY"` (e.g. `<h2 id="2025">2025</h2>`),
and the "Check out specific years" navigation `<p>` below the intro is a single
line of comma-separated `<a href="#YYYY">` links (kept on one line to save
vertical space). **When you add a new year block, you must also (1) give its
`<h2>` the matching `id` and (2) add a comma-separated `<a href="#YYYY">` link
for it in that navigation line**, in the same newest-first order. The first
entry you add to the empty scaffold creates the first year block and the first
navigation link.

## Ordering rules

- **Years descending**: newest year first (`2026`, then `2025`, ...).
- **Within a year, reverse chronological**: newest post at the top of the `<dl>`,
  oldest at the bottom.
- When adding a post, insert it at the correct position by date — do not just
  append. If the year has no `<h2>`/`<dl>` block yet, create one in the right
  spot relative to the other years.

## Entry format

Each entry is a `<dt>`/`<dd>` pair, indented two spaces, with a blank line
between entries.

### The `<dt>` (title, publication, and date line)

```html
  <dt><strong>Post title</strong><br> Publication &mdash; Date</dt>
```

- Title is wrapped in `<strong>`.
- **Title uses sentence case**: capitalise only the first word and any proper
  nouns (product, project, company, place, and personal names such as Trino,
  Maven, Java, Python, JavaScript, DevOps, Chainguard, Starburst, Sonatype,
  Kubernetes, Android, AWS). Do **not** title-case every word. Preserve the
  established casing of proper nouns and acronyms. Use the post's real title;
  only adjust casing to fit this scheme.
- **A colon starts a new sentence**: capitalise the first word after a `:` in a
  title.
- After the closing `</strong>`, separate the title from what follows with
  `<br> ` (a line break and a space), so the publication/date drop to their own
  line under the title. Between the publication and the date the separator is
  ` &mdash; ` (em dash with a space on each side).
- **Publication** is where the post appeared — the blog or site name, in the
  position the event log uses for location. Use a clean, human name for the
  site, not a bare URL: `Chainguard blog`, `Sonatype blog`, `Trino blog`,
  `simpligility.ca`, `DZone`, `InfoQ`. The full URL goes in the link below, not
  here.
- **Date** is the last segment. Use the most precise form known:
  - Full date: `5 June 2025` (day month year, no comma, no ordinal suffix).
  - Month only: `April 2026`.
  - Approximate: `Late 2025`, `April/May 2025`.

### The `<dd>` (description and links)

```html
  <dd>
    One or two sentences describing what the post covered.
    <a href="...">Read on example.com</a> &bull; <a href="...">Video</a>
    <br><br>
  </dd>
```

- Content indented four spaces.
- Start with a short description: what the post was about and, when relevant,
  who it was co-written with or what it tied to.
- Public co-authors, partners, and interviewees may be named; do not name
  customers or prospects, and do not name Manfred as the author (he is the
  author of every entry).
- **Links line**: one or more `<a>` links joined by ` &bull; ` (spaced bullet),
  all on a **single line** with **no leading `<br>`** — the links flow directly
  after the description. Follow the last link with `<br><br>` on its own line for
  visual separation from the next entry. Keep the whole links list on one line.

### Link labels and enforced order

The post itself always leads, since the page is a list of posts. Include only
the links that apply, in this canonical order:

1. **The post** — the canonical link to read it. Label it `Read on <site>` using
   the host the link points at (e.g. `Read on chainguard.dev`,
   `Read on trino.io`, `Read on simpligility.ca`). This keeps the label
   distinct from the human publication name in the `<dt>` and tells the reader
   where the link goes.
2. `Also at <site>` — a republished/cross-posted copy elsewhere, if any. Use the
   other host in the label so the two read-links never share the same text.
3. `Video` — a companion recording for the post, if one exists.
4. `Details` — a related page (the event it accompanied, a project page, a
   follow-up). Use a specific label instead if there is more than one, so no two
   links in an entry ever share the same link text.

Do **not** add internal tracking issue links — they point at private GitHub
issues and do not belong on the public page.

## Internal links must be root-relative

The site is served under **both** `simpligility.ca` and `simpligility.com`, so
links to the site's own content must be **root-relative** — start them with `/`
and never hard-code a domain.

- Correct: `<a href="/2014/05/some-old-post/">Read on simpligility.ca</a>`
- Wrong: `<a href="https://simpligility.ca/2014/05/some-old-post/">`
  (breaks/forces one domain when viewed on the other)

External links (Chainguard, Sonatype, Trino, DZone, YouTube, etc.) keep their
full `https://` URLs.

## Broken and dead links

Many entries are old posts whose links rot over time — for example the imported
`blog.sonatype.com` URLs. The standing rules:

- **Never delete an entry, and never silently strip its link, just because a URL
  no longer resolves.** The post still happened; the record stays. A dead link
  is a per-entry decision for Manfred, not a cleanup to make automatically.
- When you notice or suspect a broken link, **try to find a better URL first**:
  the post at the site's current location, a republished copy, or an archived
  snapshot (e.g. the Wayback Machine, `web.archive.org`). Prefer a live link;
  fall back to an archive link when that is all that survives.
- If no working URL can be found, **flag the entry for Manfred and leave it as
  is** — do not remove the link or the entry on your own. Surface it and let him
  decide how to proceed for that specific entry.
- We may later formalize a convention for an entry whose link is unrecoverable
  (e.g. dropping the broken `href` but keeping the title, publication, date, and
  a note of where it used to point, so the entry stays on the page). Until that
  convention is written here, do not invent one — ask.

See write-log STATUS item on finding better URLs for the tracked follow-up work.

## HTML entity conventions

Use named entities, matching the event log:

- `&mdash;` — em dash separator between publication and date in the `<dt>` line.
- `&ndash;` — en dash for ranges.
- `&bull;` — bullet separator between links.
- `&amp;` — ampersand in text (e.g. `Q&amp;A`).
- `&#39;` — apostrophe inside attribute-adjacent text where needed
  (e.g. `Trino&#39;s`).
- `<em>...</em>` — for titles quoted inside a description.

## Process for adding a new entry

1. **Gather the facts from the source.** Fetch the post and pull out:
   - the **title** (the post's real headline),
   - the **publication** (the site/blog it appeared on),
   - the **date** published (most precise form available),
   - a **one or two sentence description** of what it covered,
   - the **canonical link** to read it, plus any cross-post, companion video, or
     related page.

   If you cannot find a reliable link for an artifact the user mentions, **ask
   for the URL** rather than guessing — never invent a link.
2. Read `write-log/write-log.html`.
3. Determine the year and date; find the matching `<h2>`/`<dl>` block (or create
   one in the correct descending-year position — and when creating a new year,
   give its `<h2>` an `id="YYYY"` and add a matching comma-separated
   `<a href="#YYYY">` link to the navigation line).
4. Build the `<dt>`/`<dd>` pair: title in `<strong>` sentence case, publication
   and date in the `<dt>`, description then the links line with the post leading
   in the canonical order.
5. Insert it at the correct reverse-chronological position within the year, with
   a blank line separating it from neighbours.
6. Update the `<!-- Last updated: YYYY-MM-DD -->` comment to today's date.
7. Sanity-check: tags balanced, entities used, indentation consistent (two
   spaces for `<dt>`/`<dd>`, four for `<dd>` content).

### Worked example

Source: the blog post *Fork yeah: We're bringing kaniko back* on the Chainguard
blog (`chainguard.dev/unchained/...`), published 5 June 2025, with a companion
video. Placed in the `2025` block:

```html
  <dt><strong>Fork yeah: We&#39;re bringing kaniko back</strong><br> Chainguard blog &mdash; 5 June 2025</dt>
  <dd>
    On Chainguard forking the kaniko container build tool after Google archived it, and committing to maintain it as open source.
    <a href="https://www.chainguard.dev/unchained/fork-yeah-were-bringing-kaniko-back">Read on chainguard.dev</a> &bull; <a href="https://www.youtube.com/watch?v=NPOC2n-anAU">Video</a>
    <br><br>
  </dd>
```

## Checklist before finishing

- [ ] Entry is in the right year block and reverse-chronological position.
- [ ] `<dt>` uses `<strong>` title, `<br> ` after the closing `</strong>`,
      ` &mdash; ` between publication and date, correct date form.
- [ ] Publication is a clean human site name in the `<dt>`; the full URL is in
      the link, not the `<dt>`.
- [ ] Links use the spaced ` &bull; ` separator, the post leads with a
      `Read on <site>` label, and no two links share the same link text.
- [ ] The links list is on a single line with no leading `<br>`, followed by
      `<br><br>` on its own line; Manfred is not named as the author.
- [ ] No internal tracking issue links added.
- [ ] HTML entities (`&mdash;`, `&ndash;`, `&bull;`, `&amp;`) used, not raw
      characters.
- [ ] Own-site links are root-relative (start with `/`), not full
      `simpligility.ca`/`simpligility.com` URLs.
- [ ] Indentation and blank-line spacing match the established entries.
- [ ] `<!-- Last updated -->` date bumped.
- [ ] If a new year block was created, its `<h2>` has `id="YYYY"` and the "Check
      out specific years" navigation line has a matching `<a href="#YYYY">` link.
- [ ] No `<html>`/`<head>`/`<body>` wrapper introduced.
