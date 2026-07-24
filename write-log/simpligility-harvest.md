# simpligility.ca blog harvest — discovery inventory

Discovery pass over every post on the simpligility.ca blog, paged from the
oldest index (`/page/30/`, 2010) to the newest (`/page/1/`, 2025). This is the
**master record** for turning the self-hosted blog into write-log entries, and
it also feeds the [event log](../event-log/STATUS.md) and
[video log](../video-log/STATUS.md) — a single post often names a talk or a
video. It is a working data file, not the published page.

Harvested: 2026-07-24. Source: https://simpligility.ca/page/N/ (N = 30 → 1).

## How to read this

- Every post below is a piece of writing by Manfred, so each is a **write-log
  candidate**. Posts that also describe a talk/appearance carry an
  **`EVENT →`** note; posts that announce/contain a video carry a **`VIDEO →`**
  note. Those notes are extracted into the event- and video-log STATUS files.
- Slide-deck URLs in the old post bodies use the legacy `www.simpligility.com`
  domain; on the current site those live under `/wp-content/uploads/...` and
  links must be made **root-relative** per the log skills.

## Scope decisions (resolved 2026-07-24)

1. **Twitter Weekly Updates digests — excluded.** From late 2010 through 2012 the
   blog auto-published ~60 "Twitter Weekly Updates for YYYY-MM-DD" posts (weekly
   tweet roundups). They are auto-generated, not authored articles, so they are
   **not** write-log entries and are not enumerated below (recoverable by paging
   the blog if ever wanted).
2. **Release-only posts — one entry each.** Every substantive post, including
   short version-announcement posts (e.g. "Android Maven Plugin 4.4.2 Released"),
   gets its own entry; do not consolidate per project.
3. **Duplicate posts — dedupe.** Several posts have duplicate slug pairs (`.../`
   and `.../…-2/`) from a WordPress double-publish; add each once, using the
   canonical (non-`-2`) URL.

These rules are recorded in the write-log skill under "Which posts to include".

**Resolved (2026-07-24):** the write log lists **external writing only**, so the
self-hosted simpligility.ca posts below are **not** added as entries — the
write-log intro links to the blog for those. This harvest stays as the reference
for the `EVENT →`, `VIDEO →`, and other-site items already routed out of it.

---

## 2010

