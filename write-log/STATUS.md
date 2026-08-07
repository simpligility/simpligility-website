# Write log — work status and next steps

Working notes for building out and maintaining `write-log.html`. This captures
what has been **deferred** and the **next steps**, so the work can be resumed
later with Claude Code or any other tool. Delete items as they are completed.

Last updated: 2026-08-07 (harvested the Starburst developer blog archive)

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

Manfred wrote a number of posts on the Sonatype blog. Harvest them from the
Sonatype site itself, now at `www.sonatype.com/blog`, including the author
archive at `www.sonatype.com/blog/author/manfred-moser`. Check for two things:
posts authored by Manfred, and posts by others that reference or mention him.
Add a write-log entry for each post he authored.

Some of what turns up will be **Nexus Live** references rather than blog posts
&mdash; Nexus Live was a Sonatype live-streamed broadcast series. Those are
events, not writing, so any newly found episode that involved Manfred goes in
the [event log](../event-log/STATUS.md) under the Nexus Live item, not here.

The hidden simpligility page once noted here was the former `/video/` page
&mdash; it holds videos, not blog posts, so there is nothing to harvest from it
for the write log.

## 3. Harvest Starburst posts

The Starburst **developer** blog archive at
<https://docs.starburst.io/blog/archive.html> is **fully harvested** &mdash; it
only ran from December 2021 to April 2023 and nothing there is missing. Nine
substantive posts were added as individual entries.

The Starburst Enterprise release and LTS backport announcements are **not** one
entry per post: they are collapsed into a **single summary entry per year**
(2021, 2022, 2023), each linking the archive page. This is a deliberate
exception to the "one entry per post" rule in the skill, because the series ran
to dozens of near-identical posts that were directed and managed rather than
individually written. Keep this shape if more of the series turns up.

Also skipped deliberately: the **We moved** post (6 April 2023), a two-line
notice that the developer blog had moved. Its content is folded into the last
sentence of the 2023 summary entry instead.

The main Starburst blog at <https://www.starburst.io/blog/> is also harvested.
The live author page at <https://www.starburst.io/blog/author/manfred-moser/>
is empty and the site search does not find the name, but the **Wayback captures
of that author page do list the posts** &mdash; eight snapshots between July 2022
and October 2024 (`web.archive.org/cdx/search/cdx?url=www.starburst.io/blog/author/manfred-moser`).
Two page templates are in play: the author's own posts sit in
`blog-recent-posts-item` blocks (pre-2023) or `blog-card cell` blocks (2023 on);
anything in `blog-single-sidebar` is unrelated site content, not his. Individual
post pages **do** still carry the byline, so each one can be confirmed directly.
That union yielded nine substantive posts (2020, 2022, 2023), all added.

Loose ends on that blog:

- Two posts have been removed and now redirect to `/blog/`: **Free Presto book
  to support the community** (14 April 2020) and **Learning SQL with the Trino
  experts from Starburst** (4 October 2023). Both entries link a Wayback
  snapshot and say so in the description.
- The `batch-processing-iceberg-delta-lake` slug once held the migrated copy of
  the Starburst Galaxy batch-processing post, but it now serves an unrelated
  2024 post by another author. No entry was added for it; the developer-blog
  original is still live and is the one linked.
- The listing caps at 12 posts with no pagination, so the 2023 window relies on
  overlapping snapshots. They overlap enough to be complete, but if a gap ever
  turns up, more snapshot timestamps are available from the CDX query above.

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
