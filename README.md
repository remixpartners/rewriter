# Rewriter

A Claude Code skill that rewrites raw content into clean business prose -- with optional voice matching. Four editing stages run in sequence: a Strategist finds the point, a Craftsman rebuilds the sentences, an Anti-AI Scrub removes machine-generated style, and a Voice agent (optional) transforms the output into a specific person's voice. You orchestrate them as the Editor and do the final quality pass.

For short inputs (under 1,500 words), Fast Mode runs everything as a single pass with no sub-agents.

## What it does

You give it rough text -- notes from a call, a first draft, a ChatGPT dump, anything. It returns prose that reads like a human wrote it for Harvard Business Review. Or, if you've built a voice guide, it returns prose that reads like *you* wrote it.

The pipeline cuts word count by 40-60% with zero information loss. It does this by finding the buried lead, restructuring around it, tightening every sentence, and killing the vocabulary and patterns that mark AI-generated text.

## Install

Download `rewriter.skill` from the [Releases](../../releases) page, then:

```
claude install-skill rewriter.skill
```

Or clone this repo and point Claude Code at the SKILL.md directly.

## Usage

Type `/rewriter` in Claude Code, or ask Claude to "rewrite this" / "clean this up" / "make this professional" / "rewrite in my voice."

The skill asks one question before starting: do you want to provide context about audience and purpose, or should it jump straight in? If you share details, it runs a short intake interview (purpose, audience, intensity level 1-5). If not, it starts editing immediately.

**Intensity levels:**

- **1-2**: Light polish. Preserves your structure and voice. Tightens without reimagining.
- **3**: Editor's judgment. Restructures where needed, leaves what works.
- **4-5**: Full rewrite. Finds the point, restructures around it, rebuilds from scratch.

## The pipeline

```
         THE EDITOR (you)
         +--------------------+
         | 0. Mode check      |  Fast mode or full pipeline?
         | 1. Intake          |  Gather context, check for voice
         | 2. Dispatch        |  Run stages in sequence
         | 3. Final edit      |  Coherence, tone, completeness
         | 4. Voice (opt.)    |  Apply user's voice guide
         +--------+-----------+
                  |
    +--------+----+-----+-----------+
    v        v          v           v
STRATEGIST  CRAFTSMAN  ANTI-AI   VOICE LAYER
                       SCRUB     (optional)
```

### Stage 1: Strategist

Finds the point. Restructures around it. Does not touch sentences.

Draws on Steven Pinker's classic style (orient the reader's gaze toward something real) and Chip Heath's Commander's Intent (if everything else falls away, what survives?). Asks six questions of the input before changing a word: What is this showing the reader? What's the one thing that matters? Where's the gap? Am I assuming too much? Is this concrete or abstract? Does it break a pattern?

### Stage 2: Craftsman

Rebuilds sentences word by word. The register is sharp analyst, not marketer.

Draws on Verlyn Klinkenborg's sentence-level craft and Strunk & White's structural rules -- active voice, positive form, concrete language, omit needless words, emphatic endings. Kills transitions, kills zombie nouns, varies sentence rhythm.

### Stage 3: Anti-AI Scrub

Removes every pattern that flags text as AI-generated.

