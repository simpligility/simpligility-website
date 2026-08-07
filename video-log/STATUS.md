# Video log — work status and next steps

Working notes for building out and maintaining `video-log.html`. This captures
what has been **deferred** and the **next steps**, so the work can be resumed
later with Claude Code or any other tool. Delete items as they are completed.

Last updated: 2026-08-07 (removed the Presto SQL training task &mdash; all captured as events)

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

## 1. Sweep the event log for other standalone videos to migrate

Go through `event-log.html` and find entries that are really standalone videos
rather than events (the OneOps training series was the first such case, now
moved here). Each is a per-entry judgment for Manfred — flag candidates and
confirm before moving. When moving one, remove it from the event log (and its
year-navigation link if it was the only entry in that year) in the same commit
that adds it here.

## 2. Track down other video channels and series

Check for standalone videos on other channels, project sites, and outlets
(e.g. older simpligility.ca screencasts, conference channel uploads that are not
event recordings, partner channels). Add any that are found.

Decided against: the **AnDevCon teaser videos** playlist
(<https://www.youtube.com/playlist?list=PLB9250394EA1B2676>) is **not wanted**.
The AnDevCon conference talks are already in the event log, and these teasers are
not worth adding — do not re-propose them.

## 3. Blog-discovery videos &mdash; don't re-propose these

The simpligility.ca blog-discovery pass
([`../write-log/simpligility-harvest.md`](../write-log/simpligility-harvest.md),
`VIDEO →` notes) is done; nothing outstanding. Standing guards so these are not
re-added as video-log entries:

- The 8-part **Easy publishing to the Central Repository** series (from the
  26 Apr 2016 post) is already in the `2010–2016` section.
- **FLOSS Weekly Episode 577** (2020), the **DevOpsDays Vancouver 2016 Ignite
  talk** recording, and the **SiliconANGLE theCUBE interview** (2023) are event
  recordings and live in the [event log](../event-log/), not here.
