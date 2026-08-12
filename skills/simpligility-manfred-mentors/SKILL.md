---
name: simpligility-manfred-mentors
description: >-
  Maintain the Manfred mentors episode archive HTML fragment at
  manfred-mentors/manfred-mentors.html for simpligility.ca/manfred-mentors/.
  Use when adding new Manfred mentors episodes with a title and short summary,
  or keeping the page layout and formatting consistent.
---

# Manfred mentors page maintenance

This skill keeps `manfred-mentors/manfred-mentors.html` consistent when adding
or editing episodes. Manfred mentors is an ongoing live streaming show of
unedited, real-time work on open source projects, with a home at
<https://simpligility.ca/manfred-mentors/>.

The episodes are listed here, not in the [video log](../../video-log/). The
video log points to this page instead, the same way the write log points to the
blog for self-hosted posts. Never add Manfred mentors episodes to the video log.

The archive is published as an HTML fragment embedded in a WordPress page, so it
has **no** `<html>`, `<head>`, or `<body>` wrapper. Never add one.

## Target file

- **Path from the repo root:** `manfred-mentors/manfred-mentors.html`
- It is a standalone fragment: a lead comment, a repo-management comment, a
  `<!-- Last updated: YYYY-MM-DD -->` comment, a short intro `<p>`, then a single
  `<dl>` holding one `<dt>`/`<dd>` pair per episode, newest first.

## Page structure

The WordPress page has three parts, and only the last is maintained here:

1. The show intro, the streaming platform links for YouTube, LinkedIn, and
   Twitch, and the sponsor call-to-action. These live in WordPress.
2. The newest episode featured at the top, optionally followed by a few more
   recent episodes as embedded videos. This lives in WordPress.
3. The full episode archive at the bottom, pasted from this fragment. Every
   episode appears here as a title and a short text summary with a link to
   watch, not as an embedded video.

## Episode entry format

Each episode is a `<dt>`/`<dd>` pair, indented two spaces, with a blank line
between entries.

```html
  <dt><strong>Episode 12: Finally, Trino Gateway 17</strong><br> 1 February 2026</dt>
  <dd>
    Live work on getting the Trino Gateway 17 release out the door.
    <a href="https://www.youtube.com/watch?v=FFYYn5wwTBI">Watch on YouTube</a>
    <br><br>
  </dd>
```

- The title is wrapped in `<strong>` and starts with `Episode N:` followed by
  the episode's own title.
- **The title uses sentence case:** capitalize only the first word, the first
  word after a colon, and proper nouns such as Trino, Maven, Java, Gemini,
  Blender, and Chainguard. Preserve the established casing of proper nouns and
  acronyms. Use the episode's real title and only adjust casing to fit.
- After the closing `</strong>`, use `<br> ` and then the date. The show name is
  not repeated, because the whole page is Manfred mentors.
- **Date** is the day the episode streamed, as `1 February 2026`: day, month,
  year, with no comma and no ordinal suffix.

## Writing the summary

The summary is the point of the archive, so each episode gets one that stands on
its own.

- Write **one or two sentences** describing what the episode covered. Keep it
  concrete and factual.
- Base it on the episode itself: its title and YouTube description, and the
  video when the description is thin. Do **not** invent what happened in an
  episode.
- Do not name Manfred as the presenter, since he presents every episode. Public
  co-hosts and guests may be named; never name customers or prospects.
- Match the voice of the existing summaries: plain, direct, present the work
  rather than sell it.

If you cannot confirm an episode's title, date, or link, **ask for it** rather
than guessing. Never invent a title, a date, or a URL.

## Ordering

Newest episode first, oldest last. Insert a new episode at the top, since
episodes are numbered and released in order. Keep the numbering continuous.

## Adding a new episode

1. Gather the facts: the episode number, the title, the stream date, a one or
   two sentence summary, and the YouTube watch link.
2. Read `manfred-mentors/manfred-mentors.html`.
3. Build the `<dt>`/`<dd>` pair following the format, with the title in
   `<strong>` sentence case and the `Watch on YouTube` link after the summary.
4. Insert it at the top of the `<dl>`, above the current newest episode, with a
   blank line separating it from the next entry.
5. Update the `<!-- Last updated: YYYY-MM-DD -->` comment to today's date.
6. Sanity-check: tags balanced, entities used, indentation consistent, two
   spaces for `<dt>`/`<dd>` and four for `<dd>` content.

## Shared conventions

The Manfred mentors archive follows the same house style as the logs. See
[`../simpligility-video-log/SKILL.md`](../simpligility-video-log/SKILL.md) for
the full detail. In short:

- **HTML entities:** `&mdash;` for em dashes, `&ndash;` for en dashes and
  ranges, `&bull;` between links, `&amp;` for an ampersand in text, and
  `<em>...</em>` for a title quoted inside a summary.
- **Links:** the watch link is labeled `Watch on YouTube`. When an episode has a
  second link, join links with ` &bull; ` on one line with no leading `<br>`,
  and never repeat a link label within an entry.
- **Internal links are root-relative:** start own-site links with `/` and never
  hard-code a domain, because the site is served under both simpligility.ca and
  simpligility.com. External links keep their full `https://` URLs.
- **Dead links:** never delete an episode or silently strip a link because a URL
  stopped resolving. Look for a better or archived URL first, and otherwise flag
  it for Manfred.

## Committing changes

The archive, this skill, and `STATUS.md` live in the `simpligility-website` git
repo. Commit each completed change as its own focused commit. Fold any
`STATUS.md` update into the same commit as the work it covers.

## Checklist before finishing

- [ ] The entry belongs here: it is a Manfred mentors episode, not a video for
      the video log or a recording of another event.
- [ ] The `<dt>` uses a `<strong>` `Episode N:` title in sentence case, `<br> `
      before the date, and the correct date form.
- [ ] The summary is one or two sentences, factual, and does not name Manfred as
      the presenter.
- [ ] The `Watch on YouTube` link is present and resolves.
- [ ] The entry is at the correct newest-first position with the numbering
      continuous.
- [ ] HTML entities are used, not raw characters, and own-site links are
      root-relative.
- [ ] The `<!-- Last updated -->` date is bumped.
- [ ] No `<html>`, `<head>`, or `<body>` wrapper was introduced.
