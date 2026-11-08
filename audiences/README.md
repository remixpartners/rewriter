# Audience Guides

This folder holds **audience guides**: short, evidence-based profiles of the people a piece is written for. A voice guide controls how the writing sounds; an audience guide tells the rewriter what the reader already knows, which terms they use, what they want, and what makes them skeptical.

## How the rewriter finds guides

During intake (the Audience Check), the rewriter scans for `*.md` audience guides in these locations, in order:

1. **This folder** (`audiences/` inside the rewriter skill).
2. **A shared library** at `~/.claude/skills/audiences/`, if it exists.
3. **An `audience-guides/` folder in your current working directory**: use this in Cowork, where the skill's own folder can be reset between sessions.

Files named `README.md` or `EXAMPLE.md`, and any file starting with `_` or `.`, are ignored.

The audience named for a specific piece always overrides the guide. A missing guide never blocks a rewrite.

## Adding one

Copy `../references/audience-guide-template.md` to `audiences/<audience-name>.md` (lowercase, hyphenated, e.g. `smb-owners.md`) and fill it in. Every observation needs a basis label (documented, positioning, writer instruction, or inference) and a source. Leave a section open rather than invent a persona to fill it.

## Privacy

Real audience guides are **gitignored by default**: they often draw on client conversations. Only this README ships with the skill.
