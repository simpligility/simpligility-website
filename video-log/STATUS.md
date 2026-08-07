# Video log — work status and next steps

Working notes for building out and maintaining `video-log.html`. This captures
what has been **deferred** and the **next steps**, so the work can be resumed
later with Claude Code or any other tool. Delete items as they are completed.

Last updated: 2026-08-07 (Maven developer hangouts resolved and routed to the event log)

The conventions for this file are documented in
[`../skills/simpligility-video-log/SKILL.md`](../skills/simpligility-video-log/SKILL.md).
Read that first — in particular the rule for **one entry vs one entry per
video**. Much of the research overlaps with the
[event log](../event-log/STATUS.md) and the
[write log](../write-log/STATUS.md); do it with all three pages in mind so a
single pass through a source feeds them all.

The page holds the OneOps videos, the Sonatype video archive, and assorted
standalone videos; much more remains to be added.

---

## 1. Apache Maven developer hangouts &mdash; moved to the event log

Resolved. These turned out to be the weekly Takari **Maven developer hangouts**
(Google+ Hangouts on Air, ~September 2014 to April 2015) that Manfred organized
and co-hosted with Jason van Zyl and the Maven community. Since they are
recordings of live events he hosted &mdash; not standalone tutorials &mdash; the
video-log rule sends them to the [event log](../event-log/), where they now live
as two per-year aggregate entries (2014 and 2015) linking the archived
`takari.io/events.html` page. All recordings are offline, so there are no video
links. Nothing left to do here.

## 2. Sweep the event log for other standalone videos to migrate

Go through `event-log.html` and find entries that are really standalone videos
rather than events (the OneOps training series was the first such case, now
moved here). Each is a per-entry judgment for Manfred — flag candidates and
confirm before moving. When moving one, remove it from the event log (and its
year-navigation link if it was the only entry in that year) in the same commit
that adds it here.

## 3. Track down other video channels and series

Check for standalone videos on other channels, project sites, and outlets
(e.g. older simpligility.ca screencasts, conference channel uploads that are not
event recordings, partner channels). Add any that are found.

Decided against: the **AnDevCon teaser videos** playlist
(<https://www.youtube.com/playlist?list=PLB9250394EA1B2676>) is **not wanted**.
The AnDevCon conference talks are already in the event log, and these teasers are
not worth adding — do not re-propose them.

## 4. Add the Presto SQL training videos

The **Trino** SQL training series (2023, *Learning SQL with Trino from the
experts* &mdash; four sessions with Martin Traverso, Dain Sundstrom, and David
Phillips) has been handled: the sessions were live webinars, so each is an
**event-log** entry with its recording, and each also has its **write-log**
announcement post. They are **not** video-log entries.

Still to do: find the older **Presto** SQL training videos and decide, the same
way, whether each is a standalone video-log entry or a live event for the event
log. Add the video links, available slide decks, and related blog posts to the
appropriate log.

## 5. Add videos found in the simpligility.ca blog discovery

The blog discovery pass is captured in
[`../write-log/simpligility-harvest.md`](../write-log/simpligility-harvest.md)
with `VIDEO →` notes. Nothing outstanding to add here from it.

Already present (no action): the 8-part **Easy publishing to the Central
Repository** series (linked from the 26 Apr 2016 post) is already in the
`2010–2016` section.

Cross-log items now placed in the event log (no video-log action needed):

- **FLOSS Weekly Episode 577** (Presto/Trino, 6 May 2020) — added as a 2020 event.
- **DevOpsDays Vancouver 2016 Ignite talk** recording — added as a 2016 event.
- **SiliconANGLE theCUBE interview** (2023) — already in the event log.
