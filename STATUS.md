# Site — work status and next steps

Repo-wide and cross-cutting tasks for the simpligility.ca content managed in this
repo. Work that belongs to a single log lives in that log's own STATUS file:
[`event-log/STATUS.md`](event-log/STATUS.md),
[`video-log/STATUS.md`](video-log/STATUS.md), and
[`write-log/STATUS.md`](write-log/STATUS.md). This file is for work that spans
more than one of them, or the site as a whole. It is a living to-do list, not a
historical log: when a task is finished, **remove it** rather than marking it
done, and bump the "Last updated" date when you edit it.

Last updated: 2026-10-09 (added the header image task, trimmed the width task to its open points)

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

## 4. Finish the page width work and settle block wrappers in the repo

The event, write, and video logs now all render the same way: the fragment's
Custom HTML block sits in a Group with wide alignment and flow layout, which is
the recipe in [`skills/simpligility-site/SKILL.md`](skills/simpligility-site/SKILL.md)
under *Page width*. Two points are still open.

### Bring the Manfred mentors page in line

`/manfred-mentors/` still wraps its archive in a Group with full alignment and a
constrained inner layout, unlike the logs. Decide whether it should match them,
given that the page has its own content above the archive, and if so apply the
same wide, flow-layout Group. Use blocks only, with no custom CSS, and afterwards
fetch the page to confirm the wrapper classes and that no `<br />` appears inside
the `<style>` or `<script>`.

### Decide whether to store the block wrappers in the repo

Manfred is considering having the repo fragments hold the full WordPress block
markup, meaning the `wp:group` and `wp:html` delimiters around the fragment, so
the whole page content can be pasted into the page **Code editor** in one go
rather than into a single Custom HTML block. Today no fragment in the repo
carries a wrapper.

If adopted, apply it in one pass:

- Copy the exact serialized `wp:group` markup from a live log page rather than
  writing it by hand. The skill shows the expected form.
- Wrap all repo fragments identically, in one commit.
- Update the fragment skeleton and publishing model sections of the site skill,
  which currently say fragments carry no wrapper and go into a Custom HTML
  block. Keep the `wpautop` warning.

## 5. Add a header image to the log pages

The event, write, and video log pages are walls of text and look dull. Give each
one an image, or a similar visual element, near the page title so a visitor gets
some visual entry point before the list starts.

This is WordPress-side only. Add the image as its own block in the page,
between the title and the Group that wraps the fragment, and leave the Custom
HTML block and the repo fragments untouched.

- Pick one consistent treatment for all three, such as an Image or Cover block,
  and use blocks only, with no custom CSS, as for the page width.
- Choose or create images that fit each log: talks and events, writing, and
  video.
- WordPress writes media URLs with a full domain, which conflicts with the
  root-relative link rule for the two domains. Check the stored `src` in the
  Code editor and make it root-relative, starting with `/wp-content/uploads/`.
- After each page, fetch it and confirm the fragment Group is unchanged and no
  `<br />` appears inside the `<style>` or `<script>`.
