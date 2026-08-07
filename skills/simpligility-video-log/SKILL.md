---
name: simpligility-video-log
description: >-
  Maintain the video log HTML fragment at video-log/video-log.html for
  simpligility.ca/video-log/. Use when adding standalone tutorial or
  educational videos (and video series) not tied to a specific event, or
  keeping the layout and formatting consistent.
---

# Video log maintenance

This skill keeps `video-log/video-log.html` consistent when adding or editing
entries. The video log is the companion to the [event log](../../event-log/)
and the [write log](../../write-log/): the event log tracks public events, the
write log tracks written blog posts and articles, and the video log tracks
**standalone videos** — tutorials, explainers, and educational series Manfred
recorded that are **not** tied to a specific event. The three share their
structure and conventions, and the source research overlaps.

The file is published as an HTML fragment at <https://simpligility.ca/video-log/>
— it is embedded in a WordPress page, so it has **no** `<html>`, `<head>`, or
`<body>` wrapper. Never add one.

## What belongs here (and what does not)

The video log is **only** for videos that exist independently of any event or
article. The dividing line with the other two logs:

- A video that is the **recording of an event** (a talk, a class, a broadcast
  episode) stays a `Video` **link** on its **event-log** entry — it does **not**
  get a video-log entry.
- A video that is the **companion to a post** stays a `Video` **link** on its
  **write-log** entry — it does **not** get a video-log entry.
- A video that stands on its own — a tutorial, a how-to, an explainer, a
  training series — with no event or article behind it, **is** a video-log
  entry.

If a video could plausibly belong to an event or post, prefer linking it there
and leave it out of the video log, to avoid double-listing the same artifact.

### Videos already handled — do not re-add

The simpligility.ca blog-discovery pass surfaced a few videos that are already
in the right place. They are recorded here so they are not re-proposed as new
video-log entries:

- The eight-part *Easy publishing to the Central Repository* series, linked from
  the 26 April 2016 blog post, is already a video-log entry in the `2010–2016`
  section.
- FLOSS Weekly episode 577 from 2020, the DevOpsDays Vancouver 2016 Ignite talk
  recording, and the SiliconANGLE theCUBE interview from 2023 are event
  recordings and live in the event log, not here.

### Migrating a misfiled video out of the event log

A standalone video with no event or article behind it belongs here even when it
currently sits in the event log, as the OneOps training series once did. Treat
moving one as a per-entry judgment: flag the candidate and confirm with Manfred
before moving it. When you do move it, delete the event-log entry, along with
that year's navigation link if it was the only entry in the year, in the same
commit that adds it here. The event log has been reviewed end to end and holds
no such misfiled videos, so this is a check to run on new additions rather than
a backlog to work through.

## One entry vs one entry per video

This is the key decision when adding videos. Two shapes:

1. **A one-off or finished series** — a set of videos produced once, published
   together, usually as a single playlist (for example the OneOps user training
   class). Add it as **one entry** that links the playlist. The series has a
   single date (when it was released).
2. **An open-ended category or brand** — a recurring title that is really an
   umbrella for many separate videos that accrue over time and can span years,
   such as an ongoing show or a rolling explainer series. Add **one entry per
   video**, each with its own title, its own date, and the category name in the
   series/channel slot of the `<dt>`. This mirrors how each Trino Community
   Broadcast episode is its own event-log entry: separate dated entries let the
   category sort correctly and span multiple year blocks.

When unsure which shape applies, ask: *does this title name one finished thing,
or an ongoing line of separate videos?* The first is one entry; the second is
one entry per video.

**Exception — *Manfred mentors*.** *Manfred mentors* is exactly this
open-ended shape, but it is **not** listed in the video log. The show is an
ongoing live stream with its own home at
<https://simpligility.ca/manfred-mentors/>, and the video-log intro points
there instead — the same way the write log points to the blog for self-hosted
posts. Do not add its episodes here.

## Legacy archive collections

