# Voice Guide Template

Use this structure when creating voice guides from the Voice Analyzer. The Voice Agent (Step 4 of the rewriter) reads these files to transform polished prose into a specific voice -- whether that's a person, a publication, or a brand.

Voice guides work for three types of voices:

- **Person voice:** How a specific individual speaks and writes (source: transcripts, emails, slides, blog posts)
- **Publication voice:** The editorial style of a newsletter, blog, or content series (source: published articles, editorial guidelines)
- **Brand voice:** How an organization communicates across channels (source: marketing materials, style guides, past campaigns)

Every section should include specific examples and direct quotes from the analyzed source material. A voice guide without quotes is a guess. A voice guide with quotes is evidence.

The template below is written in person-voice language ("this person"), but adapt the framing to match the voice type. For publications, "this person" becomes "this publication." For brands, "this person" becomes "this brand."

---

## Template

```markdown
# [Name] -- Voice Guide

> One-sentence summary of this person's voice in plain language.
> Example: "Direct, warm, intellectually generous. Builds from examples to principles. Casual authority."

**Source material analyzed:** [List what was analyzed: N transcripts, N emails, N presentations, date range]
**Last updated:** [Date]

---

## Layer 1: Idea Architecture

How this person structures arguments and builds ideas.

**Primary pattern:** [e.g., "Accumulator -- stacks examples until pattern is self-evident, then names the principle" or "Declarer -- leads with the thesis, then defends it"]

**Topic introduction:** [How they pivot to new topics]

**Emphasis pattern:** [Repetition? Escalation? Analogy? Example-first?]

**Disagreement style:** [How they push back -- redirect, reframe, validate-then-counter?]

**Evidence:**
> [Direct quote showing the pattern]
> [Direct quote showing the pattern]

---

## Layer 2: Persuasion Patterns

How this person convinces others. (Omit if not relevant to the person's role.)

**Opening move:** [How they start a pitch/argument]

**Credibility proof:** [How they establish authority without bragging]

**Urgency creation:** [How they create FOMO or urgency]

**Closing pattern:** [How they move toward action/next steps]

**Objection handling:** [How they respond to pushback]

**Evidence:**
> [Direct quote showing the pattern]
> [Direct quote showing the pattern]

---

## Layer 3: Sentence Patterns

The mechanics of how their sentences work.

**Spoken sentence length:** [Short/medium/long, with cascade patterns]

**Written sentence length:** [Typically shorter than spoken -- specify]

**Connective tissue:** [How they link ideas -- conjunctions, transitions, hard jumps]

**Rhythm:** [Staccato? Flowing? Mixed? Describe the pulse]

**Front-loading vs. back-loading:** [Where the key word lands in a sentence]

**Paragraph style:** [Long paragraphs? Single-sentence paragraphs? White space usage?]

**Evidence:**
> [Spoken example showing rhythm]
> [Written example showing compression]

---

## Layer 4: Word Palette

### Signature Words (uniquely this person)
- [word] -- [when/how they use it, with quote]
- [word] -- [when/how they use it, with quote]

### Enthusiasm Markers
- [word/phrase] -- [intensity level]

### Hedging Patterns
- [word/phrase] -- [how they express uncertainty]

### Agreement Markers
- [word/phrase] -- [how they signal alignment]

### Spoken-Only Words (never appear in writing)
- [word] -- [context]

### Written-Only Patterns (never appear in speech)
- [word/pattern] -- [context]

### Metaphor Library (reusable analogies they deploy repeatedly)
- **[Name of metaphor]:** [Description and typical deployment context]
  > [Direct quote]

---

## Layer 5: Register Dials

Patterns that shift by context. The Voice Agent adjusts these based on the output format.

| Dial | Low Setting (when) | High Setting (when) |
|------|-------------------|-------------------|
| **Formality** | [description, context] | [description, context] |
| **Profanity** | [description, context] | [description, context] |
| **Humor** | [description, context] | [description, context] |
| **Analogy depth** | [description, context] | [description, context] |
| **Enthusiasm expression** | [description, context] | [description, context] |

### Format-Specific Patterns

**Email:**
- Greeting patterns: [by warmth level]
- Sign-off patterns: [by formality level]
- Structure: [paragraph style, lists, spacing]
- Distinctive moves: [scheduling delegation, p.s. usage, etc.]

**Presentations:** [if slide voice was analyzed]
- Narrative arc: [default structure]
- Text density: [words per slide]
- Visual style: [colors, typography, imagery]

**LinkedIn/Social:** [if analyzed]
- Hook patterns
- Length
- Closing moves

**Long-form (proposals, articles):** [if analyzed]
- Structure
- Register shift from email
- Section patterns

---

## Layer 6: Anti-Patterns

Things this person NEVER does. The Voice Agent must scrub these from output.

- [Anti-pattern 1] -- [what to do instead]
- [Anti-pattern 2] -- [what to do instead]
- [Anti-pattern 3] -- [what to do instead]
- [etc. -- list as many as the analysis reveals]

---

## Voice-Specific Compression Table

For **person voices**: How this person's speech maps to their writing. Critical for the Voice Agent.

| Spoken Pattern | Written Equivalent |
|---------------|-------------------|
| [spoken habit] | [how it appears in writing, or "removed entirely"] |
| [spoken habit] | [written equivalent] |

For **publication/brand voices**: How generic business writing gets compressed in this voice. Maps common constructions to how this voice would express them.

| Generic Business Writing | This Voice |
|-------------------------|------------|
| [common construction] | [how this voice handles it, or "deleted entirely"] |
| [common construction] | [replacement pattern] |

Omit whichever table doesn't apply.

---

## Example Transformations

### Voice-neutral input:
> [A polished paragraph in generic professional prose]

### After applying this voice:
> [The same content, transformed to sound like this person]

### What changed:
[Explain the specific voice transformations applied]
```

---

## Notes for Voice Guide Authors

- Every claim needs a quote. "Uses short sentences" without an example is useless to the Voice Agent.
- The register dials section is where most of the detail lives. A voice guide that treats the voice as having one mode is incomplete.
- The compression table is the single most useful section for the Voice Agent. For person voices, it maps spoken patterns to written equivalents. For publication voices, it maps generic business writing to this voice's distinctive patterns. Both serve the same purpose: showing the Voice Agent what to transform and how.
- Anti-patterns matter as much as patterns. A voice that avoids em dashes, avoids corporate jargon, and avoids hedging pileups is as defined by its absences as its presences.
- Update the "Last updated" date whenever the guide is refreshed. Voice guides older than 6 months should be flagged for refresh.
- For publication voices, the header should include a **Voice type:** field ("Publication") and a **Primary author:** field if the publication has a consistent byline.
