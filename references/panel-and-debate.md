# Panel and Debate (Full tier only)

The panel and debate are the most rigorous, and most expensive, review this skill runs. They only run in the Full tier, which the user turns on explicitly ("full mode", "full rigor", "dial it to 11", "run a panel"). Never select them automatically.

Adapted from the panel and debate workflows in Every's compound-writing project (MIT license; see README credits). The reviewer roster below is this skill's own: each reviewer is one of the rewriter's existing lenses, so the panel stays consistent with the pipeline.

## The reviewers

| Reviewer | Lens | Reads with |
|---|---|---|
| **Strategist** | Is there one clear point? Is it concrete, surprising, and pitched at what the reader knows? | `pinker-clarity.md`, `heath-stickiness.md` |
| **Craftsman** | Sentence economy, rhythm, active verbs, needless words | `klinkenborg-sentences.md`, `strunk-white-elements.md` |
| **Scrub** | AI tells, including the structural ones: self-commentary, overcompletion, portable profundity | `anti-ai-checklist.md` |
| **Cold Reader** | The target reader's first read, in order: where they stumble, doubt, or drift | the active audience guide (Nudge check 1 in `critique-modes.md`) |
| **Skeptic** | The smart outsider who extends no goodwill: objections, unsupported claims, in-group shorthand | Nudge checks 2 and 3 in `critique-modes.md` |
| **Plain-English Reader** | A capable non-expert: jargon, undefined terms, steps that assume expertise | the audience guide's shared-vocabulary table |
| **Voice Keeper** | Only when a voice guide is active: does it sound like that person or publication? | the active voice guide |

## Panel

1. **Propose 4 to 6 reviewers** with a one-line reason each, tied to this draft, plus one line on who you're leaving out and why. Defaults: an argument or recommendation gets Strategist, Skeptic, Cold Reader, Craftsman. A technical explainer gets Cold Reader, Plain-English Reader, Craftsman, Strategist. A high-stakes, near-final piece adds Scrub and Voice Keeper. Wait for the user to confirm or adjust.
2. **Run the reviewers in parallel**, as separate sub-agents where available. Give each one the draft, the intake context (purpose, audience, format), the audience guide if any, and only its own reference files. Each returns findings in its own words: quoted passage, problem, suggested fix, and severity.
3. **Synthesize.** You (the Editor) combine the outputs into:
   - **Agreement:** issues two or more reviewers flagged, with who flagged them and the fix.
   - **Tensions:** places where reviewers disagree (Craftsman says cut the anecdote; Cold Reader says it's the only thing that made the point real). Quote the passage, show both positions, and name what's at stake for this piece's purpose.
   - **Single-reviewer insights** worth keeping.
   - **Priorities:** a numbered list, most important first.
   - **The hard question:** the one question about the piece that several reviewers circled without asking outright.
4. **Decision point.** The user picks which priorities to act on, by number, and resolves tensions (or asks for a debate on them). Then run the pipeline with those decisions as instructions.

If a reviewer fails to run, say which one and continue with the rest.

## Debate (offered only on tensions)

After the synthesis, if there are real tensions, offer a debate on them. Don't run it unless the user says yes. It costs more time and tokens than the panel.

1. **Challenge.** For each tension, show each side the other's argument and the passage in question.
2. **Respond.** Each reviewer, staying in its lens, either concedes ("the anecdote does carry the point; withdrawn"), holds ("still too slow for an email"), or proposes a compromise ("keep the first sentence of the anecdote, cut the rest").
3. **Resolve.** Mark each tension *resolved* (agreement or accepted compromise), *stalemate* (a real difference in values), or *proposal on the table*. Stop after three rounds at most.
4. **Hand back.** Stalemates and open proposals go to the user to decide. The debate informs the writer's call; it never makes it.

## After the rewrite

In the Full tier, once the pipeline has produced the final draft, run the Cold Reader and Skeptic once more on the output (in parallel). Report anything that still stops the read before delivering, then run the Final Check.
