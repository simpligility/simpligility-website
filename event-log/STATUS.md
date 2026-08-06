# Event log — work status and next steps

Working notes for ongoing maintenance of `event-log.html`. This captures what has
been **deferred** and the **next steps**, so the work can be resumed later with
Claude Code or any other tool. Delete items as they are completed.

Last updated: 2026-08-06 (recorded the shared sticky-nav task)

The conventions for this file are documented in
[`../skills/simpligility-event-log/SKILL.md`](../skills/simpligility-event-log/SKILL.md). Read that first.

---

## 1. Add the DevOpsCon keynote video once cleared

The "Is DevOps doomed?" entry (DevOpsCon San Diego, 3 June 2026) has no `Video`
link yet. Manfred is working with the organizers to obtain a recording and
permission to use it. For now the entry notes that the video is available to
devm.io members. Once a usable recording and permission are in hand, add it as
the first link (`Video`, ahead of the `Slide deck`).

## 2. Find other past Starburst and Trino public events

Track down other public events Manfred did for Starburst and Trino by checking
his calendar, the Starburst blog, and the Starburst website. Add entries for
any that are missing.

## 3. Youtube search

Do a general search on youtube for Manfred Moser and related terms to find
videos of events I have not yet added. There should be a devopsdays Vancouver
one and a bunch of Sonatype ones. For the Sonatype ones there is also a hidden
page on the simpligility site that has a lot of these already. We could harvest
these and move them over.

The OneOps user training video series, which previously lived here, has been
moved to the [video log](../video-log/) as a standalone video series, along with
the other OneOps feature videos from the same channel.

## 4. Add the Nexus Live events

The former `/video/` page had a **Nexus Live** section — these were live
streamed events and belong here in the event log, not the video log. There is a
playlist at
<https://www.youtube.com/playlist?list=PLGB2s-U5FSWPHJd4EEEFgmcLJUc-_1Pcs>;
Manfred to dig out the individual events (title, date, video link) so each can be
added as its own event-log entry.

## 5. Follow-ups from the blog-discovery event additions

The events discovered in the simpligility.ca blog (2010–2024) have been added.
Loose ends:

- The **OSCON 2015** and **JavaOne 2015** decks are served from Manfred's own
  forks with GitHub Pages enabled — `simpligility/nexus-presentations` (gh-pages
  branch) and `simpligility/javaone2015` (master branch). Keep these repos; the
  entries link to `simpligility.github.io/...`. The original `takari/javaone2015`
  is gone, so the fork is the only surviving copy of that deck.
- **AnDevCon locations** are set to San Jose, CA per Manfred (the source posts did
  not state a venue).

## 6. Sticky year navigation (shared feature across all three logs)

Build a floating/sticky year-navigation list into the generated HTML so it stays
visible while scrolling the live page (see <https://simpligility.ca/event-log/>),
highlights the year currently in view, and lets the reader jump to any year
without scrolling back to the top. Implement it separately for each of the three
logs (event, video, write) but design it once so the three stay consistent.
Embedding constraint: the fragment has no `<html>`/`<head>`/`<body>` wrapper (it
is pasted into a WordPress page), so any CSS/JS must live inline within the
fragment. The same item is recorded in the video-log and write-log STATUS files.
