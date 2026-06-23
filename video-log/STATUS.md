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

The page holds the OneOps training series and OneOps feature videos; much more
remains to be added.

---

## 1. Harvest the Manfred mentors videos

*Manfred mentors* is an open-ended category, not a finished series, so each
video gets **its own dated entry** with `Manfred mentors` in the series/channel
slot (see the skill's "one entry vs one entry per video" rule). Find every video
in the series, with its title, date, and link, and add an entry for each.

## 2. Harvest older Sonatype videos

Manfred recorded a number of standalone how-to and explainer videos for Sonatype
(Maven, Nexus, security, and related topics). Track them down and add an entry
for each, with `Sonatype` in the series/channel slot. A video that is a
recording of a Sonatype *talk* or a *companion to a Sonatype post* stays a link
on its event-log/write-log entry instead — only standalone videos belong here.

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
