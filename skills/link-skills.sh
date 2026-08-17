#!/usr/bin/env bash
#
# Wire the simpligility skills in skills/ into the discovery directories used by
# the various agent CLIs, via relative symlinks. The skills live in skills/ as
# the single source of truth; this script makes them discoverable without
# copying them.
#
# Coverage of the two target roots below:
#   .claude/skills  -> Claude Code (opencode also reads this root)
#   .agents/skills  -> Gemini CLI (alias), Antigravity, opencode
#
# Run from anywhere; it resolves the repo root from its own location. Idempotent
# (re-run safely after adding a skill or on a freshly cloned machine).
#
# The skill list is discovered from the filesystem rather than hardcoded, so a
# new skill needs no edit here. A hand-maintained list went stale once already
# and left two skills invisible to every agent CLI.

set -euo pipefail

# Repo root is the parent of the dir holding this script (script lives in skills/).
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

# Skills to link: every directory under skills/ that holds a SKILL.md. The glob
# expands in sorted order, so the output is stable, and a directory without a
# SKILL.md is skipped rather than linked as a broken skill.
SKILLS=()
for skill_file in skills/*/SKILL.md; do
  [[ -f "$skill_file" ]] || continue
  SKILLS+=("$(basename "$(dirname "$skill_file")")")
done

if [[ ${#SKILLS[@]} -eq 0 ]]; then
  echo "No skills found under skills/*/SKILL.md — nothing to link." >&2
  exit 1
fi

# Discovery roots to populate (relative to the repo root).
TARGET_ROOTS=(
  .claude/skills
  .agents/skills
)

for root in "${TARGET_ROOTS[@]}"; do
  mkdir -p "$root"

  # Build the "../" prefix to climb from "$root/<skill>" back to the repo root,
  # so the symlink target stays relative and survives cloning to any path.
  depth=$(awk -F/ '{print NF}' <<<"$root")
  prefix=""
  for ((i = 0; i < depth; i++)); do
    prefix="../${prefix}"
  done

  for skill in "${SKILLS[@]}"; do
    target="${prefix}skills/${skill}"
    link="${root}/${skill}"
    ln -sfn "$target" "$link"
    echo "linked ${link} -> ${target}"
  done

  # Drop symlinks for skills that no longer exist, so a renamed or deleted skill
  # does not linger as a dangling link the CLIs still try to read. Only symlinks
  # are removed; anything else in the root is left alone.
  for link in "$root"/*; do
    [[ -L "$link" ]] || continue
    name="$(basename "$link")"
    stale=1
    for skill in "${SKILLS[@]}"; do
      if [[ "$skill" == "$name" ]]; then
        stale=0
        break
      fi
    done
    if [[ $stale -eq 1 ]]; then
      rm "$link"
      echo "removed stale ${link}"
    fi
  done
done

echo "Done. Linked ${#SKILLS[@]} skills into: ${TARGET_ROOTS[*]}"
