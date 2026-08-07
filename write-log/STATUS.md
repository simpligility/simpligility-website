# Write log — work status and next steps

Working notes for building out and maintaining `write-log.html`. This captures
what has been **deferred** and the **next steps**, so the work can be resumed
later with Claude Code or any other tool. Delete items as they are completed.

Last updated: 2026-08-07 (checked the Takari blog &mdash; no Manfred-authored posts to add)

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

## 2. Harvest Sonatype blog posts &mdash; done for 2013&ndash;2016

The Sonatype author archive was harvested. The live site
(`www.sonatype.com/blog/author/manfred-moser`) is a JS-rendered SPA that the
tooling here cannot read, so the listing was recovered from Wayback snapshots of
the old `blog.sonatype.com/author/manfred-moser` pages (which now 301 to the
live site). Pages 1&ndash;2 (2013&ndash;2016) were captured cleanly; the only
authored post not already listed was **How-to video training: Open source
component management and intelligence** (18 July 2016), now added. Posts by
others that merely reference him (e.g. Mark Miller&#39;s *TheNexus: A community
project*) are correctly not added.

**Small remaining gap:** author-archive **page 3** (the oldest posts,
2011&ndash;2012) could not be re-fetched from Wayback (snapshots 504/absent). All
known posts from that era are already in the log (three 2012 Nexus/Insight/Maven
posts and the Nov 2011 community spotlight), so this is likely complete &mdash;
but if Manfred recalls other early Sonatype posts, add them.

Nexus Live references are handled in the [event log](../event-log/STATUS.md), not
here.

## 3. Harvest old technology posts from mosabuam.com

Manfred has older technology-related blog posts on `mosabuam.com`. Go through
them and add an entry for each.

## 4. Track down other publications

Check for guest posts and articles on other sites and outlets (e.g. DZone,
InfoQ, devm.io, conference/community blogs, book chapters or forewords). Add any
that are found.

**Takari blog &mdash; checked, nothing to add.** The Takari blog
(`takari.io/blog.html`, 2014&ndash;2015, now offline &mdash; read via Wayback)
was swept. Every post is authored by Jason van Zyl or other Takari/Maven
contributors; the string "Manfred Moser" appears in none of the ~28 posts, so
there is nothing to add here. The weekly Maven developer hangouts announced on
that blog are events, already in the [event log](../event-log/) as the two
per-year aggregate entries.

## 5. Fill in the stubbed Sonatype posts from the initial import

The initial import (the now-deleted `initial-data.html`) listed a few Sonatype
posts with no title or link yet — one or two more in **2016** (one tagged Feb
2016), at least one in **2015**, and a couple untagged. Track down their titles,
dates, and URLs and add entries. The 2015 year block does not exist yet; create
it in descending-year position (between 2016 and 2014) with its
`<h2 id="2015">` and a matching navigation link.

## 6. Find better URLs for the imported posts

**Sonatype done:** every `blog.sonatype.com` link now 301s to the same path
under `www.sonatype.com/blog`, and all 20 imported Sonatype entries were verified
live (HTTP 200) and repointed there, with the read label changed to
`Read on sonatype.com`.

What remains are the other early links: the two **TheServerSide** posts
(`theserverside.com`, 2011) and the **Hudson CI blog**
(`hudsoncentral.wordpress.com`, 2011). Go through these and, for each, try to
locate a still-working URL: the post on the site's current location, a
republished copy, or an archived snapshot (e.g. the Wayback Machine,
`web.archive.org`). Replace the link when a better one is found.

**Do not delete any entry, and do not strip its link, just because a URL no
longer resolves.** Each broken link is a per-entry decision for Manfred — flag
it and leave it in place until he decides how to proceed. See the "Broken and
dead links" rule in [`../skills/simpligility-write-log/SKILL.md`](../skills/simpligility-write-log/SKILL.md);
as more links rot over time we will likely formalize a convention for dropping
an unrecoverable link while keeping the entry (and a record of where it pointed)
on the page.