Older collections (for example the Sonatype Nexus how-to series harvested from
the site's former `/video/` page) come organized **per playlist/session**, often
with many videos no longer available and uncertain dates. Handle these specially:

- **One entry per session/series** (the finished-series rule), with the series
  name as the `<dt>` title in sentence case and the publisher in the
  series/channel slot (e.g. `Sonatype`).
- **List the session's videos in the `<dd>`**, one per line separated by `<br>`,
  after a short description followed by a lone `<br>`. A **live** video is linked
  by its title (`<a href="...">Title</a>`); a **dead/unavailable** video keeps
  its title as plain text with the original URL preserved in an HTML comment, so
  the reference is not lost: `Title <!-- https://www.youtube.com/watch?v=... -->`.
- **Preserve the original episode titles verbatim** in the list (only converting
  `–`/`—` to `&ndash;`/`&mdash;` and any `&` to `&amp;`) — this is a faithful
  archive of what each video was called. The session entry title still uses
  sentence case.
- **Undated archives go in a year-range section** rather than being forced into a
  single year: add one `<h2 id="YYYY-YYYY">YYYY&ndash;YYYY</h2>` block (e.g.
  `2010&ndash;2016`) in the correct descending position with a matching
  `<a href="#YYYY-YYYY">` navigation link, and place the session entries inside it
  without a per-entry date (the heading carries the era). Keep them in the source
  collection's curated order.

Check liveness before linking: a removed or private video fails a YouTube oEmbed
request (`https://www.youtube.com/oembed?url=<watch-url>&format=json`); link only
the ones that pass, and comment out the rest as above.

Because these archives leave some titles as plain (unlinked) text, the intro
carries a second `<p>` explaining that those titles are videos no longer
available online, kept as a record. Keep that note in place.

## Target file

- **Path (from repo root):** `video-log/video-log.html`
- It is a standalone fragment: a lead comment, a repo-management comment, a
  `<!-- Last updated -->` comment, an intro `<p>`, a second `<p>` noting that
  some titles are shown as plain text because those videos are no longer
  available online, a one-line "Check out specific
  years" navigation `<p>`, then one `<h2>` + `<dl>` block per year (plus, at the
  bottom, an optional year-range block such as `2010&ndash;2016` for undated
  archive collections — see "Legacy archive collections").

## Deferred work: `video-log/STATUS.md`

`video-log/STATUS.md` is a tracked, living to-do list of deferred work and next
steps for the video log (chiefly harvesting videos from each channel and series,
and sweeping the event log for standalone videos to migrate here). It is **not**
a historical log: when a task is finished, **remove it** from the file rather
than marking it done. Check it at the start of a session, keep it current, and
bump its "Last updated" date when you edit it.

## Committing changes

The video log, this skill, and `STATUS.md` live in the `simpligility-website`
git repo. Commit each completed change as its own focused commit and push it to
`main`. Fold any `STATUS.md` update into the same commit as the work it covers.

## File structure

```html
<!-- Video Log for simpligility.ca/video-log/ -->
<!-- Managed in the simpligility-website repo; edit there, then copy this into the WordPress page code view -->
<!-- Last updated: YYYY-MM-DD -->

<p>Over the years I have recorded many tutorial and educational videos ...</p>

Check out specific years:
<p><a href="#2026">2026</a>, <a href="#2025">2025</a>, ...</p>

<h2 id="2026">2026</h2>

<dl>

  <dt><strong>Video title</strong><br> Series/channel &mdash; Date</dt>
  <dd>
    Description sentence(s).
    <a href="...">Watch on YouTube</a> &bull; <a href="...">Slide deck</a>
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
- **Within a year, reverse chronological**: newest video at the top of the
  `<dl>`, oldest at the bottom.
- When adding a video, insert it at the correct position by date — do not just
  append. If the year has no `<h2>`/`<dl>` block yet, create one in the right
  spot relative to the other years.

## Entry format

Each entry is a `<dt>`/`<dd>` pair, indented two spaces, with a blank line
between entries.

### The `<dt>` (title, series/channel, and date line)

```html
  <dt><strong>Video title</strong><br> Series/channel &mdash; Date</dt>
