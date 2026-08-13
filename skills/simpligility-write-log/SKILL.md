---
name: simpligility-write-log
description: >-
  Maintain the write log HTML fragment at write-log/write-log.html for
  simpligility.ca/write-log/. Use when adding newly discovered blog posts or
  articles Manfred has written, or keeping the layout and formatting consistent.
---

# Write log maintenance

This skill keeps `write-log/write-log.html` consistent when adding or editing
entries. It covers only what is specific to the write log.

**Read [`simpligility-site`](../simpligility-site/SKILL.md) first.** It holds
the conventions the event, write, and video logs share: the WordPress fragment
skeleton, the year navigation and its sticky counterpart, the ordering rules,
the `<dt>` and `<dd>` entry format, the root-relative link rule, the HTML entity
list, the broken-link rules, the `STATUS.md` conventions, and how to commit.
Where this file repeats something from there, that file wins.

## Target file

- **Path from the repo root:** `write-log/write-log.html`
- The `<dt>` shape is `<strong>Title</strong><br> Publication &mdash; Date`.

## Which posts to include

Not every URL on a site is a write-log entry. When harvesting:

- **External writing only.** The write log lists writing published on **other**
  sites such as Chainguard, Trino, Sonatype, DZone, and Java Magazine. Do
  **not** add simpligility.ca's own self-hosted blog posts as entries, because
  the page intro links visitors to the blog for those. A cross-posted copy
  hosted here may still appear as a secondary `Also at simpligility.ca` link on
  an external entry, but simpligility.ca is never the primary publication.
