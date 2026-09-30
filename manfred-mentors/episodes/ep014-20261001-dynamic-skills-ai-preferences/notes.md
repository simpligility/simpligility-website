# Notes: episode 14

Working file for this episode. Collect ideas, shape an outline, and track open
items here.

Planned stream: Thursday, 1 October 2026, afternoon Pacific.

Topic: using skills to teach AI tools a set of personal preferences, with the
`manfred-*` skill family as the worked example.


## Title suggestions

* Teaching AI your preferences with skills
* Building a skill family for AI preferences
* Skills that make AI work the way you do
* One skill family, every AI tool
* From memory to skills: preferences that persist

Working title from the topic idea was "Using dynamic skills for AI
preferences". Two wobbles worth fixing before it ships: "dynamics" is a typo
for "dynamic", and "preference" reads better plural.


## Ideas

* The problem first, before any skill file appears on screen. An agent that
  does not know the conventions writes the wrong commit trailer, wraps markdown
  at the wrong width, and reaches for "e.g." in prose. Every session starts by
  re-explaining the same things.
* Built-in cross-session memory is switched off on purpose. Show that choice and
  say why: a skill file is reviewable, diffable, and version controlled, while a
  memory store is none of those.
* The open `SKILL.md` format works across every major AI coding tool, so the
  same file feeds Claude Code, opencode, Codex CLI, GitHub Copilot, and
  Antigravity.
* One source of truth, no per-tool copies. `install-skills.sh` symlinks each
  skill from the repo into the user-level skills directory of each tool, and
  `install-instructions.sh` does the same for the global instructions file that
  tools variously call `CLAUDE.md`, `AGENTS.md`, and `GEMINI.md`. Both scripts
  are idempotent, so a fresh machine is one command away.
* The base-plus-children pattern is the real content of the episode. The
  `manfred` base skill carries identity, bios, communication preferences, and
  working style, and it holds a skill index table that routes to the topic
  children.
* Gating matters. The children are written not to auto-activate on a generic
  topic match, so the base skill is their activation path. Without that, every
  markdown edit anywhere would drag in personal house style.
* `manfred-git` is a hard precondition rather than a topic match: no commit, no
  push, no PR until it is loaded. That is what keeps the `Assisted-by:` trailer
  correct instead of a tool's default `Co-authored-by:`.
* Second layer worth showing live: this website repo carries its own
  project-scoped `skills/` directory with `simpligility-site` as the base and a
  child per page section. Same pattern, different scope — personal context
  versus project context.
* Compare against the `trinodb-*` family for a third scope: project facts that
  are useful to anyone working on Trino, not just to one person.
* Close on reuse. Copy the `manfred-*` skills, rename them to another prefix,
  and replace the contents. The structure is the reusable part, not the
  specifics.


## Demo outline

Rough shape, to be firmed up before the stream.

1. Start with a small writing or git task and let the agent do it cold, with no
   skills loaded. Let the result be wrong in the ordinary ways.
2. Open the `getting-stuff-done` repo and walk the `skills/` directory. Show one
   `SKILL.md` in full so viewers see there is no magic in the format.
3. Run `install-skills.sh` and show the symlinks it creates across tool
   directories. Point out that editing happens only in the repo.
4. Invoke the `manfred` base skill and show the skill index table doing the
   routing to a child.
5. Redo the task from step 1 with the skills active and diff the two results.
6. Show the same pattern at project scope in the website repo.
7. Wrap up with how to copy the pattern.


## Status and open items

- [ ] Pick the final title from the suggestions
- [ ] Confirm the stream time and update this file
- [ ] Decide the cold-start task for step 1 so the contrast is obvious on camera
- [ ] Check whether the repo is public and ready to show on stream
- [ ] Write the YouTube title and description
- [ ] After streaming, add the episode to `../../manfred-mentors.html` following
      the `simpligility-manfred-mentors` skill