```

- Title is wrapped in `<strong>`.
- **Title uses sentence case**: capitalise only the first word and any proper
  nouns (product, project, company, place, and personal names such as Trino,
  Maven, Java, Python, JavaScript, DevOps, Chainguard, Starburst, Sonatype,
  Kubernetes, Android, OneOps, AWS). Do **not** title-case every word. Preserve
  the established casing of proper nouns and acronyms. Use the video's real
  title; only adjust casing to fit this scheme. For a per-video entry in an
  open-ended category, the title is the **specific** video's title, not the
  category name (the category goes in the series/channel slot).
- **A colon starts a new sentence**: capitalise the first word after a `:` in a
  title.
- After the closing `</strong>`, separate the title from what follows with
  `<br> ` (a line break and a space), so the series/date drop to their own line
  under the title. Between the series/channel and the date the separator is
  ` &mdash; ` (em dash with a space on each side).
- **Series/channel** sits where the event log puts location and the write log
  puts publication. Use a clean, human name for the series the video belongs to
  or the channel it lives on: `OneOps`, `Sonatype`, `simpligility.ca`. Omit it
  only when a video genuinely belongs to no series or channel; in that case the
  date follows the title directly with ` &mdash; `. The full URL goes in the
  link below, not here.
- **Date** is the last segment. Use the most precise form known:
  - Full date: `5 June 2025` (day month year, no comma, no ordinal suffix).
  - Month only: `January 2017`.
  - Approximate: `Late 2015`, `April/May 2015`.

### The `<dd>` (description and links)

```html
  <dd>
    One or two sentences describing what the video covered.
    <a href="...">Watch on YouTube</a> &bull; <a href="...">Slide deck</a>
    <br><br>
  </dd>
```

- Content indented four spaces.
- Start with a short description: what the video was about and, when relevant,
  who it was made with or what project or audience it served.
- Public co-presenters, partners, and guests may be named; do not name customers
  or prospects, and do not name Manfred as the presenter (he presents every
  entry).
- **Links line**: one or more `<a>` links joined by ` &bull; ` (spaced bullet),
  all on a **single line** with **no leading `<br>`** — the links flow directly
  after the description. Follow the last link with `<br><br>` on its own line for
  visual separation from the next entry. Keep the whole links list on one line.

### Link labels and enforced order

The video itself always leads, since the page is a list of videos. Include only
the links that apply, in this canonical order:

1. **The video** — the canonical link to watch it. Label it `Watch on <host>`
   using the host the link points at (e.g. `Watch on YouTube`, `Watch on
   simpligility.ca`). For a one-off/finished series this is the **playlist**
   link; for a single video it is that video. This keeps the label distinct from
   the series name in the `<dt>` and tells the reader where the link goes.
2. `Slide deck` — accompanying slides, if any. Prefer a PDF self-hosted on
   simpligility.ca (`/wp-content/uploads/...`); a publicly accessible deck
   hosted elsewhere is fine. Never link a deck a visitor cannot open.
3. `Details` — a related "read more" page: a project page, a course page, a
   write-up. Use a specific label instead if there is more than one such page,
   so no two links in an entry ever share the same link text.

Do **not** add internal tracking issue links — they point at private GitHub
issues and do not belong on the public page.

## Internal links must be root-relative

The site is served under **both** `simpligility.ca` and `simpligility.com`, so
links to the site's own content must be **root-relative** — start them with `/`
and never hard-code a domain.

- Correct: `<a href="/wp-content/uploads/2016/05/slides.pdf">Slide deck</a>`
- Wrong: `<a href="https://simpligility.ca/wp-content/uploads/2016/05/slides.pdf">`
  (breaks/forces one domain when viewed on the other)

External links (YouTube, Sonatype, project sites, etc.) keep their full
`https://` URLs.

## Broken and dead links

Many entries are older videos whose related pages rot over time. The standing
rules mirror the write log:

- **Never delete an entry, and never silently strip its link, just because a URL
  no longer resolves.** The video still exists; the record stays. A dead link is
  a per-entry decision for Manfred, not a cleanup to make automatically.
