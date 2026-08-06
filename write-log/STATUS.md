# Write log — work status and next steps

Working notes for building out and maintaining `write-log.html`. This captures
what has been **deferred** and the **next steps**, so the work can be resumed
later with Claude Code or any other tool. Delete items as they are completed.

Last updated: 2026-08-06 (recorded the shared sticky-nav task)

The conventions for this file are documented in
[`../skills/simpligility-write-log/SKILL.md`](../skills/simpligility-write-log/SKILL.md). Read that first.

An initial set of older posts (2011–2016) has been imported; much more remains
to be added. Much of the research overlaps with the
[event log](../event-log/STATUS.md); do it with both pages in mind so a single
pass through a site feeds both.

---

## 1. simpligility.ca blog — harvested; self-hosted posts not listed

The full simpligility.ca blog (2010–2025) is inventoried in
[`simpligility-harvest.md`](simpligility-harvest.md). **Decision (2026-07-24):**
the write log lists **external writing only**, so simpligility.ca's own
self-hosted posts are **not** added as entries — the page intro now links to the
blog for those (rule recorded in the skill under "Which posts to include"). The
harvest is kept as the reference from which the `EVENT →` items were added to the
[event log](../event-log/event-log.html), the `VIDEO →` items were routed to the
[video log](../video-log/STATUS.md), and the other-site writing it surfaced
(e.g. the SD Times Honeycomb interview) feeds item 5 below.

## 2. Harvest Sonatype blog posts

Manfred wrote a number of posts on the Sonatype blog. There is also a hidden
page on the simpligility site that already collects many Sonatype items (noted
in the event-log STATUS) — harvest from there and from the Sonatype blog itself.

## 3. Harvest Starburst posts

Collect posts on the Starburst blog.

## 4. Harvest old technology posts from mosabuam.com

Manfred has older technology-related blog posts on `mosabuam.com`. Go through
them and add an entry for each.

## 5. Track down other publications

Check for guest posts and articles on other sites and outlets (e.g. DZone,
InfoQ, devm.io, conference/community blogs, book chapters or forewords). Add any
that are found.

## 6. Fill in the stubbed Sonatype posts from the initial import

The initial import (the now-deleted `initial-data.html`) listed a few Sonatype
posts with no title or link yet — one or two more in **2016** (one tagged Feb
2016), at least one in **2015**, and a couple untagged. Track down their titles,
dates, and URLs and add entries. The 2015 year block does not exist yet; create
it in descending-year position (between 2016 and 2014) with its
`<h2 id="2015">` and a matching navigation link.

## 7. Find better URLs for the imported posts

Many imported entries point at old `blog.sonatype.com` URLs (and other early
links) that are dead or will rot over time. Go through them and, for each, try
to locate a still-working URL: the post on the site's current location, a
republished copy, or an archived snapshot (e.g. the Wayback Machine,
`web.archive.org`). Replace the link when a better one is found.

**Do not delete any entry, and do not strip its link, just because a URL no
longer resolves.** Each broken link is a per-entry decision for Manfred — flag
it and leave it in place until he decides how to proceed. See the "Broken and
dead links" rule in [`../skills/simpligility-write-log/SKILL.md`](../skills/simpligility-write-log/SKILL.md);
as more links rot over time we will likely formalize a convention for dropping
an unrecoverable link while keeping the entry (and a record of where it pointed)
on the page.

## 8. Sticky year navigation (shared feature across all three logs)

Build a floating/sticky year-navigation list into the generated HTML so it stays
visible while scrolling the live page (see <https://simpligility.ca/write-log/>),
highlights the year currently in view, and lets the reader jump to any year
without scrolling back to the top. Implement it separately for each of the three
logs (event, video, write) but design it once so the three stay consistent.
Embedding constraint: the fragment has no `<html>`/`<head>`/`<body>` wrapper (it
is pasted into a WordPress page), so any CSS/JS must live inline within the
fragment. The same item is recorded in the event-log and video-log STATUS files.