- **Launching early** — 11 Jan 2010 — <https://simpligility.ca/2010/01/launching-early/> — Announces the launch of the simpligility technologies site, following agile "launch early" principles.
- **Maven Android SDK Deployer adds SDK 2.1 support** — 13 Jan 2010 — <https://simpligility.ca/2010/01/maven-android-sdk-deployer-adds-sdk-2-1-support/>
- **How to mavenize a typical web application build: JasperServer 3.7 sample webapp** — 25 Jan 2010 — <https://simpligility.ca/2010/01/how-to-mavenize-a-typical-web-application-build-jasperserver-3-7-sample-webapp/>
- **Documenting Android Development with Apache Maven** — 2 Feb 2010 — <https://simpligility.ca/2010/02/documenting-android-development-with-apache-maven/>
- **Improving the mavenized JasperServer 3.7 sample webapp build** — 3 Feb 2010 — <https://simpligility.ca/2010/02/improving-the-mavenized-jasperserver-3-7-sample-webapp-build/>
- **How to contribute to the Maven books** — 22 Feb 2010 — <https://simpligility.ca/2010/02/how-to-contribute-to-the-maven-books/> — On contributing to the Maven reference books, specifically the Android chapter.
- **Presenting an introduction to Android** — 7 Apr 2010 — <https://simpligility.ca/2010/04/presenting-an-introduction-to-android/> — `EVENT →` Vancouver Island Java User Group (VIJUG), Victoria BC, April 2010 (announcement).
- **Learn about Android Development with Maven in Vancouver** — 20 Apr 2010 — <https://simpligility.ca/2010/04/learn-about-android-development-with-maven-in-vancouver/> — `EVENT →` Vancouver Android Developers meetup, Vancouver, April 2010 (announcement).
- **Recap Presentation about Maven and Android** — 30 Apr 2010 — <https://simpligility.ca/2010/04/recap-presentation-about-maven-and-android/> — `EVENT →` Vancouver Android Developers, Vancouver, April 2010. Slides: `maven_android_intro.pdf`.
- **Attribute support for KSOAP2 on Android** — 25 May 2010 — <https://simpligility.ca/2010/05/attribute-support-for-ksoap2-on-android/>
- **Automatically starting the emulator in your Android build** — 31 May 2010 — <https://simpligility.ca/2010/05/automatically-starting-the-emulator-in-your-android-build/>
- **Android Artifacts hit Maven Central** — 19 June 2010 — <https://simpligility.ca/2010/06/android-artifacts-hit-maven-central/>
- **Maven Android Plugin with zipalign and improved verification** — 27 June 2010 — <https://simpligility.ca/2010/06/maven-android-plugin-with-zipalign-and-improved-verification/>
- **Impressions from the first day of MVN 201** — 28 June 2010 — <https://simpligility.ca/2010/06/impressions-from-the-first-day-of-mvn-201/> — `EVENT →` Sonatype MVN 201 Maven training, June 2010 (attended as student, not presented).
- **Sonatype Maven Training – MVN 201 continued** — 28 June 2010 — <https://simpligility.ca/2010/06/sonatype-maven-training-mvn-201-continued/> — `EVENT →` same training (attended).
- **Multi Module Android project in Eclipse** — 8 July 2010 — <https://simpligility.ca/2010/07/multi-module-android-project-in-eclipse/>
- **Solidifying my Maven foundation** — 20 July 2010 — <https://simpligility.ca/2010/07/solidifying-my-maven-foundation/> — `EVENT →` Sonatype Maven training MVN 101/201 (attended).
- **Sign, zipalign and to market, to market with Maven** — 31 July 2010 — <https://simpligility.ca/2010/07/sign-zipalign-and-to-market-to-market-with-maven/>
- **Referential integrity with sqlite on Android the lazy way** — 20 Aug 2010 — <https://simpligility.ca/2010/08/referential-integrity-with-sqlite-on-android-the-lazy-way/>
- **Maven and Android in Barcelona** — 30 Aug 2010 — <https://simpligility.ca/2010/08/maven-and-android-in-barcelona/> — `EVENT →` GTUG Barcelona, Barcelona Spain, 10 September 2010. Slides: `maven_android_intro_gtug_barcelona.pdf`.
- **Hands on lab about Maven and Android development at AndroidTO** — 13 Oct 2010 — <https://simpligility.ca/2010/10/hands-on-lab-about-maven-and-android-development-at-androidto/> — `EVENT →` AndroidTO, Toronto, October 2010 (hands-on lab, ~200 attendees). Slides: `maven_android_intro_androidto.pdf`.
- **Reviving ksoap2 for Android** — 15 Oct 2010 — <https://simpligility.ca/2010/10/reviving-ksoap2-for-android/>
- **Growth** — 28 Oct 2010 — <https://simpligility.ca/2010/10/growth/> — Personal reflection; `EVENT →` mentions AndroidTO Toronto, October 2010.
- **Release version management for your Android application** — 12 Nov 2010 — <https://simpligility.ca/2010/11/release-version-management-for-your-android-application/>
- **Presenting introduction to Android** — 17 Nov 2010 — <https://simpligility.ca/2010/11/presenting-introduction-to-android/> — `EVENT →` Association of Professional Engineers and Geoscientists of BC (APEG BC), Victoria BC, November 2010. Talk "Android: Explained by Numbers" (slides referenced).
- **Apache Maven, Android and Testing at AnDevCon** — 6 Dec 2010 — <https://simpligility.ca/2010/12/apache-maven-android-and-testing-at-andevcon/> — `EVENT →` AnDevCon 2011 (announcement of two sessions + BOF).
- **Gingerbread support for the Maven Android SDK Deployer** — 6 Dec 2010 — <https://simpligility.ca/2010/12/gingerbread-support-for-the-maven-android-sdk-deployer/>
- **Proguard for Android with Maven without shooting yourself in the foot** — 11 Dec 2010 — <https://simpligility.ca/2010/12/proguard-for-android-with-maven-without-shooting-yourself-in-the-foot/>
- **Hints for using Proguard on your Android app** — 17 Dec 2010 — <https://simpligility.ca/2010/12/hints-for-using-proguard-on-your-android-app/>

