# Voice Analyzer

Build a voice guide for any person by analyzing how they actually speak and write. The output is a structured voice profile saved to `voices/[name].md` that the rewriter's Voice Layer (Step 4) can apply.

This workflow requires substantial source material. Don't attempt to build a voice guide from a single email or a paragraph of writing. You need patterns, and patterns require volume.

---

## Step 1: Source Gathering

Ask the user what sources are available. Explain that more sources produce a better voice guide, and that different source types reveal different dimensions of voice.

### Source Types (ranked by richness)

| Source | What It Reveals | Minimum Useful Volume |
|--------|----------------|----------------------|
| **Meeting transcripts** | Raw idea formation, sentence rhythm, filler words, enthusiasm patterns, how they structure arguments in real time | 10+ transcripts, ideally across different contexts (1:1, sales, teaching, groups) |
| **Outbound emails** | Written compression of speech, formality calibration, greeting/signoff patterns, structural habits | 15+ substantive emails (5+ sentences each), across different recipients |
| **Presentations/slides** | Visual argument structure, information hierarchy, text density preferences, narrative arc patterns | 5+ decks, ideally across different purposes (pitch, workshop, keynote) |
| **Blog posts/articles** | Sustained written voice, paragraph-level rhythm, how they develop ideas at length | 5+ posts of 500+ words each |
| **Social media (LinkedIn, Twitter)** | Compressed voice, hook patterns, how they think about audience, casual vs. professional register | 20+ substantive posts (not just reshares) |
| **Journals/personal writing** | Unfiltered voice, emotional register, self-talk patterns | Any volume is valuable, but handle with care -- this is private |
| **Chat messages (Slack, Teams)** | Ultra-casual register, reaction patterns, how they collaborate async | 50+ messages in substantive threads |

Tell the user: "The more varied the sources, the better the voice guide. Transcripts from different contexts (1:1 vs. group, selling vs. teaching, casual vs. formal) are especially valuable because they reveal what stays constant across contexts -- that's the core voice."

### Organizing Sources

Ask the user to point you to:
1. **Transcript locations** -- file paths, Google Drive folders, or databases
2. **Email access** -- Gmail search queries, or exported emails
3. **Other writing** -- file paths, URLs, or pasted text
4. **Slides** -- file paths to HTML decks, PDFs, or PowerPoint files

For each source type, confirm the time range. Recent material (30-90 days) is best for capturing current voice, but older material can reveal stable patterns.

---

## Step 2: Dispatch Analysis Agents

Split sources by context type and dispatch parallel analysis agents. The key insight: a person's voice shifts depending on context, and those shifts ARE the voice. Analyzing across contexts reveals both the stable core and the context-sensitive dials.

### Recommended Agent Splits

**For transcripts**, split by relationship/context:
- **Intimate/partner conversations** (1:1 with co-founders, close collaborators) -- most authentic
- **Sales/BD calls** (prospects, pitches) -- persuasion mode
- **Client advisory** (teaching, consulting, delivering findings) -- expert mode
- **Public speaking/lectures** (keynotes, panels, workshops) -- performance mode
- **Casual networking** (catch-ups, intros, relationship maintenance) -- social mode

**For emails**, split by:
- **Substantive business emails** (follow-ups, proposals, check-ins)
- **Internal/partner emails** (to co-founders, team)

**For slides**, analyze as a single batch since visual patterns tend to be more consistent across contexts.

**For other sources** (blogs, social, journals), analyze as their own batch.

### Agent Prompt Template

Each analysis agent should receive this framework. Adapt the specific questions to the source type.