- **No books.** The co-authored books are listed on the
  [writing page](https://simpligility.ca/writing/), so they are deliberately
  **not** write-log entries and the page intro links there instead. A blog post
  announcing a book is still an entry, because the post is the writing. Do not
  re-propose adding the books themselves.
- **Skip auto-generated digests.** The old simpligility.ca blog auto-published
  weekly "Twitter Weekly Updates for YYYY-MM-DD" roundups. These are not
  authored articles, so exclude them, and treat any similar auto-posted content
  the same way.
- **One entry per post**, including short release or version-announcement posts
  such as "Android Maven Plugin 4.4.2 Released". Do not consolidate several
  releases of one project into a single entry.
- **Dedupe double-publishes.** WordPress sometimes produced duplicate slug pairs
  such as `.../slug/` and `.../slug-2/` for the same post. Add the post once,
  using the canonical non-`-2` URL.

## Deferred work: `write-log/STATUS.md`

`write-log/STATUS.md` tracks deferred work and next steps for this page, chiefly
the harvesting of posts from each site, under the STATUS conventions in the site
skill.

## Sources already swept

These sources have been harvested and are complete, so treat finding more as a
watch-for-new check rather than a backlog:

- The **simpligility.ca blog** from 2010 to 2025 is fully inventoried in
  [`../../write-log/simpligility-harvest.md`](../../write-log/simpligility-harvest.md).
  Its own self-hosted posts are not write-log entries, so the harvest is kept as
  a reference rather than a backlog: the `EVENT →` items went to the event log,
  the `VIDEO →` items to the video log, and the other-site writing it surfaced
  fed the other-publications hunt.
- The **other publications hunt** is closed. It swept for guest posts,
  interviews, and articles outside the company blogs, and the only find was the
  SD Times lead from the simpligility.ca harvest, which resolved to *Developers
  give their early impressions of the Android Honeycomb OS*, 4 March 2011, and
  is in the log. Searched and **empty**: InfoQ, The New Stack, DevOps.com,
  foojay.io, opensource.com, and devm.io together with its JAXenter archive.
  Manfred settled the remaining outlets named on the
  [writing page](https://simpligility.ca/writing/): there is nothing to add for
  **CloudBees**, the **Eclipse Foundation**, or **Telus**; his **Salesforce**
  writing was never public and is covered under Takari; **DZone** holds only the
  *npmGate* article already in the log; and **Oracle** is the single Java
  Magazine article from 2017. Do not re-run this hunt &mdash; only sweep an
  outlet that is genuinely new.
- The **Starburst blogs** were harvested in full, both the main `starburst.io`
  blog and the separate developer blog archive. The events they surfaced went to
  the event log.
- The **Sonatype author archive** was harvested for 2013 to 2016. The live site
  at `www.sonatype.com/blog/author/manfred-moser` is a JS-rendered SPA the
  tooling here cannot read, so the listing was recovered from Wayback snapshots
  of the old `blog.sonatype.com/author/manfred-moser` pages. **No 2015 posts
  exist** &mdash; the archive runs from December 2014 straight to February 2016,
  so there is no 2015 block and none is expected. Author-archive **page 3**, the
  oldest posts from 2011 and 2012, could not be re-fetched from Wayback because
  the snapshots 504 or are absent, but all known posts from that era are already
  in the log, three 2012 Nexus, Insight, and Maven posts plus the November 2011
  community spotlight, so it is treated as complete. Add more only if Manfred
  recalls them. Posts by others that merely reference him, such as Mark
  Miller&#39;s *TheNexus: A community project*, are correctly excluded. Nexus
  Live is handled in the event log, not here.
- The **Trino and Presto blogs** on `trino.io` and the Presto-era posts were
  harvested into the log.
- The **mosabuam.com** personal blog was harvested from the author archive at
  <https://www.mosabuam.com/author/manfred>, 6 pages and 76 posts from 2001 to
  2010. **Only the technology posts are in the log**, 32 of them, in the 2001,
  2003, 2006, 2007, 2009, and 2010 blocks. The rest of the site is personal
  writing about travel, paddling, biking, and recipes, plus two Twitter digest
  posts, and is deliberately **excluded** per Manfred. He reviewed the
  borderline cases one by one and settled them as follows, so do not re-propose
  either group:
  - **In:** *The original waterways is still online*, the 1996 hand-coded site
    kept for the web-history angle even though its subject is kayaking, and
    *Mosabuam.com update &ndash; Step 1*, part of the site's build story
    alongside the Postnuke theme releases.
  - **Out:** *Back on the internet and in the Java world*, *My new camcorder
    &ndash; Sharp VL-AX1E*, *Gallery all up and well again*, and *Mailinglists
    down*.
- The **Takari blog** at `takari.io/blog.html` from 2014 to 2015, now offline
  and read via Wayback, was swept and holds nothing to add. Every post is
  authored by Jason van Zyl or other Takari and Maven contributors, and the
  string "Manfred Moser" appears in none of the roughly 28 posts. The weekly
  Maven developer hangouts announced there are events, already in the event log
  as the two per-year aggregate entries.

## The publication slot

The write log puts the publication between the title and the date:

```html
  <dt><strong>Post title</strong><br> Chainguard blog &mdash; 5 June 2025</dt>
```

Use a clean human name for the site rather than a bare URL: `Chainguard blog`,
`Sonatype blog`, `Trino blog`, `DZone`, `InfoQ`. The full URL belongs in the
link.

## Link labels and enforced order

The post itself always leads, since the page is a list of posts. Include only
the links that apply, in this order:

1. **The post** — the canonical link to read it, labelled `Read on <site>` using
   the host the link points at, such as `Read on chainguard.dev` or `Read on
   trino.io`. This keeps the label distinct from the human publication name in
   the `<dt>` and tells the reader where the link goes.
2. `Also at <site>` — a republished or cross-posted copy, using the other host
   in the label so the two read-links never share the same text.
3. `Video` — a companion recording for the post.
4. `Details` — a related page such as the event it accompanied, a project page,
   or a follow-up. Use a specific label instead when there is more than one.

## Process for adding a new entry

1. **Gather the facts from the source.** Fetch the post and pull out:
   - the **title**, its real headline,
   - the **publication** it appeared on,
   - the **date** published, in the most precise form available,
   - a **one or two sentence description** of what it covered,
   - the **canonical link**, plus any cross-post, companion video, or related
     page.

   If you cannot find a reliable link for an artifact the user mentions, **ask
   for the URL** rather than guessing. Never invent a link.
2. Read `write-log/write-log.html`.
3. Find the matching year block, or create one in the correct descending-year
   position with its `id` and navigation link.
4. Build the `<dt>` and `<dd>` pair: sentence-case title, publication and date in
   the `<dt>`, description, then the links line with the post leading.
5. Insert it at the correct reverse-chronological position within the year, with
   a blank line separating it from its neighbours.
6. Bump the `<!-- Last updated -->` comment.
7. Run the checklist in the site skill, plus the write-log points that follow.

### Worked example

Source: the blog post *Fork yeah: We're bringing kaniko back* on the Chainguard
blog, published 5 June 2025, with a companion video. Placed in the `2025` block:

```html
  <dt><strong>Fork yeah: We&#39;re bringing kaniko back</strong><br> Chainguard blog &mdash; 5 June 2025</dt>
  <dd>
    On Chainguard forking the kaniko container build tool after Google archived it, and committing to maintain it as open source.
    <a href="https://www.chainguard.dev/unchained/fork-yeah-were-bringing-kaniko-back">Read on chainguard.dev</a> &bull; <a href="https://www.youtube.com/watch?v=NPOC2n-anAU">Video</a>
    <br><br>
  </dd>
```

## Checklist for the write log

Run the shared checklist in the site skill first, then confirm:

- [ ] The post was published on another site, not self-hosted here, and is not a
      book or an auto-generated digest.
- [ ] Publication is a clean human name in the `<dt>`.
- [ ] The post leads with a `Read on <site>` label, and a cross-post uses `Also
      at <site>` with a different host.
