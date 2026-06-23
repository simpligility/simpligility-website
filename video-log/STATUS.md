# Video log — work status and next steps

Working notes for building out and maintaining `video-log.html`. This captures
what has been **deferred** and the **next steps**, so the work can be resumed
later with Claude Code or any other tool. Delete items as they are completed.

Last updated: 2026-06-23

The conventions for this file are documented in
[`../skills/simpligility-video-log/SKILL.md`](../skills/simpligility-video-log/SKILL.md).
Read that first — in particular the rule for **one entry vs one entry per
video**. Much of the research overlaps with the
[event log](../event-log/STATUS.md) and the
[write log](../write-log/STATUS.md); do it with all three pages in mind so a
single pass through a source feeds them all.

The page holds the OneOps videos, the Manfred mentors episodes, and the Sonatype
video archive; much more remains to be added.

---

## 1. Keep the Manfred mentors episodes up to date

The initial 12 episodes are on the page, each as its own dated entry under the
`Manfred mentors` series (an open-ended category, not a finished series — see the
skill's "one entry vs one entry per video" rule). *Manfred mentors* is an ongoing
live show (YouTube, LinkedIn, Twitch), so add new episodes as they are published.
The episode playlist for finding them is
<https://www.youtube.com/playlist?list=PLHdo8mJLIMWALFrGgA6-wWcWgyZmjAex->.

## 2. Recover the Apache Maven Hangouts titles

The Sonatype video archive (Nexus how-to series, Central Repository publishing,
Staging Suite, the 2 Minute Challenge, Smart Proxy) has been harvested from the
former `/video/` page into the `2010&ndash;2016` section. The one section left
behind is **Apache Maven Hangouts**, which is empty on that page — no titles or
links survive. If Manfred can recover the episode titles (and any links), add
them as their own session entry following the legacy-archive convention in the
skill. Until then there is nothing to harvest for it.

## 3. Sweep the event log for other standalone videos to migrate

Go through `event-log.html` and find entries that are really standalone videos
rather than events (the OneOps training series was the first such case, now
moved here). Each is a per-entry judgment for Manfred — flag candidates and
confirm before moving. When moving one, remove it from the event log (and its
year-navigation link if it was the only entry in that year) in the same commit
that adds it here.

## 4. Track down other video channels and series

Check for standalone videos on other channels, project sites, and outlets
(e.g. older simpligility.ca screencasts, conference channel uploads that are not
event recordings, partner channels). Add any that are found.