## 2011

- **Android StrictMode for all platform versions** — 6 Jan 2011 — <https://simpligility.ca/2011/01/android-strictmode-for-all-platform-versions/>
- **Fireside chats at AnDevCon 2011** — 12 Jan 2011 — <https://simpligility.ca/2011/01/fireside-chats-at-andevcon/> — `EVENT →` AnDevCon 2011, San Francisco, March 2011. Hosts fireside chats (Android Community Leaders; Android Development Tooling); his sessions 306 "Using Apache Maven for Android development" and 406 "Testing Android applications".
- **More Guice for Android and Maven central** — 23 Jan 2011 — <https://simpligility.ca/2011/01/more-guice-for-android-and-maven-central/>
- **Honeycomb for the Maven Android SDK Deployer** — 26 Jan 2011 — <https://simpligility.ca/2011/01/honeycomb-for-the-maven-android-sdk-deployer/>
- **NFC and Android 2.3.3 for Maven Android SDK Deployer** — 9 Feb 2011 — <https://simpligility.ca/2011/02/nfc-and-android-2-3-3-for-maven-android-sdk-deployer/>
- **While it is snowing like mad outside** — 23 Feb 2011 — <https://simpligility.ca/2011/02/while-it-is-snowing-like-mad-outside/> — Maven Android SDK Deployer gains Android 3.0.
- **Time for some fireside chats at AnDevCon 2011** — 25 Feb 2011 — <https://simpligility.ca/2011/02/time-for-some-fireside-chats-at-andevcon-2011/> — `EVENT →` AnDevCon 2011.
- **Lean in Victoria** — 1 Mar 2011 — <https://simpligility.ca/2011/03/lean-in-victoria/> — `EVENT →` Eric Ries lean-startup talk, Victoria, early 2011 (attended).
- **About delicious honeycomb** — 4 Mar 2011 — <https://simpligility.ca/2011/03/about-delicious-honeycomb/> — `WRITING (other site) →` links an SD Times interview about Honeycomb development.
- **Fragments for all Maven users** — 4 Mar 2011 — <https://simpligility.ca/2011/03/fragments-for-all-maven-users/>
- **Presentation files for AnDevCon** — 8 Mar 2011 — <https://simpligility.ca/2011/03/presentation-files-for-andevcon/> — `EVENT →` AnDevCon 2011 slides: `maven_android_intro_andevcon.pdf`, `maven_android_test_andevcon.pdf`.
- **AnDevCon 2011 in hindsight – Part 1** — 11 Mar 2011 — <https://simpligility.ca/2011/03/andevcon-2011-in-hindsight-part-1/> — `EVENT →` AnDevCon 2011 recap.
- **AnDevCon 2011 in hindsight – Part 2** — 12 Mar 2011 — <https://simpligility.ca/2011/03/andevcon-2011-in-hindsight-part-2/> — `EVENT →` AnDevCon 2011 recap (Maven talk ~30, testing/CI talk ~150 attendees).
- **Android Development Introduction at VIJUG** — 29 Apr 2011 — <https://simpligility.ca/2011/04/android-development-introduction-at-vijug/> — `EVENT →` VIJUG, Vancouver Island, April 2011 (~20 attendees). Slides: `android_dev_intro.pdf`.
- **Hudson – Book, Changes and Community** — 13 June 2011 — <https://simpligility.ca/2011/06/hudson-book-changes-and-community/> — Announces the Hudson book project opportunity.
- **OSCON for coffee and robots** — 20 June 2011 — <https://simpligility.ca/2011/06/oscon-for-coffee-and-robots/> — `EVENT →` OSCON Java 2011 (announcement).
- **AnDevCon feedback and outlook** — 8 June 2011 — <https://simpligility.ca/2011/06/andevcon-feedback-and-outlook/> — `EVENT →` AnDevCon 1 feedback; announces AnDevCon 2 testing workshop.
- **Android Open Source Development Tools at OSCON 2011** — 26 July 2011 — <https://simpligility.ca/2011/07/android-open-source-development-tools-at-oscon-2011/> — `EVENT →` OSCON Java 2011, Portland, July 2011 (~30 attendees). Slides: `oscon2011-android-os-tools.pdf` (+ short version).
- **Easier Android test reporting with Maven and Hudson** — 2 Sep 2011 — <https://simpligility.ca/2011/09/easier-android-test-reporting-with-maven-and-hudson/>
- **Git and github training** — 13 Sep 2011 — <https://simpligility.ca/2011/09/git-and-github-training/> — `EVENT →` Git/GitHub training (attended).
- **Fireside Chats at AnDevCon II** — 17 Sep 2011 — <https://simpligility.ca/2011/09/fireside-chats-at-andevcon-ii/> — `EVENT →` AnDevCon II (two fireside chats: app publishing; Android tablet dev).
- **Android Maven Documentation Update** — 27 Oct 2011 — <https://simpligility.ca/2011/10/android-maven-documentation-update/>
- **Hudson, CI and more interviews** — 2 Nov 2011 — <https://simpligility.ca/2011/11/hudson-ci-and-more-interviews/> — `WRITING (other site) →` two TheServerSide interviews (already in write log). `EVENT →` prepared a JavaOne 2011 talk with Tim (did not attend in person).
- **New Android Maven Samples** — 3 Nov 2011 — <https://simpligility.ca/2011/11/new-android-maven-samples/>
- **Testing Android Applications – Going from Zero to Hero** — 6 Nov 2011 — <https://simpligility.ca/2011/11/testing-android-applications-going-from-zero-to-hero/> — `EVENT →` AnDevCon II 4-hour testing workshop, 6 Nov 2011 (slides referenced).
- **Apache Maven at AnDevCon II** — 7 Nov 2011 — <https://simpligility.ca/2011/11/apache-maven-at-andevcon-ii/> — `EVENT →` AnDevCon II, Nov 2011 (~40 attendees). Slides: `android_maven_intro_andevcon2.pdf`.
- **In the spotlight** — 7 Nov 2011 — <https://simpligility.ca/2011/11/in-the-spotlight/> — Sonatype community-spotlight recognition (the spotlight post itself is already in write log 2011).
- **News about testing Android apps** — 10 Nov 2011 — <https://simpligility.ca/2011/11/news-about-testing-android-apps/> — Follow-up on TDD/BDD after the AnDevCon workshop.

