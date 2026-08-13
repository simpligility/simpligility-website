---
name: simpligility-event-log
description: >-
  Maintain the event log HTML fragment at event-log/event-log.html for
  simpligility.ca/event-log/. Use when adding newly discovered past events,
  adding upcoming events, or keeping the layout and formatting consistent.
---

# Event log maintenance

This skill keeps `event-log/event-log.html` consistent when adding or editing
events. It covers only what is specific to the event log.

**Read [`simpligility-site`](../simpligility-site/SKILL.md) first.** It holds
the conventions the event, write, and video logs share: the WordPress fragment
skeleton, the year navigation and its sticky counterpart, the ordering rules,
the `<dt>` and `<dd>` entry format, the root-relative link rule, the HTML entity
list, the broken-link rules, the `STATUS.md` conventions, and how to commit.
Where this file repeats something from there, that file wins.

## Target file

- **Path from the repo root:** `event-log/event-log.html`
- The `<dt>` shape is `<strong>Title</strong><br> Location &mdash; Date`, with
  the location optional.

## What belongs here

Public events: presentations, classes, workshops, panels, user meetups,
broadcasts, and conference appearances. The recording of an event stays a
`Video` link on its entry here and does **not** get a video-log entry. A
standalone video with no event behind it belongs in the video log instead.

## Deferred work: `event-log/STATUS.md`

`event-log/STATUS.md` tracks deferred work and next steps for this page, under
the STATUS conventions in the site skill.

## Sources already swept

These sources have been reviewed for past events and are complete, so treat
finding more as a watch-for-new check rather than a backlog:

- Starburst and Trino events. The Starburst blogs were swept as part of the
  write-log harvest and yielded Cinco de Trino 2022, whose recap and session
  pages are gone from starburst.io, so that entry links a Wayback copy. Manfred
  confirmed his calendar and the rest of the Starburst site hold nothing
  further.
- Sonatype event videos on YouTube. The full Nexus Live catalog and the former
  simpligility `/video/` page are captured, and both DevOpsDays Vancouver Ignite
  talks from 2013 and 2016 are in. Manfred confirmed the Sonatype event catalog
  is complete.
- The OneOps user training series and the other OneOps feature videos moved to
  the video log as standalone videos, so they are not event-log entries.

## Standing decisions

Settled calls from earlier work on the log. Follow them rather than
re-litigating them:

- **The OSCON 2015 and JavaOne 2015 decks** are served from Manfred's own forks
  with GitHub Pages enabled, `simpligility/nexus-presentations` on the gh-pages
  branch and `simpligility/javaone2015` on master, so those entries link
  `simpligility.github.io/...` rather than an upstream URL. Keep both repos: the
  original `takari/javaone2015` is gone, so the fork is the only surviving copy
  of that deck.
- **AnDevCon locations** are San Jose, CA per Manfred. The source posts did not
  state a venue, so do not "correct" these from the posts.

## The location slot

The event log puts an optional location between the title and the date:

```html
  <dt><strong>Event title</strong><br> San Diego, CA &mdash; 3 June 2026</dt>
```

- Use `City, ST` with the state abbreviation for the US, or `City, Province`
  such as `Vancouver, BC` elsewhere.
- Omit it for purely virtual or online events, so the date follows the title
  directly.

## Per-entry anchors

Most entries need no anchor, because the year navigation only targets the year
headings. Add an `id` to an individual `<dt>` only when something links to that
specific entry, such as a blog post pointing a reader at the recording and
slides for one talk. Do not add anchors pre-emptively.

```html
  <dt id="maven-safe-for-production"><strong>Is Maven safe for production?</strong><br> Minneapolis, MN &mdash; 20 May 2026</dt>
```

- Use a short, descriptive, kebab-case slug derived from the title, and keep it
  stable once anything links to it.
- The link that targets it is root-relative, as in
  `/event-log/#maven-safe-for-production`.
- **Preserve existing `id` attributes on subsequent edits.** An anchor that is
  already in place has an inbound link somewhere, so do not strip it when
  reordering, rewording, or otherwise updating the entry.

