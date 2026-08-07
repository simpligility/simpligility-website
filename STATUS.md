# Site — work status and next steps

Repo-wide and cross-cutting tasks for the simpligility.ca content managed in this
repo. Work that belongs to a single log lives in that log's own STATUS file:
[`event-log/STATUS.md`](event-log/STATUS.md),
[`video-log/STATUS.md`](video-log/STATUS.md), and
[`write-log/STATUS.md`](write-log/STATUS.md). This file is for work that spans
more than one of them, or the site as a whole. It is a living to-do list, not a
historical log: when a task is finished, **remove it** rather than marking it
done, and bump the "Last updated" date when you edit it.

Last updated: 2026-08-07 (added the About-page log-linking task)

---

## 1. Build out the Manfred mentors page

The *Manfred mentors* show has a dedicated page at
<https://simpligility.ca/manfred-mentors/>, currently a promo landing page
(intro, streaming-platform links, sponsor call-to-action) with no episode list.
The video log no longer lists the episodes and points here instead; that rule
is recorded in
[`skills/simpligility-video-log/SKILL.md`](skills/simpligility-video-log/SKILL.md).

Next: expand the WordPress page into a proper episode archive &mdash; a
blog-style, reverse-chronological list of episodes with titles, dates, and watch
links. Consider managing it here as its own HTML fragment, like the three logs
(with a matching skill and STATUS file), so it can be generated and kept
consistent. The episode playlist for reference is
<https://www.youtube.com/playlist?list=PLHdo8mJLIMWALFrGgA6-wWcWgyZmjAex->.

## 2. Establish a regular Manfred mentors cadence

Set a regular, predictable streaming cadence for *Manfred mentors* &mdash; for
example a fixed weekly or biweekly day and time &mdash; and commit to it rather
than streaming ad hoc. Decide the interval, announce the schedule on the
dedicated page and the streaming platforms (YouTube, LinkedIn, Twitch), and then
run with it consistently.

## 3. Link the log pages better from the About pages

The event, write, and video logs
(<https://simpligility.ca/event-log/>, <https://simpligility.ca/write-log/>,
<https://simpligility.ca/video-log/>) are not well surfaced from the site's
About page(s). Add clear links to all three logs there so visitors reading
Manfred's background can find his talks, writing, and videos. Keep the links
root-relative (`/event-log/`, `/write-log/`, `/video-log/`) so they work under
both simpligility.ca and simpligility.com. The About pages are WordPress pages,
not managed in this repo, so the edit is made in the WordPress admin.

The write-log-specific facet of this &mdash; linking the write log from the
books section of the About page &mdash; is tracked in
[`write-log/STATUS.md`](write-log/STATUS.md).