## 2012

- **Android Lint available in the Central Repository** — 19 Jan 2012 — <https://simpligility.ca/2012/01/android-lint-available-in-the-central-repository/>
- **Android Compatibility Library following Lint** — 31 Jan 2012 — <https://simpligility.ca/2012/01/android-compatibility-library-following-lint/>
- **AnDevCon III Fireside Chat – Tricks of the Trade** — 11 Mar 2012 — <https://simpligility.ca/2012/03/andevcon-iii-fireside-chat-tricks-of-the-trade/> — `EVENT →` AnDevCon III fireside chat, 16 May 2012 (announcement).
- **Apache Maven for Android Development Pros and Teams** — 14 May 2012 — <https://simpligility.ca/2012/05/apache-maven-for-android-development-pros-and-teams/> — `EVENT →` AnDevCon III workshop. Slides: `android-maven-workshop-simpligility-andevcon3.pdf`; materials ZIP.
- **Android Open Source – so what?** — 16 May 2012 — <https://simpligility.ca/2012/05/android-open-source-so-what/> — `EVENT →` AnDevCon III lightning talk (300+ attendees). Slides: `open_source_cooperation_lightning_talk.pdf`.
- **Fireside Chat at AnDevCon III a Roaring Success** — 18 May 2012 — <https://simpligility.ca/2012/05/fireside-chat-at-andevcon-iii-a-roaring-success/> — `EVENT →` AnDevCon III fireside chat recap (16 May 2012, six experts, 2.5 h).
- **Launching the Google Developer Group Victoria BC** — 11 June 2012 — <https://simpligility.ca/2012/06/launching-the-google-developer-group-victoria-bc/> — `EVENT →` GDG Victoria BC launch (user-group founding).
- **Google IO 2012 Recap** — 3 July 2012 — <https://simpligility.ca/2012/07/google-io-2012-recap/> — `EVENT →` Google I/O 2012, Moscone West San Francisco, 27–29 June 2012 (GDG Leaders Summit 26 June); attended.
- **JellyBean, GCM and Javadoc for the Maven Android SDK Deployer** — 4 July 2012 — <https://simpligility.ca/2012/07/jellybean-gcm-and-javadoc-for-the-maven-android-sdk-deployer/>
- **A fantastic opportunity to learn Git** — 6 July 2012 — <https://simpligility.ca/2012/07/a-fantastic-opportunity-to-learn-git/> — `EVENT →` full-day Git/GitHub workshop with Matthew McCullough (GitHub), Victoria BC, 29 August 2012; co-organized by VIJUG + GDG Victoria.
- **Ask Your Expert Peers** — 23 Aug 2012 — <https://simpligility.ca/2012/08/ask-your-expert-peers/> — On the fireside-chat user-group format.
- **You don't do Repository Driven Development yet? Where have you been?** — 20 Sep 2012 — <https://simpligility.ca/2012/09/you-dont-do-repository-driven-development-yet-where-have-you-been/>
- **Jenkins User Conference SF and JavaOne 2012** — 15 Oct 2012 — <https://simpligility.ca/2012/10/jenkins-user-conference-sf-and-javaone-2012/> — `EVENT →` Jenkins User Conference SF 2012 (already in event log) + JavaOne 2012 (Sonatype booth support), San Francisco. Video (Confreaks), slides.