## Link labels and enforced order

Include only the links that apply, and always place them in this order, with the
recording leading:

1. `Video` — YouTube or another recording.
2. `Slide deck` — the slides for the talk. This is the single label for any
   deck; do **not** use `Presentation`, which overlaps with the `Video`
   recording of the same talk. Prefer a PDF self-hosted under
   `/wp-content/uploads/...`, though a publicly accessible deck hosted elsewhere
   is fine. Google Slides links were dropped precisely because they were not
   public.
3. `Details` — any "read more about this event" page, such as a post-event
   recap or the event's own page. **Exception:** for a **Trino Community
   Broadcast**
   episode, label the `trino.io/episodes/N` page `Detailed show notes`.
4. `Registration` or `Registration page` — the sign-up link for an upcoming
   event.

### Handling multiple supporting pages

`Details` is the default for a single "read more" page, but no two links in one
entry may share the same link text. So:

- **One** supporting page becomes `Details`:
  `Video &bull; Slide deck &bull; <a ...>Details</a>`
- **Two or more** drop the generic label and each get a short specific one, kept
  in the order above:
  `Video &bull; Slide deck &bull; <a ...>Show notes</a> &bull; <a ...>Recap</a>`

Existing entries predate this rule and may use older labels such as `Show
notes`, `Recap blog post`, or `Keynote details on event site`. Match this scheme
for new and edited entries.

## Process for adding a new entry

1. **Gather the facts from the sources.** Start from whatever the user provides,
   such as a blog post, video, event page, or slide deck, and fetch each source
   to pull out:
   - the **title** of the talk or event,
   - the **date** in the most precise form available,
   - whether it was **in person**, noting the location, or **virtual**,
   - a **one or two sentence description** of what it was and what it covered,
   - all relevant **links**: video, slide deck, the source page itself, and
     registration.

   If the user mentions an artifact such as "the video" or "the slides" without
   a URL, and you cannot find it reliably, **ask for the URL** rather than
   guessing. Never invent a link.
2. Read `event-log/event-log.html`.
3. Find the matching year block, or create one in the correct descending-year
   position with its `id` and navigation link.
4. Build the `<dt>` and `<dd>` pair: sentence-case title, location for in-person
   events only, description, then the links line in the canonical order.
5. Insert it at the correct reverse-chronological position within the year, with
   a blank line separating it from its neighbours.
6. Bump the `<!-- Last updated -->` comment.
7. Run the checklist in the site skill, plus the event-log points that follow.

### Worked example

Source: the blog post *Fork yeah: We're bringing kaniko back* on
`chainguard.dev/unchained/...`, published 5 June 2025, plus its companion video.
It is virtual, so there is no location, the source page is the single "read
more" link, and the video leads. Placed in the `2025` block between the 6 June
and 14 May entries:

```html
  <dt><strong>Fork yeah: We&#39;re bringing kaniko back</strong><br> 5 June 2025</dt>
  <dd>
    Blog post and video on Chainguard forking the kaniko container build tool after Google archived it, committing to maintain it as open source.
    <a href="https://www.youtube.com/watch?v=NPOC2n-anAU">Video</a> &bull; <a href="https://www.chainguard.dev/unchained/fork-yeah-were-bringing-kaniko-back">Details</a>
    <br><br>
  </dd>
```

## Checklist for the event log

Run the shared checklist in the site skill first, then confirm:

- [ ] Location is included for in-person events and omitted for virtual ones.
- [ ] Links follow the canonical order of Video, Slide deck, Details, and
      Registration.
- [ ] A deck uses the label `Slide deck`, never `Presentation`, and it is
      publicly accessible.
- [ ] A single "read more" page is labelled `Details`, or `Detailed show notes`
      for a Trino Community Broadcast episode.
- [ ] No separate `Speakers:` line; other names are woven into the description.
- [ ] Any existing `id` anchor on an entry is preserved, and a new one is added
      only when something links to that specific entry.
