# Voice Guides

This folder holds **voice guides** -- structured profiles that teach the rewriter to write in a specific voice (a person, a publication, or a brand). When you ask the rewriter to "write in my voice," it reads a guide from here and transforms the polished draft to match.

## How the rewriter finds guides

During intake, the rewriter scans for `*.md` voice guides in these locations, in order:

1. **This folder** (`voices/` inside the rewriter skill).
2. **A shared library** at `~/.claude/skills/voices/`, if it exists -- handy if you keep one set of voices across several skills.
3. **A `voice-guides/` folder in your current working directory** -- use this in Cowork, where the skill's own folder can be reset between sessions.

Files named `README.md` or `EXAMPLE.md`, and any file starting with `_` or `.`, are ignored -- they are scaffolding, not voices.

## Adding your own voice guide

Two ways:

- **Guided (recommended):** run `/rewriter voice-analyze`, or tell Claude "build a voice profile." It interviews you, analyzes your writing samples, and saves a finished guide.
- **By hand:** copy `../references/voice-guide-template.md` to `voices/<your-name>.md` and fill it in. Use a lowercase, hyphenated name (e.g. `steven.md`, `acme-brand.md`).

See `EXAMPLE.md` in this folder for a complete, filled-in guide you can model yours on.

## Privacy

Real voice guides are **gitignored by default** -- they capture personal communication patterns and stay on your machine. Only this README and `EXAMPLE.md` ship with the skill. To deliberately version-control a guide, force-add it: `git add -f voices/<name>.md`.

## Cowork note

Cowork may treat the skill's own folder as scratch space and clear it between sessions. To keep a voice guide you build in Cowork, save it in your **workspace** (a `voice-guides/` folder works well), not inside the skill folder. The rewriter checks there too.