## 2013

- **Android Development Growing Up – Fireside Chat at AnDevCon 5** — 13 Feb 2013 — <https://simpligility.ca/2013/02/android-development-growing-up-fireside-chat-at-andevcon-5/> — `EVENT →` AnDevCon 5 fireside chat, Boston (date in post ambiguous — verify).

## 2014

- **Android Maven Plugin 4.0.0 ships** — 26 Nov 2014 — <https://simpligility.ca/2014/11/android-maven-plugin-4-0-0-ships/>

## 2015

- **ksoap2-android 3.4.0 and next steps** — 8 Jan 2015 — <https://simpligility.ca/2015/01/ksoap2-android-3-4-0-next-steps/>
- **CLS, OSCON and Devoxx4Kids** — 6 Aug 2015 — <https://simpligility.ca/2015/08/cls-oscon-and-devoxx4kids/> — `EVENT →` Portland, July 2015: OSCON talk "Getting your ducks in a row – an introduction to managing components in your software supply chain" (slides: `sonatype.github.io/nexus-presentations/component-software-supply-chain.html`); also Community Leadership Summit and Devoxx4Kids.
- **Maven Central In Your Hands and Other News** — 29 Oct 2015 — <https://simpligility.ca/2015/10/maven-central-in-your-hands-and-other-news/> — `EVENT →` JavaOne 2015, October 2015: talk "Still Rocking it Maven" with Jason van Zyl. Slides: `takari.github.io/javaone2015/still-rocking-it-maven.html`; source `github.com/takari/javaone2015`.

## 2016

