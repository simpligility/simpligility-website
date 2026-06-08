---
name: event-log
description: >-
  Maintain the event log HTML fragment at event-log/event-log.html for
  simpligility.ca/event-log/. Use when adding newly discovered past events,
  adding upcoming events, or keeping the layout and formatting consistent.
---

# Event log maintenance

This skill keeps `event-log/event-log.html` consistent when adding or editing
events. The file is published as an HTML fragment at
<https://simpligility.ca/event-log/> — it is embedded in a WordPress page, so
it has **no** `<html>`, `<head>`, or `<body>` wrapper. Never add one.

## Target file

- **Path (from repo root):** `event-log/event-log.html`
- It is a standalone fragment: a lead comment, a repo-management comment, a
  `<!-- Last updated -->` comment, an intro `<p>`, a one-line "Check out
  specific years" navigation `<p>`, then one `<h2>` + `<dl>` block per year.

## Deferred work: `event-log/STATUS.md`

`event-log/STATUS.md` is a tracked, living to-do list of deferred work and next
steps for the event log. It is **not** a historical log: when a task is
finished, **remove it** from the file rather than marking it done. Check it at
the start of a maintenance session, keep it current as work is deferred or
completed, and bump its "Last updated" date when you edit it.

## Committing changes

The event log, this skill, and `STATUS.md` live in the `simpligility-website`
git repo. Commit each completed change as its own focused commit and push it to
`main`. Fold any `STATUS.md` update into the same commit as the work it covers.

## File structure

```html
<!-- Event Log for simpligility.ca/event-log/ -->
<!-- Managed in the simpligility-website repo; edit there, then copy this into the WordPress page code view -->
<!-- Last updated: YYYY-MM-DD -->

<p>Many of my presentations, classes, and other events are public. ...</p>

Check out specific years:
<p><a href="#2026">2026</a>, <a href="#2025">2025</a>, ...</p>

<h2 id="2026">2026</h2>

<dl>

  <dt><strong>Title</strong><br> Date</dt>
  <dd>
    Description sentence(s).
    <a href="...">Video</a> &bull; <a href="...">Slide deck</a>
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
for it in that navigation line**, in the same newest-first order.

## Ordering rules

- **Years descending**: newest year first (`2026`, then `2025`, ...).
- **Within a year, reverse chronological**: newest event at the top of the
  `<dl>`, oldest at the bottom.
- When adding an event, insert it at the correct position by date — do not just
  append. If the year has no `<h2>`/`<dl>` block yet, create one in the right
  spot relative to the other years.

## Entry format

Each entry is a `<dt>`/`<dd>` pair, indented two spaces, with a blank line
between entries.

### The `<dt>` (title and date line)

```html
  <dt><strong>Event title</strong><br> Date</dt>
```

With an optional location between the title and the date:

```html
  <dt><strong>Event title</strong><br> San Diego, CA &mdash; 3 June 2026</dt>
```

- Title is wrapped in `<strong>`.
- **Title uses sentence case**: capitalise only the first word and any proper
  nouns (product, project, company, place, and personal names such as Trino,
  Maven, Java, Python, JavaScript, DevOps, Chainguard, Starburst, Kubernetes,
  AWS). Do
  **not** title-case every word. For example, write
  `Trino powers business intelligence`, not `Trino Powers Business
  Intelligence`. Preserve the established casing of proper nouns and acronyms.
- **A colon starts a new sentence**: capitalise the first word after a `:` in a
  title, even though the rest of the clause stays sentence case. For example,
  `Attacks rewritten: Where malware enters the build`.
- After the closing `</strong>`, separate the title from what follows with
  `<br> ` (a line break and a space), so the date/location drops to its own line
  under the title. Between any later segments (location and date) the separator
  is ` &mdash; ` (em dash with a space on each side).
- **Location** (optional) goes between title and date: `City, ST` for US
  (state abbreviation) or `City, Province` (e.g. `Vancouver, BC`). Omit for
  purely virtual/online events.
- **Date** is the last segment. Use the most precise form known. Accepted forms
  seen in the file:
  - Full date: `3 June 2026` (day month year, no comma, no ordinal suffix).
  - Date range: `5&ndash;6 August 2025` (use `&ndash;` for the range).
  - Month only: `April 2026`.
  - Approximate: `Late 2025`, `April/May 2025`.

### The `<dd>` (description and links)

```html
  <dd>
    One or two sentences describing the event.
    <a href="...">Link label</a> &bull; <a href="...">Link label</a>
    <br><br>
  </dd>
