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

**Read [`simpligility-site`](../simpligility-site/SKILL.md) first.** It holds
the conventions every page on the site shares: the Custom HTML block
requirement, page width, the root-relative link rule, the HTML entity list, the
no-duplicate-link-text and dead-link rules, the `STATUS.md` conventions, and how
to commit. This file covers only what is specific to the archive. Where it
repeats a rule from there, that file wins.

The archive differs from the three logs in one structural way: it has **no year
headings and no year navigation**, so the shared fragment skeleton, ordering,
and `<dt>` middle-slot rules in the site skill do not apply. The episode format
below replaces them.

The episodes are listed here, not in the [video log](../../video-log/). The
video log points to this page instead, the same way the write log points to the
blog for self-hosted posts. Never add Manfred mentors episodes to the video log.

## Target file

- **Path from the repo root:** `manfred-mentors/manfred-mentors.html`
- It is a standalone fragment: a lead comment, a repo-management comment, a
  `<!-- Last updated: YYYY-MM-DD -->` comment, a short intro `<p>`, then a
  single `<dl>` holding one `<dt>` and `<dd>` pair per episode, newest first.

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

Each episode is a `<dt>` and `<dd>` pair, indented two spaces, with a blank line
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
  the episode's own title, in the sentence case the site skill describes.
- After the closing `</strong>` comes `<br> ` and then the date. There is no
  middle slot, because the whole page is Manfred mentors and repeating the show
  name adds nothing.
- **Date** is the day the episode streamed, as `1 February 2026`.
- The watch link is labelled `Watch on YouTube`.

## Writing the summary

The summary is the point of the archive, so each episode gets one that stands on
its own.

- Write **one or two sentences** describing what the episode covered. Keep it
  concrete and factual.
- Base it on the episode itself: its title and YouTube description, and the
  video when the description is thin. Do **not** invent what happened in an
  episode.
- Match the voice of the existing summaries: plain and direct, presenting the
  work rather than selling it.
- The site skill's rule against naming Manfred applies here too, since he
  presents every episode. Public co-hosts and guests may be named.

If you cannot confirm an episode's title, date, or link, **ask for it** rather
than guessing. Never invent a title, a date, or a URL.

## Ordering

Newest episode first, oldest last. Insert a new episode at the top, since
episodes are numbered and released in order. Keep the numbering continuous.

## Adding a new episode

1. Gather the facts: the episode number, the title, the stream date, a one or
   two sentence summary, and the YouTube watch link.
2. Read `manfred-mentors/manfred-mentors.html`.
3. Build the `<dt>` and `<dd>` pair following the format, with the title in
   `<strong>` sentence case and the `Watch on YouTube` link after the summary.
4. Insert it at the top of the `<dl>`, above the current newest episode, with a
   blank line separating it from the next entry.
5. Bump the `<!-- Last updated -->` comment.
6. Run the checklist in the site skill, plus the episode points that follow.

## Checklist for the archive

- [ ] The entry belongs here: it is a Manfred mentors episode, not a video for
      the video log or a recording of another event.
- [ ] The `<dt>` carries an `Episode N:` title in sentence case, with `<br> `
      before the date and no middle slot.
- [ ] The summary is one or two sentences and factual.
- [ ] The `Watch on YouTube` link is present and resolves.
- [ ] The entry is at the correct newest-first position with the numbering
      continuous.