```
You are a voice analyst studying [PERSON]'s [speaking/writing/visual] patterns in [CONTEXT]. Your job is to deeply analyze HOW they communicate -- idea formation, sentence structures, word choices, rhythm, and distinctive habits.

[SOURCE-SPECIFIC INSTRUCTIONS: what files to read, what to focus on]

## ANALYSIS FRAMEWORK

Analyze across these dimensions. Use SPECIFIC QUOTES/EXAMPLES as evidence for every observation.

### 1. IDEA ARCHITECTURE
- How do they structure arguments? Lead with conclusion or build toward it?
- How do they introduce new topics or pivot?
- Do they use examples first then generalize, or assert then support?
- How do they handle disagreement or deliver difficult messages?
- Default emphasis pattern: repetition, escalation, analogy, example?

### 2. SENTENCE PATTERNS
- Average sentence length
- How they connect ideas (conjunctions, pauses, hard jumps)
- Active vs. passive voice patterns
- Front-loading vs. back-loading key information
- Rhythm: staccato, flowing, or mixed? What's the pulse?

### 3. PERSUASION PATTERNS (especially for sales/BD/pitch contexts)
- How do they open a pitch or argument?
- How do they establish credibility without bragging?
- How do they handle objections or skepticism?
- How do they create urgency without being pushy?
- How do they close -- move toward action or next steps?
- Persuasion mix: stories vs. data vs. demos vs. abstract theory?

### 4. WORD CHOICES & VOCABULARY
- Most frequently used words and phrases (especially distinctive ones)
- Default register (casual, professorial, analytical, enthusiastic)
- Jargon usage and domains the vocabulary draws from
- Favorite metaphors -- catalog with name, description, deployment context, and direct quote for each
- Words/phrases that are uniquely "theirs"

### 5. VERBAL/WRITTEN HABITS
- Filler words, hedging patterns, self-corrections
- How they start and end thoughts
- Humor: when, how, what kind?
- Energy patterns: what makes them speed up or slow down?
- Enthusiasm and agreement markers

### 6. CONTEXT-SPECIFIC PATTERNS
- How does this context differ from others?
- What's unique to this mode of communication?
- What stays the same regardless of context?

Provide your analysis with EXTENSIVE DIRECT QUOTES (at least 3-5 per category).
```

### For Slide Analysis

If the user has presentations to analyze, prompt them: "I can also analyze your slide decks to understand your visual argument style -- how you structure narratives across slides, your text density preferences, and how your verbal patterns translate into presentation design. This adds a 'slide voice' section to your guide. Want to include that?"

If yes, dispatch a slides analysis agent with this additional framework:

```
### SLIDE-SPECIFIC DIMENSIONS

1. NARRATIVE ARCHITECTURE: Default arc, opening/closing patterns, section transitions, typical slide count
2. SLIDE-LEVEL PATTERNS: Text density, header style, bullet patterns, data vs. text ratio, white space
3. VISUAL VOICE: Color, typography, image usage, templates, visual complexity
4. INFORMATION DESIGN: How they visualize frameworks, comparisons, timelines, pricing
5. SPOKEN-TO-VISUAL TRANSLATION: How verbal patterns become slide patterns
6. ANTI-PATTERNS: What they never do in slides
```

---

## Step 3: Synthesis

Once all analysis agents return, YOU (the Editor) synthesize their findings into a unified voice guide. This is the critical step -- you're not just concatenating reports. You're finding the patterns that appear across contexts and separating them from context-specific variations.

### Synthesis Process

1. **Identify the core voice** -- patterns that appear in 3+ contexts are the stable core. These go in the main sections of the voice guide.

2. **Map the dials** -- patterns that shift by context are register dials. Document what turns and when. For example: "profanity appears in partner conversations and close networking, never in client emails or presentations."

3. **Extract the word palette** -- compile the signature vocabulary across all sources. Separate into: always-use words, context-specific words, and never-use words.

4. **Document the anti-patterns** -- things the person consistently avoids across all contexts. These are as important as what they do.

5. **Note spoken-to-written compression** -- how does the person's speech compress into writing? What gets kept, what gets dropped? This is critical for the Voice Agent to know.

6. **Include the slide voice** (if analyzed) -- how the person designs presentations, as a distinct section.

### Output Format

Write the voice guide following the template in `references/voice-guide-template.md`. Save to `voices/[name].md`.

---

## Step 4: User Review

Present the voice guide to the user for review. Ask specifically:

1. "Does this sound like you? Read the example transformations and tell me if they feel right."
2. "Is anything missing? A phrase you use constantly that I didn't catch?"
3. "Is anything wrong? A pattern attributed to you that doesn't feel accurate?"
4. "Are there contexts I should weight more or less?"

Iterate until the user confirms the guide. Then save the final version.

---

## Maintenance

Voice guides should be refreshed every 3-6 months as a person's communication patterns evolve. The user can re-run the analyzer with fresh sources, or make targeted edits to the existing guide.

If the user says "update my voice" or "refresh my voice guide," re-run the analyzer with new recent sources and diff against the existing guide. Preserve stable patterns, update shifted ones.
