# Site — work status and next steps

Repo-wide and cross-cutting tasks for the simpligility.ca content managed in this
repo. Work that belongs to a single log lives in that log's own STATUS file:
[`event-log/STATUS.md`](event-log/STATUS.md),
[`video-log/STATUS.md`](video-log/STATUS.md), and
[`write-log/STATUS.md`](write-log/STATUS.md). This file is for work that spans
more than one of them, or the site as a whole. It is a living to-do list, not a
historical log: when a task is finished, **remove it** rather than marking it
done, and bump the "Last updated" date when you edit it.

Last updated: 2026-08-12 (closed the About-page links and reframed the width task)

---

## 1. Establish a regular Manfred mentors cadence

Set a regular, predictable streaming cadence for *Manfred mentors* &mdash; for
example a fixed weekly or biweekly day and time &mdash; and commit to it rather
than streaming ad hoc. Decide the interval, announce the schedule on the
dedicated page and the streaming platforms (YouTube, LinkedIn, Twitch), and then
run with it consistently.

## 2. Sweep the GitHub repositories for talk and video material

Go through the repositories in the
[`mosabua`](https://github.com/mosabua?tab=repositories) and
[`simpligility`](https://github.com/simpligility?tab=repositories) GitHub
accounts and look for slide decks, demo projects, workshop material, and other
artifacts that document a talk, a workshop, or a recorded session. Many of
these repositories are named after the event or the topic and carry the date in
the README or the commit history, so they are a good source of entries that are
missing from the logs.

For each find, decide which log it belongs in &mdash; a conference or meetup
appearance goes in the [event log](event-log/STATUS.md), a recording goes in the
[video log](video-log/STATUS.md), and written material goes in the
[write log](write-log/STATUS.md) &mdash; then add it following that log's skill.
A repository can feed more than one log when a talk was both delivered and
recorded. Existing entries can also gain a link to the matching repository as a
slides or material reference. Do the sweep in a single pass with all three logs
in mind, and record the accounts as swept in the relevant skills once it is
done.

## 3. Find readable copies of the three Sonatype books

*Repository Management with Nexus*, *Maven: The Complete Reference*, and *Maven
by Example* are listed on the [writing page](https://simpligility.ca/writing/)
with source-code links only, so a visitor has no way to actually read them. The
old `books.sonatype.com` URLs now redirect to Sonatype marketing pages and the
rendered books are gone.

Dig through the local archives, old machines, and backups for PDF copies. If
any turn up, upload them to the website and link them from the matching book on
the writing page, so the entry offers the book itself next to its source. Where
no PDF survives, check whether the book can be rebuilt from the source
repositories &mdash; `simpligility/nexus-book`,
`simpligility/maven-reference-en`, and `simpligility/maven-example-en` &mdash;
before giving up on it.

## 4. Make the page widths consistent and wider, using blocks only

The four fragment pages are each wrapped differently, so they render at
different widths:

| Page | Wrapper today | Result |
|------|---------------|--------|
| `/manfred-mentors/` | Group, `alignfull`, constrained inner layout | wide |
| `/write-log/` | Group, `alignwide`, flow inner layout | wide |
| `/event-log/` | Group, no alignment | narrow |
| `/video-log/` | no Group at all | narrow |

Work through all four in the block editor and settle on one treatment, then
apply it everywhere so the logs and the mentors archive match. Wider is the
goal: the entries are dense two-line records and the default 645px column
cramps them.

**No custom CSS.** Nothing goes into the Site Editor under Styles, Additional
CSS, and no `page-id` overrides are written. The block UI can do this on its
own, and a page that depends on a rule hidden somewhere else cannot be fixed
from the editor later. The block recipe is in
[`skills/simpligility-site/SKILL.md`](skills/simpligility-site/SKILL.md) under
*Page width*.

Take care not to disturb the fragments while rearranging blocks. Each one has to
stay inside a single Custom HTML block, because anywhere else WordPress inserts
a `<br />` after every line of the inline style and script, which silently kills
the sticky year navigation. That has already happened once to the write log.
After each page, fetch it and confirm the wrapper carries the intended alignment
class and that no `<br />` appears inside the `<style>` or `<script>`.

These are WordPress changes, not repo changes.
