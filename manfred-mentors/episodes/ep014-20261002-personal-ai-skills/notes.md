# Notes: episode 14

Working file for this episode. Collect ideas, shape an outline, and track open
items here.

Planned stream: Friday, 2 October 2026, 12pm Pacific (3pm Eastern, 9pm CEST).

Topic: using skills to teach AI tools a set of personal preferences, with the
`manfred-*` skill family as the worked example. Other skill families and the
memory question are parked in the episode 15 notes.


## Title

Final title: **Hacking AI "skills" into a personal config system**

The quotes around "skills" signal that the term is being stretched beyond its
usual meaning of teaching an agent a task. The working title was "Using dynamic
skills for AI preferences".


## Announcement

Teaser description for StreamYard, used on YouTube, LinkedIn, and Twitch.

> Skills are meant to teach an AI agent how to do a task. I've been abusing
> them for something else: a personal config system that teaches every AI tool
> I use how I work. That covers my commit conventions, my writing style, and
> who I am.
>
> In this live session I walk through my own skill family. It lives in one git
> repository, is linked into Claude Code, Codex CLI, Copilot, and others, and
> has a base skill that routes to topic-specific child skills. It's optional
> and flexible: it only kicks in when I want it, and it grows one skill at a
> time. We'll watch an agent get things wrong without the skills, then right
> with them, and look at how you can adapt the pattern for your own preferences
> and projects.
>
> Unedited, real-time work, as always. Bring your questions.


## Ideas

* The problem first, before any skill file appears on screen. An agent that
  does not know the conventions writes the wrong commit trailer, wraps markdown
  at the wrong width, and reaches for "e.g." in prose. Every session starts by
  re-explaining the same things.
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
6. Wrap up with how to copy the pattern.


## Status and open items

- [ ] Decide the cold-start task for step 1 so the contrast is obvious on camera
- [ ] Check whether the repo is public and ready to show on stream
- [ ] After streaming, add the episode to `../../manfred-mentors.html` following
      the `simpligility-manfred-mentors` skill
