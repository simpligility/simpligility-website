# simpligility-website

Resources and other material for the [simpligility.ca](https://simpligility.ca/)
website maintenance operated by [Manfred Moser](https://simpligility.ca/sponsor/).

## Agent skills

The `skills/` directory holds agent skills for maintaining this site (the
[event log](skills/simpligility-event-log/),
[write log](skills/simpligility-write-log/), and
[video log](skills/simpligility-video-log/)). Run `skills/link-skills.sh` to
symlink them into the discovery directories used by Claude Code, Gemini CLI,
Antigravity, and opencode. Re-run it on a fresh clone or after adding a skill.