```

- Content indented four spaces.
- Start with a short description (what it was, who it was with, what it covered).
- **Do not include registration or attendance numbers** (e.g. "203
  registrations, 70 live attendees", "37 registered, 11 attended", percentage
  splits of prospects/customers). These are internal metrics and do not belong
  on the public page.
- **Do not name customers or prospects.** Never list attending or interested
  companies or individuals as customers/prospects. Public co-presenters,
  partners, vendors, hosts, and guests may be named (that is what they are there
  for); customer and prospect identities may not.
- **No separate speaker line.** Manfred Moser is the presenter, host, or
  panelist on every entry, so never name him as a speaker. Any other public
  co-presenters, partners, hosts, or guests worth recording are woven into the
  description prose (e.g. "co-presented with Patrick Smyth", "with co-host Cole
  Bowden and guest Rob Dickinson"), not put on a `Speakers:` line.
- **Links line**: one or more `<a>` links joined by ` &bull; ` (spaced bullet),
  all on a **single line** with **no leading `<br>`** — the links flow directly
  after the description. Follow the last link with `<br><br>` on its own line for
  visual separation from the next entry. Keep the whole links list on one line
  (do not break it across lines around the `&bull;` separators); a line break
  there wraps awkwardly in the rendered `<dd>`.

### Link labels and enforced order

Include only the links that apply, but always place them in this canonical
order (the recording leads):

1. `Video` — YouTube or other recording.
2. `Slide deck` — the slides for the talk. This is the single label for any
   deck; do **not** use `Presentation` (it overlaps with the `Video` recording
   of the same talk). Prefer a PDF self-hosted on simpligility.ca
   (`/wp-content/uploads/...`), but a link to a web-hosted deck elsewhere is
   fine **as long as it is publicly accessible** — that is the only hard
   requirement. Google Slides links were dropped precisely because they were
   not public; never link a deck a visitor cannot open.
3. `Details` — any "read more about this event" page: post-event recap blog,
   the event's own page, etc. This is the consolidated label for such
   supporting pages. **Exception:** for **Trino Community Broadcast** episodes,
   label the `trino.io/episodes/N` page `Detailed show notes` (not `Details`).
4. `Registration` / `Registration page` — sign-up link for upcoming events.

Do **not** add internal tracking issue links. They link to private GitHub
issues and do not belong on the public page. Existing entries still contain
them; they are being removed over time, so never add new ones.

#### Handling multiple supporting pages

`Details` is the default for a "read more" page, but **never use the same link
text twice** in one entry — duplicate `Details` links are ambiguous and bad for
accessibility. So:

- **One** supporting page → label it `Details`.
  `Video &bull; Slide deck &bull; <a ...>Details</a>`
- **Two or more** supporting pages → drop the generic `Details` and give each a
  short, specific label instead, keeping them in the order above.
  `Video &bull; Slide deck &bull; <a ...>Show notes</a> &bull; <a ...>Recap</a>`

Existing entries predate this rule and may use older labels (`Show notes`,
`Recap blog post`, `Keynote details on event site`); match this scheme for new
and edited entries. If you are editing an entry that still has an internal
tracking issue link, ask the user for confirmation before removing it — do not
remove it automatically.

## Internal links must be root-relative

The site is served under **both** `simpligility.ca` and `simpligility.com`, so
links to the site's own content must be **root-relative** — start them with `/`
and never hard-code a domain.

- Correct: `<a href="/wp-content/uploads/2026/05/talk.pdf">Slide deck</a>`
- Wrong: `<a href="https://simpligility.ca/wp-content/uploads/2026/05/talk.pdf">`
  (breaks/forces one domain when viewed on the other)

This applies to any link pointing at this site (e.g. `Slide deck` PDFs under
`/wp-content/uploads/...`). External links (YouTube, a publicly hosted deck
elsewhere, chainguard.dev, trino.io, etc.) keep their full `https://` URLs.

## HTML entity conventions

Use named entities, matching the existing file:

- `&mdash;` — em dash separator in the `<dt>` line.
- `&ndash;` — en dash for ranges (date ranges, time ranges, `10:00&ndash;11:00`).
- `&bull;` — bullet separator between links.
- `&amp;` — ampersand in text (e.g. `Q&amp;A`).
- `&#39;` — apostrophe inside attribute-adjacent text where needed
  (e.g. `Trino&#39;s`).
