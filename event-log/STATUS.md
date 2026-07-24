# Event log — work status and next steps

Working notes for ongoing maintenance of `event-log.html`. This captures what has
been **deferred** and the **next steps**, so the work can be resumed later with
Claude Code or any other tool. Delete items as they are completed.

Last updated: 2026-07-24 (added simpligility.ca blog discovery, item 3)

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

## 3. Add older conferences discovered in the simpligility.ca blog

A full discovery pass over the simpligility.ca blog (2010–2025) is captured in
[`../write-log/simpligility-harvest.md`](../write-log/simpligility-harvest.md),
which carries `EVENT →` notes with dates, locations, and slide/video links. The
events below were found there and are **not yet in the event log**. Add each
(oldest-first within its year), pulling the slide-deck PDFs onto the site and
linking them root-relative per the skill. Verify details against the source post
before adding.

Talks and appearances (Manfred presenting/hosting) — highest priority:

- **VIJUG intro to Android** — Victoria BC — April 2010 (announcement only; confirm it happened).
- **Maven and Android** — Vancouver Android Developers — Vancouver — April 2010. Slides `maven_android_intro.pdf`.
- **Maven and Android** — GTUG Barcelona — Barcelona, Spain — 10 September 2010. Slides `maven_android_intro_gtug_barcelona.pdf`.
- **Maven and Android hands-on lab** — AndroidTO — Toronto — October 2010 (~200 attendees). Slides `maven_android_intro_androidto.pdf`.
- **Android: Explained by Numbers** — APEG BC — Victoria BC — November 2010.
- **AnDevCon 2011** — San Francisco — March 2011. Sessions "Using Apache Maven for Android development" (306) and "Testing Android applications" (406); hosted two fireside chats. Slides `maven_android_intro_andevcon.pdf`, `maven_android_test_andevcon.pdf`.
- **Android Development Introduction** — VIJUG — Vancouver Island — April 2011. Slides `android_dev_intro.pdf`.
- **Android Open Source Development Tools** — OSCON Java 2011 — Portland — July 2011. Slides `oscon2011-android-os-tools.pdf`.
- **AnDevCon II** — November 2011. "Apache Maven for Android" (slides `android_maven_intro_andevcon2.pdf`) + a 4-hour "Testing Android Applications" workshop (6 Nov); hosted two fireside chats.
- **AnDevCon III** — May 2012. Workshop "Apache Maven for Android Development Pros and Teams" (slides + materials ZIP); lightning talk "Android Open Source – so what?" (16 May, slides `open_source_cooperation_lightning_talk.pdf`); "Tricks of the Trade" fireside chat (16 May).
- **Git/GitHub full-day workshop with Matthew McCullough** — Victoria BC — 29 August 2012 (co-organized by VIJUG + GDG Victoria).
- **GDG Victoria BC launch** — Victoria BC — June 2012 (user-group founding).
- **JavaOne 2012** — San Francisco — October 2012 (Sonatype booth support; the Jenkins User Conference SF talk that week is already logged).
- **AnDevCon 5 fireside chat "Android Development Growing Up"** — Boston — 2013 (date in post ambiguous; verify).
- **OSCON 2015** — Portland — July 2015 — "Getting your ducks in a row – an introduction to managing components in your software supply chain". Slides at `sonatype.github.io/nexus-presentations/component-software-supply-chain.html`.
- **JavaOne 2015** — October 2015 — "Still Rocking it Maven" with Jason van Zyl. Slides at `takari.github.io/javaone2015`.
- **DevOpsDays Vancouver 2016** — Vancouver — April 2016 — Ignite talk. Video <https://www.youtube.com/watch?v=M2mnDiWJhOY> (at 3h17m17s); Google Slides deck. (Distinct from the 2013 DevOpsDays entry already logged.)
- **FLOSS Weekly Episode 577** — 6 May 2020 — Presto/Trino with Dain Sundstrom. Video <https://twit.tv/shows/floss-weekly/episodes/577>. (Appearance; could go here or in the video log.)
- **Data Engineer Things meetup "Big Data Whirlwind Tour"** — Bellevue WA — early April 2024 — Trino talk (~100+ attendees).

Attended (not presenting) — decide per-entry whether these belong in the log:

- Sonatype Maven training MVN 101/201 (June 2010, as student); Eric Ries lean-startup talk (Victoria, early 2011); Google I/O 2012 (San Francisco); Community Leadership Summit + Devoxx4Kids (Portland, July 2015); Open Source Summit NA 2024 (Seattle, April 2024); Google I/O 2024 (Mountain View, May 2024).

## 4. Youtube search

Do a general search on youtube for Manfred Moser and related terms to find
videos of events I have not yet added. There should be a devopsdays Vancouver
one and a bunch of Sonatype ones. For the Sonatype ones there is also a hidden
page on the simpligility site that has a lot of these already. We could harvest
these and move them over.

The OneOps user training video series, which previously lived here, has been
moved to the [video log](../video-log/) as a standalone video series, along with
the other OneOps feature videos from the same channel.

## 5. Add the Nexus Live events

The former `/video/` page had a **Nexus Live** section — these were live
streamed events and belong here in the event log, not the video log. There is a
playlist at
<https://www.youtube.com/playlist?list=PLGB2s-U5FSWPHJd4EEEFgmcLJUc-_1Pcs>;
Manfred to dig out the individual events (title, date, video link) so each can be
added as its own event-log entry.

## 6. Add AnDevCon

Linked to these teaser videos maybe -
https://www.youtube.com/playlist?list=PLB9250394EA1B2676, but also find other
details, look in my calendar, the simpligility website (blog posts?) and also I
think there are slides on the simpligility github org

## 7. Add the Learning Lab video and recap once live

The Learning Lab entry (23 July 2026, "Learning Lab: Chainguard Libraries for
Java — CVE remediation, fallback, and policies") currently has only its slide
deck. Once they go live, add:

- the `Video` link (YouTube), as the first link ahead of the slide deck, and
- a `Details` link to the recap at
  <https://edu.chainguard.dev/software-security/learning-labs/ll202607/>.