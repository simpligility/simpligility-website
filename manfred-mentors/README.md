# Manfred mentors

This folder contains resources for maintaining and expanding the Manfred
mentors page at
[https://simpligility.ca/manfred-mentors/](https://simpligility.ca/manfred-mentors/).

The `manfred-mentors.html` file content is maintained in this repo and copied
into the code view of the page in the WordPress admin interface. It holds the
episode archive: the full list of past episodes with a title and a short
summary for each.

The skill for maintaining the file is located in
`../skills/simpligility-manfred-mentors/`.

## Episode folders

Preparation material for each episode lives in one folder per episode under
[`episodes/`](episodes/), named `epNNN-YYYYMMDD-<kebab-slug>`. The number is the
episode number, zero-padded to three digits so folders sort in episode order.
The date is the stream date, and the slug is a short identifying kebab-case name
that survives a title change. For example,
`ep014-20261002-personal-ai-skills`.

Each folder holds:

- `notes.md` — a working file for ideas, title suggestions, a demo outline, and
  open items.
- `assets/` — slides, diagrams, demo scripts, and thumbnail sources for the
  episode.

These folders are preparation only. Once an episode has streamed, it is added to
`manfred-mentors.html` as an archive entry following the skill.

[`STATUS.md`](STATUS.md) tracks deferred work and next steps. It is a living
to-do list, not a historical log: when a task is done, remove it from the file.

Manfred mentors is an ongoing live streaming show. Its episodes are listed here
rather than in the [video log](../video-log/), which points to this page
instead.
