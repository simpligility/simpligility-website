# Video log — work status and next steps

Working notes for building out and maintaining `video-log.html`. This captures
what has been **deferred** and the **next steps**, so the work can be resumed
later with Claude Code or any other tool. Delete items as they are completed.

Last updated: 2026-08-12 (added the year-block breakup task)

The conventions for this file are documented in
[`../skills/simpligility-video-log/SKILL.md`](../skills/simpligility-video-log/SKILL.md).
Read that first — in particular the rule for **one entry vs one entry per
video**. Much of the research overlaps with the
[event log](../event-log/STATUS.md) and the
[write log](../write-log/STATUS.md); do it with all three pages in mind so a
single pass through a source feeds them all.

The page holds the OneOps videos, the Sonatype video archive, and the standalone
Chainguard and personal videos.

---

## 1. Break the year blocks up better

The page currently runs `2026`, `2025`, `2017`, and then one lumped
`2010&ndash;2016` heading. That last block holds the five aggregate Sonatype
series &mdash; *Tips from the trenches*, *Easy publishing to the Central
Repository*, *Empowering releases with the Nexus Staging Suite*, *The Nexus 2
minute challenge*, and *Nexus Professional and Smart Proxy* &mdash; none of
which carry a date, so seven years of work collapse into a single undated
heading and the year navigation is nearly useless for everything before 2017.

Date the series, then split the block into per-year headings. Each series is a
list of individual videos, so establish the span from the upload dates of its
videos on YouTube and file the series under the year it ran, or under the year
it started when it ran across several. Where a series genuinely spans years and
should not be split, keep a range heading for it rather than forcing a single
year. When the blocks change, update the `id="YYYY"` attributes, the "Check out
specific years" navigation line, and the sticky year navigation so all three
stay in step, and follow the ordering rules in the skill.

The known video channels and playlists have been swept and nothing new was
found. What was checked, and the standing "do not re-propose" guards, live in
the skill under **Channels already swept**. Beyond the year blocks there is no
harvesting backlog: add new standalone videos as they appear, following the
skill.
