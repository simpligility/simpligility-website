# Event log — work status and next steps

Working notes for ongoing maintenance of `event-log.html`. This captures what has
been **deferred** and the **next steps**, so the work can be resumed later with
Claude Code or any other tool. Delete items as they are completed.

Last updated: 2026-08-07 (enumerated the full Nexus Live catalog; added May 2013)

The conventions for this file are documented in
[`../skills/simpligility-event-log/SKILL.md`](../skills/simpligility-event-log/SKILL.md). Read that first.

---

## 1. Find other past Starburst and Trino public events

Track down other public events Manfred did for Starburst and Trino by checking
his calendar, the Starburst blog, and the Starburst website. Add entries for
any that are missing.

The Starburst blogs have been swept as part of the write-log harvest and
yielded one event: **Cinco de Trino 2022**, now added. Both the recap post and
the on-demand session page have been removed from starburst.io, so that entry
links a Wayback copy. What remains here is the calendar and the rest of the
Starburst website; the blogs themselves are done.

## 2. Youtube search

Do a general search on youtube for Manfred Moser and related terms to find
videos of events I have not yet added. Both DevOpsDays Vancouver Ignite talks
(2013 and 2016) are already in, so what remains is a bunch of Sonatype event
videos to track down and add as event-log entries.

The hidden simpligility page that once collected many of these was the former
`/video/` page, already harvested into the [video log](../video-log/) &mdash;
nothing left to harvest there.

The OneOps user training video series, which previously lived here, has been
moved to the [video log](../video-log/) as a standalone video series, along with
the other OneOps feature videos from the same channel.

## 3. Add the Nexus Live events

Nexus Live (originally *Nexus Office Hours*, monthly on the last Friday) was a
Sonatype live-streamed broadcast series and each episode belongs here in the
event log, not the video log. The full catalog was enumerated by scraping the
`ytInitialData` JSON from the Sonatype channel search
(<https://www.youtube.com/@Sonatypeinc>) — the playlist and channel pages are
JS-rendered, but the initial HTML payload carries the video IDs and titles.

**Added, each its own entry:** March, April, **May**, June, and September 2013,
plus the April 2014 Engineering Summit episode (Nexus 2.8). May 2013 was the most
recent addition (`wCfEbGTmJao`); its title names Manfred, so it was unambiguous.

**Pending Manfred's confirmation — did he host/appear in these?** Their titles
name only the guest, so involvement needs confirming before they are added. All
are live on the Sonatype channel:

- July 2013 with Jason van Zyl, creator of Maven &mdash; `ivUg9jZK0MA`
- October 2013 with John Nagro and Tom McLaughlin from Hubspot &mdash; `21cbI2hwQSI`
- November 2013 with Kyle Allan from Riot Games &mdash; `sLIQH8TKPas`
- December 2013 with Tyler Jewell, CEO of Codenvy &mdash; `mgTvdIAqsnk`
- March 2014 &mdash; The First 2 Minute Challenge &mdash; `HFssIdUoA4Q`
- June 2014 with Alex Honor and Damon Edwards from RunDeck &mdash; `eHaEEBEMRA8`
- July 31, 2014 &mdash; The Atlassian Story &mdash; `hkd7cCifYV4`
- October 2014 with Gene Kim and Josh Corman &mdash; `tJGdjtVLqYI`

No August 2013 or early-2014 episodes exist on the channel; this is the complete
list. Entries carry month-precision dates matching the existing Nexus Live
entries; exact broadcast dates and per-episode topics can be filled in later.

## 4. Follow-ups from the blog-discovery event additions

The events discovered in the simpligility.ca blog (2010–2024) have been added.
Loose ends:

- The **OSCON 2015** and **JavaOne 2015** decks are served from Manfred's own
  forks with GitHub Pages enabled — `simpligility/nexus-presentations` (gh-pages
  branch) and `simpligility/javaone2015` (master branch). Keep these repos; the
  entries link to `simpligility.github.io/...`. The original `takari/javaone2015`
  is gone, so the fork is the only surviving copy of that deck.
- **AnDevCon locations** are set to San Jose, CA per Manfred (the source posts did
  not state a venue).
