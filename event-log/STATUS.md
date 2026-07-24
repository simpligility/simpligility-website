# Event log — work status and next steps

Working notes for ongoing maintenance of `event-log.html`. This captures what has
been **deferred** and the **next steps**, so the work can be resumed later with
Claude Code or any other tool. Delete items as they are completed.

Last updated: 2026-07-24 (added the simpligility.ca blog-discovery events)

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

## 5. Add the AnDevCon teaser videos

The AnDevCon conference talks and fireside chats (AnDevCon 2011, AnDevCon II
2011, AnDevCon III 2012, AnDevCon 5 2013) have been added to the event log from
the simpligility.ca blog discovery. What remains is the AnDevCon **teaser
videos** playlist
(<https://www.youtube.com/playlist?list=PLB9250394EA1B2676>) — likely video-log
material rather than events. Evaluate and add there if worthwhile.

## 6. Add the Learning Lab video and recap once live

The Learning Lab entry (23 July 2026, "Learning Lab: Chainguard Libraries for
Java — CVE remediation, fallback, and policies") currently has only its slide
deck. Once they go live, add:

- the `Video` link (YouTube), as the first link ahead of the slide deck, and
- a `Details` link to the recap at
  <https://edu.chainguard.dev/software-security/learning-labs/ll202607/>.

## 7. Follow-ups from the blog-discovery event additions

The events discovered in the simpligility.ca blog (2010–2024) have been added.
Loose ends:

- **DevOpsDays Vancouver 2016** links only the `Video`. A published Google Slides
  deck exists
  (`docs.google.com/presentation/d/12o1JhRxBaNTP5HLFz7M6YuxZwZNd0nZYmRqYM36bEFI/pub`);
  add it as a `Slide deck` if it should be public.
- The **OSCON 2015** and **JavaOne 2015** decks are served from Manfred's own
  forks with GitHub Pages enabled — `simpligility/nexus-presentations` (gh-pages
  branch) and `simpligility/javaone2015` (master branch). Keep these repos; the
  entries link to `simpligility.github.io/...`. The original `takari/javaone2015`
  is gone, so the fork is the only surviving copy of that deck.
- **AnDevCon locations** are set to San Jose, CA per Manfred; the source posts did
  not state a venue, so confirm if a more precise venue/city is wanted.
