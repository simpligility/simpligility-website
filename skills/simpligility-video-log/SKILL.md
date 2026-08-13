---
name: simpligility-video-log
description: >-
  Maintain the video log HTML fragment at video-log/video-log.html for
  simpligility.ca/video-log/. Use when adding standalone tutorial or
  educational videos and video series not tied to a specific event, or
  keeping the layout and formatting consistent.
---

# Video log maintenance

This skill keeps `video-log/video-log.html` consistent when adding or editing
entries. It covers only what is specific to the video log.

**Read [`simpligility-site`](../simpligility-site/SKILL.md) first.** It holds
the conventions the event, write, and video logs share: the WordPress fragment
skeleton, the year navigation and its sticky counterpart, the ordering rules,
the `<dt>` and `<dd>` entry format, the root-relative link rule, the HTML entity
list, the broken-link rules, the `STATUS.md` conventions, and how to commit.
Where this file repeats something from there, that file wins.

## Target file

- **Path from the repo root:** `video-log/video-log.html`
- The `<dt>` shape is
  `<strong>Title</strong><br> Series or channel &mdash; Date`.
- The intro carries a second `<p>` explaining that some titles appear as plain
  text because those videos are no longer available online. Keep that note in
  place, because the legacy archive collections leave titles unlinked.
- The bottom of the page may hold a year-range block such as
  `2010&ndash;2016` for undated archive collections.

## What belongs here

The video log is **only** for videos that exist independently of any event or
article:

- A video that is the **recording of an event**, such as a talk, a class, or a
  broadcast episode, stays a `Video` link on its **event-log** entry and does
  **not** get an entry here.
- A video that is the **companion to a post** stays a `Video` link on its
  **write-log** entry and does **not** get an entry here.
- A video that stands on its own, such as a tutorial, a how-to, an explainer, or
  a training series with no event or article behind it, **is** a video-log
  entry.

When a video could plausibly belong to an event or post, prefer linking it there
and leave it out of the video log, so the same artifact is not listed twice.

### Videos already handled, do not re-add

The simpligility.ca blog-discovery pass surfaced videos that are already in the
right place, recorded here so they are not re-proposed:

- The eight-part *Easy publishing to the Central Repository* series, linked from
  the 26 April 2016 blog post, is already a video-log entry in the 2010 to 2016
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

### Channels already swept

The known channels and playlists have been reviewed for standalone videos, so
treat finding more as a watch-for-new check rather than a backlog:

- The @ManfredMoser personal YouTube channel holds only personal and family
  clips apart from the Public service announcement already listed, so nothing
  else there belongs in the video log.