- **Android Maven Plugin 4.4.1 Released** — 31 Jan 2016 — <https://simpligility.ca/2016/01/android-maven-plugin-4-4-1-released/>
- **Android NDK Maven Plugin 1.1.0 Released** — 15 Feb 2016 — <https://simpligility.ca/2016/02/android-ndk-maven-plugin-1-1-0-released/>
- **Android NDK Maven Plugin 1.1.1 Released** — 22 Mar 2016 — <https://simpligility.ca/2016/03/android-ndk-maven-plugin-1-1-1-released/>
- **Impressions from DevOpsDays Vancouver 2016** — 18 Apr 2016 — <https://simpligility.ca/2016/04/impressions-devopsdays-vancouver-2016/> — `EVENT →` DevOpsDays Vancouver 2016, Vancouver, April 2016. `VIDEO →` his Ignite talk recording <https://www.youtube.com/watch?v=M2mnDiWJhOY> (at 3h17m17s); slides on Google Slides.
- **Maven Repository Provisioner goes 1.0.0 and beyond** — 26 Apr 2016 — <https://simpligility.ca/2016/04/maven-repository-provisioner-goes-1-0-0/>
- **Easy Publishing to the Central Repository** — 26 Apr 2016 — <https://simpligility.ca/2016/04/easy-publishing-to-the-central-repository/> — `VIDEO →` 8-part Central Repository publishing series (**already in video log**).
- **Progressive Organization POM 5.0.0 Released** — 31 May 2016 — <https://simpligility.ca/2016/05/progressive-organization-pom-5-0-0-released/>
- **ksoap2-android meets okhttp** — 31 May 2016 — <https://simpligility.ca/2016/05/ksoap2-android-meets-okhttp/>
- **Android Maven Plugin 4.4.2 Released** — 31 May 2016 — <https://simpligility.ca/2016/05/android-maven-plugin-4-4-2-released/>
- **Android NDK Maven Plugin 1.1.2 Released** — 18 July 2016 — <https://simpligility.ca/2016/07/android-ndk-maven-plugin-1-1-2-released/>
- **Android Maven Plugin 4.4.3 Released** — 18 July 2016 — <https://simpligility.ca/2016/07/android-maven-plugin-4-4-3-released/>

## 2017

(OneOps blog posts and the Java Magazine article for 2017 are already in the write log; these are the self-hosted simpligility.ca posts.)

- **Android Maven Plugin 4.5.0 Released** — 19 July 2017 — <https://simpligility.ca/2017/07/android-maven-plugin-4-5-0-released/>
- **Maven Repository Provisioner 1.2.1** — 19 July 2017 — <https://simpligility.ca/2017/07/maven-repository-provisioner-1-2-1/>

## 2018

- **ksoap2-android 3.6.3** — 26 Nov 2018 — <https://simpligility.ca/2018/11/ksoap2-android-3-6-3/>

## 2019

- **Recent Maven Wrapper Updates** — 26 Mar 2019 — <https://simpligility.ca/2019/03/recent-maven-wrapper-updates/> — maven-wrapper 0.5.4 and takari-maven-plugin 0.7.5.
- **ksoap-android 3.6.4** — 29 Mar 2019 — <https://simpligility.ca/2019/03/ksoap-android-3-6-4/>
- **Kotlin for polyglot-maven** — 29 Mar 2019 — <https://simpligility.ca/2019/03/kotlin-for-polyglot-maven/>
- **Maven Repository Provisioner 1.4.0** — 3 Apr 2019 — <https://simpligility.ca/2019/04/maven-repository-provisioner-1-4-0/>
- **Android Maven Plugin 4.6.0 Released** — 9 May 2019 — <https://simpligility.ca/2019/05/android-maven-plugin-4-6-0-released/>
- **Kotlin Improvements for Polyglot-Maven** — 7 June 2019 — <https://simpligility.ca/2019/06/kotlin-improvements-for-polyglot-maven/>

## 2020

