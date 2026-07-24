# Video log — work status and next steps

Working notes for building out and maintaining `video-log.html`. This captures
what has been **deferred** and the **next steps**, so the work can be resumed
later with Claude Code or any other tool. Delete items as they are completed.

Last updated: 2026-07-24 (added simpligility.ca blog discovery, item 6)

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

## 5. Add the Presto and Trino SQL training videos

Find the Presto SQL training videos and the newer Trino SQL training videos
created with Martin, Dain, and David. Determine whether each series is a
standalone video-log entry or belongs in the event log. Add the video links,
available slide decks, and related blog posts to the appropriate log entries.

## 6. Add videos found in the simpligility.ca blog discovery

The blog discovery pass is captured in
[`../write-log/simpligility-harvest.md`](../write-log/simpligility-harvest.md)
with `VIDEO →` notes. From it, to add here:

- **Chainguard "PSA" video on joining Chainguard** — 2025 — a short fun video
  Manfred made about joining Chainguard: <https://www.youtube.com/watch?v=OA9EpeBnwrA>.
  Standalone video → add a 2025 entry.

Already present (no action): the 8-part **Easy publishing to the Central
Repository** series (linked from the 26 Apr 2016 post) is already in the
`2010–2016` section.

Cross-log items now placed in the event log (no video-log action needed):

- **FLOSS Weekly Episode 577** (Presto/Trino, 6 May 2020) — added as a 2020 event.
- **DevOpsDays Vancouver 2016 Ignite talk** recording — added as a 2016 event.
- **SiliconANGLE theCUBE interview** (2023) — already in the event log.