Fetches the latest [Wikipedia guide to AI writing signs](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (updated regularly as LLM behavior changes) and scans for: cursed vocabulary, negative parallelisms, rule-of-three lists, em dash overuse, editorial commentary, compulsive summaries, hedging pileups, promotional tone, copula avoidance, dangling significance, legacy inflation, vague attributions, elegant variation, and the "one of the most" formula.

### Stage 4: Editor pass

Checks coherence (do paragraphs follow?), tone (does it sound like one voice?), completeness (did anything get lost?), precision (are claims specific?), and format compliance (right length, register, structure for the stated purpose). If voice is not active, this is the final output. If voice is active, passes to Stage 5.

### Stage 5: Voice Layer (optional)

Transforms the polished output into a specific voice -- a person, a publication, or a brand.

Reads a voice guide from `voices/[name].md` and applies the voice's actual patterns: idea architecture, sentence rhythm, word palette, register calibration, and anti-patterns. Voice guide patterns with direct-quote evidence override Scrub rules. Global user rules (CLAUDE.md) override everything. After the Voice Layer, the Editor does one final verification scan before delivering.

## Voice matching

The rewriter can write in any voice -- a person, a publication, or a brand -- if you build a voice guide first.

### Voice types

- **Person voice:** How a specific individual speaks and writes. Built from transcripts, emails, slides, blog posts.
- **Publication voice:** The editorial style of a newsletter, blog, or content series. Built from published articles and editorial guidelines.
- **Brand voice:** How an organization communicates. Built from marketing materials, style guides, and past campaigns.

### Building a voice guide

Run `/rewriter voice-analyze` or tell Claude "build a voice profile." The Voice Analyzer walks you through:

1. **Identify voice type** -- person, publication, or brand. This determines source types.
2. **Gathering sources** -- for people: transcripts, emails, slides. For publications: articles, style guides. More variety produces a better guide.
3. **Dispatching analysis agents** -- parallel agents analyze sources across dimensions (idea architecture, sentence patterns, word palette, etc.)
4. **Synthesis** -- findings merge into a structured voice guide covering idea architecture, sentence patterns, word palette, register dials, and anti-patterns.
5. **Review** -- you read the guide and confirm it captures the voice.

The output is saved to `voices/[name].md`. Once it exists, the rewriter auto-detects it during intake. Multiple voice guides can coexist -- the rewriter lists all available voices and lets you choose.

### Privacy

Voice guides are gitignored by default. Your voice stays on your machine. The skill ships with the tools to build a voice guide, not with anyone's actual voice.

## Fast mode

Inputs under 1,500 words skip the sub-agent pipeline entirely. The Editor runs all four stages inline as a single pass. Same quality, 2-3 minutes faster.

Why 1,500 words? Below that, all reference material (~35K tokens) plus input and output fit in a single attention window. Above it, focused per-stage sub-agents produce better results.

## Example

**Input** (AI-generated):

> In the ever-evolving landscape of the electric vehicle industry, Tesla, Inc. stands as a beacon of innovation and disruption. It is worth noting that Tesla's journey from a niche EV startup to one of the most valuable companies on the planet has been nothing short of remarkable, and its executive leadership team plays a pivotal role in navigating the complex challenges and exciting opportunities that lie ahead.

**Output** (after pipeline):

> Tesla's revenue fell for the first time in company history in 2025. Full-year sales dropped to $94.8 billion from $97.7 billion. Q4 net income fell 61%, to $840 million.

67 words became 30. Every fact survived. The filler didn't.

## Reference files

The skill includes six reference files that the sub-agents consult at their respective stages:

| File | Stage | Source |
|---|---|---|
| `pinker-clarity.md` | Strategist | Steven Pinker, *The Sense of Style* (2014) |
| `heath-stickiness.md` | Strategist | Chip & Dan Heath, *Made to Stick* (2007) |
| `klinkenborg-sentences.md` | Craftsman | Verlyn Klinkenborg, *Several Short Sentences About Writing* (2012) |
| `strunk-white-elements.md` | Craftsman | Strunk & White, *The Elements of Style*, 4th ed. (2000) |
| `anti-ai-checklist.md` | Scrub (fallback) | Distilled from [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) |
| `voice-guide-template.md` | Voice Layer | Template for building voice guides |

## Edge cases

- **Input is already polished.** Skips the Strategist and Craftsman. Sends straight to the Scrub.
- **Input has no discernible point.** Asks the user: "What's the one thing you want the reader to take away?"
- **User wants to preserve their voice.** At intensity 1-2, the Craftsman tightens without imposing a new voice.
- **User wants a specific voice applied.** If a voice guide exists in `voices/`, the Voice Layer runs after the Editor pass. Multiple guides are listed for the user to choose from.
- **User disagrees with the rewrite.** Shows intermediate stages (Strategist, Craftsman, Scrub, Voice) so you can pinpoint where it went wrong.
- **Input is over 5,000 words.** Applies the pipeline section by section.
- **Voice guide conflicts with style rules.** Voice wins. If the voice guide has direct-quote evidence that the voice genuinely uses a construction, the Voice Layer preserves it.

## Changelog

### 1.2 (2026-03-25)
- **Multi-voice types**: Voice guides now support persons, publications, and brands (not just individuals)
- **Publication voice support**: Voice Analyzer handles article-based analysis for editorial/newsletter voices
- **Voice guide template**: Updated with publication/brand compression tables and voice-type metadata
- **Multiple voices**: Rewriter auto-detects and lists all guides in `voices/` during intake

### 1.1 (2026-03-24)
- **Voice matching**: Voice Layer (Stage 4) transforms output into a specific voice using voice guides
- **Voice Analyzer**: Sub-skill (`VOICE-ANALYZER.md`) builds voice guides from transcripts, emails, slides, and other writing samples
- **Fast mode**: Inputs under 1,500 words skip sub-agents, run the full pipeline as a single pass
- **Voice guide template**: Structured template (`references/voice-guide-template.md`) for building voice profiles
- Anti-AI scrub applied to all documentation

### 1.0 (2026-03-23)
- Initial release: Strategist, Craftsman, Anti-AI Scrub pipeline
- Five reference files (Pinker, Heath, Klinkenborg, Strunk & White, anti-AI checklist)
- Intake interview with intensity levels 1-5

## License

MIT. See [LICENSE](LICENSE).

## Built by

[Remix Partners](https://remixpartners.ai) -- we help companies turn generative AI from sideline experiments into growth engines.