- `<em>...</em>` — for talk/topic titles quoted inside a description.

## Process for adding a new entry

1. **Gather the facts from the source(s).** Start from whatever the user
   provides — a blog post, video, event page, slide deck — and fetch each
   source to pull out:
   - the **title** (the talk/event/post name),
   - the **date** (most precise form available),
   - whether it was **in person** (note the location) or **virtual**,
   - a **one or two sentence description** of what it was and what it covered,
   - all relevant **links** (video, presentation PDF, slide deck, the source
     page itself, registration).

   If the user mentions an artifact ("the video", "the slides") but does not
   give a URL, and you cannot find it reliably, **ask for the URL** rather than
   guessing — never invent a link.
2. Read `event-log/event-log.html`.
3. Determine the year and date; find the matching `<h2>`/`<dl>` block (or
   create one in the correct descending-year position — and when creating a new
   year, give its `<h2>` an `id="YYYY"` and add a matching comma-separated
   `<a href="#YYYY">` link to the "Check out specific years" navigation line).
4. Build the `<dt>`/`<dd>` pair following the formats above:
   - Title in `<strong>`, **sentence case** (a colon capitalises the next word).
   - **In-person** → location before the date; **virtual** → omit the location.
   - Description first, then the links line.
   - Links in the **canonical order** (Video, Slide deck, Details,
     Registration); a single "read more" page is `Details` (`Detailed show
     notes` for a Trino Community Broadcast episode).
5. Insert it at the correct reverse-chronological position within the year,
   with a blank line separating it from neighbours.
6. Update the `<!-- Last updated: YYYY-MM-DD -->` comment near the top to
   today's date.
7. Sanity-check: tags balanced, entities used, indentation consistent (two
   spaces for `<dt>`/`<dd>`, four for `<dd>` content).

### Worked example

Source: the blog post *Fork yeah: We're bringing kaniko back*
(`chainguard.dev/unchained/...`), published 5 June 2025, plus its companion
video. It is a virtual artifact (no location), the source page is the single
"read more" link (`Details`), and the video leads. The resulting entry, placed
in the `2025` block between the 6 June and 14 May entries:

```html
  <dt><strong>Fork yeah: We&#39;re bringing kaniko back</strong><br> 5 June 2025</dt>
  <dd>
    Blog post and video on Chainguard forking the kaniko container build tool after Google archived it, committing to maintain it as open source.
    <a href="https://www.youtube.com/watch?v=NPOC2n-anAU">Video</a> &bull; <a href="https://www.chainguard.dev/unchained/fork-yeah-were-bringing-kaniko-back">Details</a>
    <br><br>
  </dd>
```

## Checklist before finishing

- [ ] Entry is in the right year block and reverse-chronological position.
- [ ] `<dt>` uses `<strong>` title, `<br> ` after the closing `</strong>`,
      ` &mdash; ` between location and date, correct date form.
- [ ] Location included for in-person events, omitted for virtual ones.
- [ ] Links use the spaced ` &bull; ` separator and follow the canonical order
      (Video, Slide deck, Details, Registration), and a deck uses the label
      `Slide deck`, never `Presentation`.
- [ ] The links list is on a single line with no leading `<br>`, followed by
      `<br><br>` on its own line; no separate `Speakers:` line (other names are
      woven into the description, and Manfred is never named as a speaker).
- [ ] A single "read more" page is labelled `Details` (or `Detailed show notes`
      for a Trino Community Broadcast episode's `trino.io` page); multiple such
      pages use distinct specific labels (no duplicate link text).
- [ ] No new internal tracking issue links added; removal of an existing one
      was confirmed with the user first.
- [ ] HTML entities (`&mdash;`, `&ndash;`, `&bull;`, `&amp;`) used, not raw
      characters.
- [ ] Own-site links are root-relative (start with `/`), not full
      `simpligility.ca`/`simpligility.com` URLs.
- [ ] Indentation and blank-line spacing match surrounding entries.
- [ ] `<!-- Last updated -->` date bumped.
- [ ] If a new year block was created, its `<h2>` has `id="YYYY"` and the "Check
      out specific years" navigation line has a matching `<a href="#YYYY">` link.
- [ ] No `<html>`/`<head>`/`<body>` wrapper introduced.