- The [AnDevCon teaser videos playlist](https://www.youtube.com/playlist?list=PLB9250394EA1B2676)
  is not wanted. The AnDevCon conference talks are already in the event log, and
  the teasers are not worth adding.
- The OneOps videos, the Sonatype video archive, and the standalone Chainguard
  demos are already captured. Chainguard Learning Labs and other webinars are
  live events and live in the event log, not here.

## One entry vs one entry per video

This is the key decision when adding videos. Two shapes:

1. **A one-off or finished series** — a set of videos produced once and
   published together, usually as a single playlist, such as the OneOps user
   training class. Add it as **one entry** linking the playlist, with the single
   date it was released.
2. **An open-ended category or brand** — a recurring title that is really an
   umbrella for separate videos accruing over time and spanning years, such as
   an ongoing show or a rolling explainer series. Add **one entry per video**,
   each with its own title, its own date, and the category name in the series
   slot. This mirrors how each Trino Community Broadcast episode is its own
   event-log entry: separate dated entries sort correctly and span year blocks.

When unsure which shape applies, ask whether the title names one finished thing
or an ongoing line of separate videos. The first is one entry, the second is one
entry per video.

**Exception, Manfred mentors.** *Manfred mentors* has exactly this open-ended
shape but is **not** listed here. The show is an ongoing live stream with its
own home at <https://simpligility.ca/manfred-mentors/>, and the video-log intro
points there instead, the same way the write log points to the blog for
self-hosted posts. Do not add its episodes.

## Legacy archive collections

Older collections, such as the Sonatype Nexus how-to series harvested from the
site's former `/video/` page, come organized per playlist or session, often with
many videos no longer available and uncertain dates. Handle these specially:

- **One entry per session or series**, following the finished-series rule, with
  the series name as the `<dt>` title in sentence case and the publisher in the
  series slot, such as `Sonatype`.
- **List the session's videos in the `<dd>`**, one per line separated by `<br>`,
  after a short description followed by a lone `<br>`. A **live** video is
  linked by its title as `<a href="...">Title</a>`. A **dead or unavailable**
  video keeps its title as plain text with the original URL preserved in an HTML
  comment, so the reference is not lost:
  `Title <!-- https://www.youtube.com/watch?v=... -->`.
- **Preserve the original episode titles verbatim** in the list, converting only
  dashes to `&ndash;` and `&mdash;` and any ampersand to `&amp;`. This is a
  faithful archive of what each video was called, while the session entry title
  still uses sentence case.
- **Undated archives go in a year-range section** rather than being forced into
  a single year. Add one `<h2 id="YYYY-YYYY">YYYY&ndash;YYYY</h2>` block such as
  `2010&ndash;2016` in the correct descending position, with a matching
  `<a href="#YYYY-YYYY">` navigation link, and place the session entries inside
  it without a per-entry date, since the heading carries the era. Keep them in
  the source collection's curated order.

## Deferred work: `video-log/STATUS.md`

`video-log/STATUS.md` tracks deferred work and next steps for this page, chiefly
harvesting videos from each channel and series and sweeping the event log for
standalone videos to migrate here, under the STATUS conventions in the site
skill.

## The series slot

The video log puts the series or channel between the title and the date:

```html
  <dt><strong>Video title</strong><br> OneOps &mdash; January 2017</dt>
```

- Use a clean human name for the series the video belongs to or the channel it
  lives on, such as `OneOps`, `Sonatype`, or `simpligility.ca`. The full URL
  belongs in the link.
- Omit it only when a video genuinely belongs to no series or channel, in which
  case the date follows the title directly.
- For a per-video entry in an open-ended category, the `<dt>` title is the
  **specific** video's title and the category name goes in this slot.

## Link labels and enforced order

The video itself always leads, since the page is a list of videos. Include only
the links that apply, in this order:

1. **The video** — the canonical link to watch it, labelled `Watch on <host>`
   using the host the link points at, such as `Watch on YouTube`. For a finished
   series this is the **playlist** link; for a single video it is that video.
   This keeps the label distinct from the series name in the `<dt>`.
2. `Slide deck` — accompanying slides. Prefer a PDF self-hosted under
   `/wp-content/uploads/...`; a publicly accessible deck hosted elsewhere is
   fine.
3. `Details` — a related "read more" page such as a project page, a course
   page, or a write-up. Use a specific label instead when there is more than
   one.

## Process for adding a new entry

1. **Decide the shape first.** Is this a finished series, so one entry with a
   playlist link, or one video within an open-ended category, so one entry per
   video?
2. **Gather the facts from the source.** Watch or inspect the video or playlist
   and pull out:
   - the **title** of the video or series,
   - the **series or channel** it belongs to,
   - the **date** published, in the most precise form available,
   - a **one or two sentence description** of what it covered,
   - the **canonical link**, the video itself or the playlist for a finished
     series, plus any slide deck or related page.

   If you cannot find a reliable link for an artifact the user mentions, **ask
   for the URL** rather than guessing. Never invent a link.
3. Read `video-log/video-log.html`.
4. Find the matching year block, or create one in the correct descending-year
   position with its `id` and navigation link.
5. Build the `<dt>` and `<dd>` pair: sentence-case title, series and date in the
   `<dt>`, description, then the links line with the video leading.
6. Insert it at the correct reverse-chronological position within the year, with
   a blank line separating it from its neighbours.
7. Bump the `<!-- Last updated -->` comment.
8. Run the checklist in the site skill, plus the video-log points that follow.

### Worked example

A finished series, the OneOps beginner training class, released as a single
playlist on YouTube in January 2017. One entry, linking the playlist:

```html
  <dt><strong>OneOps user training: Level 1 &mdash; beginner</strong><br> OneOps &mdash; January 2017</dt>
  <dd>
    A recorded beginner training class for OneOps, the open source cloud application lifecycle management platform from Walmart, released as an open video series on the Walmart Labs Community YouTube channel.
    <a href="https://www.youtube.com/playlist?list=PLjDnb0653uBDMBpTBoLVkVtGIDO-P8e3U">Watch on YouTube</a> &bull; <a href="https://oneops.github.io/oneops-training/">Details</a>
    <br><br>
  </dd>
```

## Checklist for the video log

Run the shared checklist in the site skill first, then confirm:

- [ ] The video is standalone, not the recording of an event or the companion to
      a post, since those stay as links on their own log entries.
- [ ] The right shape was chosen: a finished series is one entry with a playlist
      link, an open-ended category is one entry per video.
- [ ] Series or channel is a clean human name in the `<dt>`.
- [ ] The video leads with a `Watch on <host>` label.
- [ ] Every linked video passes the oEmbed liveness check, and dead ones are
      plain text with the URL preserved in an HTML comment.