- **Free Book No. 5 – Presto The Definitive Guide** — 14 Apr 2020 — <https://simpligility.ca/2020/04/free-book-no-5-presto-the-definitive-guide/>
- **On FLOSS Weekly about Presto/Trino** — 7 May 2020 — <https://simpligility.ca/2020/05/on-floss-weekly-about-presto/> — `VIDEO / EVENT →` FLOSS Weekly Episode 577 (with Dain Sundstrom; host Randal Schwartz, co-host Simon Phipps): <https://twit.tv/shows/floss-weekly/episodes/577>. Appearance — decide event log vs video log.
- **Join me for Presto First Steps** — 5 Oct 2020 — <https://simpligility.ca/2020/10/join-me-for-presto-first-steps/> — Announces the O'Reilly Presto First Steps training.

## 2022

- **Trino The Definitive Guide 2nd edition** — 3 Oct 2022 — <https://simpligility.ca/2022/10/trino-the-definitive-guide-2nd-edition/>
- **Next week is Trino week** — 4 Nov 2022 — <https://simpligility.ca/2022/11/next-week-is-trino-week/>
- **Trino guide for everyone in 2023** — 30 Dec 2022 — <https://simpligility.ca/2022/12/trino-guide-for-everyone-in-2023/>

## 2023

- **In service of Trino and Commander Bun Bun** — 8 May 2023 — <https://simpligility.ca/2023/05/in-service-of-trino-and-commander-bun-bun/> — His history with Trino/Presto.
- **Personal takeaways from Open Source Summit** — 16 May 2023 — <https://simpligility.ca/2023/05/personal-takeaways-from-open-source-summit/> — `EVENT →` OSS NA 2023, Vancouver (already in event log). `VIDEO →` SiliconANGLE theCUBE interview (already in event log).

## 2024

- **Meeting old and new friends in Seattle** — 9 Apr 2024 — <https://simpligility.ca/2024/04/meeting-old-and-new-friends-in-seattle/> — `EVENT →` Open Source Summit NA 2024, Seattle (announcement) + Trino meetup.
- **Recap about DET meetup and Open Source Summit in Seattle** — 28 Apr 2024 — <https://simpligility.ca/2024/04/recap-from-det-meetup-and-open-source-summit-na/> — `EVENT →` Data Engineer Things meetup, Bellevue WA, early April 2024 — talk "Big Data Whirlwind Tour" on Trino (~100+ attendees); and Open Source Summit NA 2024, Seattle.
- **It's showtime, it's IO time** — 9 May 2024 — <https://simpligility.ca/2024/05/its-showtime-its-io-time/> — `EVENT →` Google I/O 2024 (announcement).
- **Google doubling down on AI** — 20 May 2024 — <https://simpligility.ca/2024/05/google-doubling-down-on-ai/> — `EVENT →` Google I/O 2024, Mountain View CA, May 2024 (attended).

## 2025

- **Wrapping up my 2024 with Trino** — 10 Jan 2025 — <https://simpligility.ca/2025/01/wrapping-up-my-2024-with-trino/>
- **Six months a Chainguardian!** — 21 Sep 2025 — <https://simpligility.ca/2025/09/six-months-a-chainguardian/> — `VIDEO →` "fun PSA" video on joining Chainguard: <https://www.youtube.com/watch?v=OA9EpeBnwrA>.
- **A new chapter – your support makes a difference** — 6 Oct 2025 — <https://simpligility.ca/2025/10/a-new-chapter-your-support-makes-a-difference/> — GitHub Sponsors ask for continued open source work.

---

## Other-site writing surfaced by these posts

Publications on sites other than simpligility.ca, referenced from the posts
above, for the [write log](STATUS.md):

- **SD Times interview on Honeycomb development** — March 2011 — referenced from "About delicious honeycomb". Track down the SD Times URL.
- TheServerSide interviews (Sept 2011) — already in write log.
- OSCON 2015 supply-chain slide deck and JavaOne 2015 "Still Rocking it Maven" deck — hosted on GitHub Pages (see 2015 entries) — decks, not articles; belong in the event log entries.