- When you notice or suspect a broken link, **try to find a better URL first**:
  the current location of the page, a republished copy, or an archived snapshot
  (e.g. the Wayback Machine, `web.archive.org`). Prefer a live link; fall back to
  an archive link when that is all that survives.
- If no working URL can be found, **flag the entry for Manfred and leave it as
  is** — do not remove the link or the entry on your own.

## HTML entity conventions

Use named entities, matching the event and write logs:

- `&mdash;` — em dash separator between series/channel and date in the `<dt>`.
- `&ndash;` — en dash for ranges.
- `&bull;` — bullet separator between links.
- `&amp;` — ampersand in text (e.g. `Q&amp;A`).
- `&#39;` — apostrophe inside attribute-adjacent text where needed
  (e.g. `Trino&#39;s`).
- `<em>...</em>` — for titles quoted inside a description.

## Process for adding a new entry

1. **Decide the shape first** (see "One entry vs one entry per video"): is this a
   finished series (one entry, playlist link) or one video within an open-ended
   category (one entry per video)?
2. **Gather the facts from the source.** Watch/inspect the video or playlist and
   pull out:
   - the **title** (the video's or series' real title),
   - the **series/channel** it belongs to,
   - the **date** published (most precise form available),
   - a **one or two sentence description** of what it covered,
   - the **canonical link** (the video, or the playlist for a finished series),
     plus any slide deck or related page.

   If you cannot find a reliable link for an artifact the user mentions, **ask
   for the URL** rather than guessing — never invent a link.
3. Read `video-log/video-log.html`.
4. Determine the year and date; find the matching `<h2>`/`<dl>` block (or create
   one in the correct descending-year position — and when creating a new year,
   give its `<h2>` an `id="YYYY"` and add a matching comma-separated
   `<a href="#YYYY">` link to the navigation line).
5. Build the `<dt>`/`<dd>` pair: title in `<strong>` sentence case, series/channel
   and date in the `<dt>`, description then the links line with the video leading
   in the canonical order.
6. Insert it at the correct reverse-chronological position within the year, with
   a blank line separating it from neighbours.
7. Update the `<!-- Last updated: YYYY-MM-DD -->` comment to today's date.
8. Sanity-check: tags balanced, entities used, indentation consistent (two
   spaces for `<dt>`/`<dd>`, four for `<dd>` content).

### Worked example

A finished series — the OneOps beginner training class, released as a single
playlist on YouTube in January 2017. One entry, linking the playlist:

```html
  <dt><strong>OneOps user training: Level 1 &mdash; beginner</strong><br> OneOps &mdash; January 2017</dt>
  <dd>
    A recorded beginner training class for OneOps, the open source cloud application lifecycle management platform from Walmart, released as an open video series on the Walmart Labs Community YouTube channel.
    <a href="https://www.youtube.com/playlist?list=PLjDnb0653uBDMBpTBoLVkVtGIDO-P8e3U">Watch on YouTube</a> &bull; <a href="https://oneops.github.io/oneops-training/">Details</a>
    <br><br>
  </dd>
```

## Checklist before finishing

- [ ] The video belongs here (it is standalone, not a recording of an event or a
      companion to a post — those stay as links on their own log entries).
- [ ] The right shape was chosen: a finished series is one entry (playlist link);
      an open-ended category is one entry per video.
- [ ] Entry is in the right year block and reverse-chronological position.
- [ ] `<dt>` uses `<strong>` title, `<br> ` after the closing `</strong>`,
      ` &mdash; ` between series/channel and date, correct date form.
- [ ] Series/channel is a clean human name in the `<dt>`; the full URL is in the
      link, not the `<dt>`.
- [ ] Links use the spaced ` &bull; ` separator, the video leads with a
      `Watch on <host>` label, and no two links share the same link text.
- [ ] The links list is on a single line with no leading `<br>`, followed by
      `<br><br>` on its own line; Manfred is not named as the presenter.
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
