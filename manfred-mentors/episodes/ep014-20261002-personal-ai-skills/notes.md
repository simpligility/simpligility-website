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

Teaser description for StreamYard, used on YouTube, LinkedIn, and Twitch. Each
paragraph is on a single line so it pastes without hard line breaks.

```text
Skills are meant to teach an AI agent how to do a task. I've been abusing them for something else: a personal config system that teaches every AI tool I use how I work. That covers my commit conventions, my writing style, and who I am.

In this live session I walk through my own skill family. It lives in one git repository, is linked into Claude Code, Codex CLI, Copilot, and others, and has a base skill that routes to topic-specific child skills. It's optional and flexible: it only kicks in when I want it, and it grows one skill at a time. We'll watch an agent get things wrong without the skills, then right with them, and look at how you can adapt the pattern for your own preferences and projects.

Unedited, real-time work, as always. Bring your questions.
```


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


## Benefits

The points to land as the takeaway, whether in the wrap-up or along the way:

* **Across harnesses.** The same skills work in Claude Code, opencode, Codex
  CLI, GitHub Copilot, Antigravity, and any other tool that reads `SKILL.md`.
* **Across models.** The skills are plain markdown, so they carry over
  unchanged when switching models within a tool or between vendors.
* **Across computers.** The skills live in a git repo. On a new machine, clone
  or pull the repo, run the install scripts, and every tool is set up.
* **Yours to copy.** Anyone can copy the skills, rename them, and replace the
  contents to make the setup their own. The structure is the valuable part.
* **Modular and dynamic.** Each skill covers one use case, and a skill loads
  only when it is invoked, so the context stays small and relevant. The
  `trinodb-*` family shows the same property in a later episode.


## Demo outline

The cold-start task asks the agent to build a small dice roller in Python with
a README and commit it, in a throwaway repo. One task exercises both
`manfred-writing` and `manfred-git`, and a dice roller for board games and
RPGs is a fun, easy-to-follow thing to build on camera.

Setup, done live at the start of the demo: two empty, unpushed repos side by
side, `~/training/mm014-cold` and `~/training/mm014-warm`, each created with
`git init`.

The prompt, identical both times and with no style hints:

```
Create a small command-line script that rolls dice for board games and tabletop
RPGs with a README.md that explains how to use it. Each invocation should do one
roll of each dice by default. There should be options to set number of dice and
type of dice. The supported dice type should be d4, d6, d8, d10, d12, and d20.
```

1. In `mm014-cold`, start a fresh session without invoking `/manfred` and run
   the prompt. The gated children cannot load without the base skill, so this
   also shows the gating. Let the result be wrong in the ordinary ways.
2. Open the `getting-stuff-done` repo and walk the `skills/` directory. Show one
   `SKILL.md` in full so viewers see there is no magic in the format.
3. Run `install-skills.sh` and show the symlinks it creates across tool
   directories. Point out that editing happens only in the repo.
4. In `mm014-warm`, start a fresh session, invoke `/manfred`, and show the skill
   index table routing to a child.
5. Run the same prompt, then compare from `~/training` with
   `git -C mm014-cold log -1`, `git -C mm014-warm log -1`, and
   `diff mm014-cold/README.md mm014-warm/README.md`. The generated code differs
   between any two runs, so comparing it is noise. Compare the commit and the
   README only.
6. Wrap up with how to copy the pattern.

What to point at in the comparison:

* Guaranteed: the commit trailer. The tool default `Co-Authored-By:` becomes
  `Assisted-by:`. Lead with this one.
* Likely: Title Case headings, markdown not wrapped at 80, and a commit subject
  outside the Chris Beams rules.
* Possible: "e.g.", parentheses, and ampersands. Do not promise these on
  camera.

The `manfred` skill was refactored to load only on an explicit request, never
on identity cues, so it should stay out of the cold run. Confirm that in a
rehearsal, and note which differences actually show up.

## Status and open items

- [ ] Rehearse the cold and warm runs once in a scratch repo
- [ ] Check whether the repo is public and ready to show on stream
- [x] After streaming, add the episode to `../../manfred-mentors.html` following
      the `simpligility-manfred-mentors` skill
