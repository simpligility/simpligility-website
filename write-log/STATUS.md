# Write log — work status and next steps

Working notes for building out and maintaining `write-log.html`. This captures
what has been **deferred** and the **next steps**, so the work can be resumed
later with Claude Code or any other tool. Delete items as they are completed.

Last updated: 2026-08-07 (moved the completed harvests into the skill; added the Chainguard harvest task)

The conventions for this file are documented in
[`../skills/simpligility-write-log/SKILL.md`](../skills/simpligility-write-log/SKILL.md). Read that first,
in particular **Sources already swept** — the sites that are done and should not
be re-harvested.

An initial set of older posts (2011–2016) has been imported; much more remains
to be added. Much of the research overlaps with the
[event log](../event-log/STATUS.md); do it with both pages in mind so a single
pass through a site feeds both.

---

## 1. Harvest Chainguard blog posts

The log holds eight Chainguard posts from the initial harvest, all on the
Unchained blog (`chainguard.dev/unchained/...`), but the set is **not complete**
— more of Manfred's posts are unlisted, and new ones keep appearing.

**Consider waiting.** Chainguard is building an author page that is expected to
go live soon. Once it does, it collects Manfred's posts in one place and makes
this harvest far easier and more reliable than sweeping the Unchained blog by
hand. Check whether the author page is live before starting; only fall back to a
manual sweep of the blog if it is still not up when this becomes urgent.

## 2. Harvest old technology posts from mosabuam.com

Manfred has older technology-related blog posts on `mosabuam.com`. Go through
them and add an entry for each.

## 3. Track down other publications

Check for guest posts and articles on other sites and outlets (e.g. DZone,
InfoQ, devm.io, conference/community blogs, book chapters or forewords). Add any
that are found. The simpligility.ca blog harvest surfaced leads for this (e.g.
the SD Times Honeycomb interview) — see **Sources already swept** in the skill.

## 4. Link the write log from the About page books section

The site's About page has a section on the books Manfred has co-authored
(*Trino: The Definitive Guide* and *Presto: The Definitive Guide*). Add a link
from there to the write log (root-relative `/write-log/`,
<https://simpligility.ca/write-log/>) so readers who arrive via the books can
find the rest of his writing. The About page is a WordPress page, not managed in
this repo, so the edit is made in the WordPress admin. This is the
write-log-specific part of the broader About-page log-linking task in the
[top-level STATUS](../STATUS.md).
