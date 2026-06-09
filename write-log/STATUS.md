# Write log — work status and next steps

Working notes for building out and maintaining `write-log.html`. This captures
what has been **deferred** and the **next steps**, so the work can be resumed
later with Claude Code or any other tool. Delete items as they are completed.

Last updated: 2026-06-08

The conventions for this file are documented in
[`../skills/write-log/SKILL.md`](../skills/write-log/SKILL.md). Read that first.

The page is currently scaffolding only — no posts have been added yet. Much of
the research overlaps with the [event log](../event-log/STATUS.md); do it with
both pages in mind so a single pass through a site feeds both.

---

## 1. Harvest blog posts from simpligility.ca

Go through the old blog posts on the simpligility website itself and add an
entry for each. These are the most personal/oldest posts (Maven, Android, Java,
open source) and several are referenced by event-log work as well.

## 2. Harvest Sonatype blog posts

Manfred wrote a number of posts on the Sonatype blog. There is also a hidden
page on the simpligility site that already collects many Sonatype items (noted
in the event-log STATUS) — harvest from there and from the Sonatype blog itself.

## 3. Harvest Chainguard posts

Collect Manfred's posts and articles on the Chainguard blog
(`chainguard.dev/unchained/...`) and Chainguard Academy/Education content. Some
are already referenced from the event log (e.g. the kaniko fork post) and can be
cross-linked.

## 4. Harvest Trino and Starburst posts

Collect posts on `trino.io` and the Starburst blog. The Trino Summit / Trino
Fest recap posts (see event-log STATUS) are written content and belong here too.

## 5. Track down other publications

Check for guest posts and articles on other sites and outlets (e.g. DZone,
InfoQ, devm.io, conference/community blogs, book chapters or forewords). Add any
that are found.

## 6. Fill in the stubbed Sonatype posts from the initial import

`initial-data.html` listed a few Sonatype posts with no title or link yet — one
or two more in **2016** (one tagged Feb 2016), at least one in **2015**, and a
couple untagged. Track down their titles, dates, and URLs and add entries. The
2015 year block does not exist yet; create it in descending-year position
(between 2016 and 2014) with its `<h2 id="2015">` and a matching navigation
link. Once these are recovered, `initial-data.html` can be deleted.
