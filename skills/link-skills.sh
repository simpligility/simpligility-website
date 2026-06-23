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

set -euo pipefail

# Repo root is the parent of the dir holding this script (script lives in skills/).
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

# Skills to link (directory names under skills/).
SKILLS=(
  simpligility-event-log
  simpligility-write-log
  simpligility-video-log
)

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
done

echo "Done. Skills linked into: ${TARGET_ROOTS[*]}"
