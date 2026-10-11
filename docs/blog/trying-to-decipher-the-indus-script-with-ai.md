# Asking Astra to decipher the Indus script

Chinmay Kulkarni · October 11, 2026

I started this project to see whether Astra could decipher the Indus script on its own.

For about two weeks, I let Astra work on the problem. It struggled to make decisive progress. Eventually, I brought in Opus and Sol to help.

I kept it going across multiple usage resets, giving it more token budget to continue working. This became a sustained attempt to see how far it could get.

We still haven’t deciphered it. We haven’t established a sound or meaning for any of the 417 signs in the catalogue this project tracks.

The project began as a test of autonomous research. After two weeks, I intervened and it became a collaboration across models.

What interested me was whether an agent could choose productive research directions, recognize when a hypothesis had failed, and find evidence that would support an actual reading. This is an account of how that attempt went.

## The problem we started with

The Indus civilization left short inscriptions on seals, tablets, pottery and other objects. Many seals combine a small sequence of signs with an animal image. The surviving texts average roughly five signs. We lack an accepted bilingual inscription and a securely identified underlying language. Those are substantial obstacles when even a long text gives you very little material to work with. [Researchers discussing the decipherment problem](https://www.harappa.com/answers/why-has-language-harappa-not-been-deciphered) describe these gaps in more detail.

There is a long history of computational work on the script. Researchers have studied sign frequencies, preferred positions, recurring sequences and statistical similarities to language. Rajesh Rao’s [2010 overview](https://www.harappa.com/sites/default/files/pdf/indus-script-analysis.pdf) is a useful introduction. Our use of AI builds on that kind of investigation; the existence of recurring structure is already an established research question with a substantial literature.

For an autonomous agent, this problem requires more than generating a plausible translation. It has to work out which sources to trust, which assumptions need testing, and which experiment could distinguish competing explanations. There is no simple answer checker waiting at the end.

The [repository](https://github.com/chinmaymk/indus-script) contains the sources, scripts, results and failed hypotheses. The goal remains reading the inscriptions. A larger repository does not tell us whether we are closer to that goal.

## Two weeks with Astra

There were sources to inspect, patterns to measure and hypotheses to test. Each could yield a concrete output. The harder task was choosing work that could connect an inscription to an ancient sound or meaning. Astra could keep investigating while that connection remained missing.

That was the difficulty I encountered over those two weeks. Bringing in Opus and Sol was my intervention. The findings below come from the project as a whole; some of the work continued after the solo attempt.

## How many tokens we used

The retained usage records contain **821,734,966 input and output tokens across the research models**, through October 11, 2026 at 1:23 a.m. Pacific time. Including automatic review overhead brings the recorded total to **838,914,762**.

| Model or activity | Input including cache | Output including reasoning | Total |
| --- | ---: | ---: | ---: |
| Astra including its subagents | 813,809,360 | 3,158,840 | 816,968,200 |
| Sol including its subagent | 3,347,915 | 17,844 | 3,365,759 |
| Opus | 1,352,535 | 38,497 | 1,391,032 |
| Fable auxiliary review | 6,421 | 3,554 | 9,975 |
| Research models subtotal | 818,516,231 | 3,218,735 | 821,734,966 |
| Automatic review overhead | 17,139,879 | 39,917 | 17,179,796 |
| Recorded research total | 835,656,110 | 3,258,652 | 838,914,762 |

These counts cover the retained research record from September 22 through that cutoff, including the later help from other models. They exclude writing this post and doing the token audit. Astra’s count includes 44 subagent histories using the same model.

The cache component is substantial: **810,960,583 tokens** in the overall total are cached input reads. Context reused across successive calls still appears in the usage counters. The recorded output is **3,258,652 tokens**, including reasoning. That distinction matters when interpreting a headline number approaching a billion tokens. These counts also do not measure dollar cost or subscription usage-limit units. [OpenAI](https://developers.openai.com/api/docs/guides/agents-api/observability) and [Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) document how their input and cache counters work.

The tally uses individual OpenAI response records and deduplicated Claude messages, plus separate saved CLI usage summaries. It is exact for those retained records at the cutoff; it cannot establish usage missing from the logs. The [audit and reproduction details](https://github.com/chinmaymk/indus-script/blob/main/docs/RESEARCH_TOKEN_USAGE.md) are saved alongside the research.

## Getting the data right

One complication was deciding what our sign IDs actually represented.

Different catalogues classify the same graphics differently. A unit in one transcription can correspond to two tokens in another. Similar looking forms can be distinguished in one system and merged in another. Joining datasets by apparent resemblance can quietly change the thing being measured.

We also checked a small batch directly against printed catalogue pages. That batch eventually covered six consecutive pages: 198 lines and 949 assigned sign positions, representing 173 sign types. We preserved missing spans and the source’s doubtful readings. Those numbers describe a checked slice of a catalogue, not a complete corpus.

Two AI review passes agreeing on a printed sign helps establish transcription fidelity. They may still inherit the same error from the printed source. Checking the original object or its photograph answers a different question. The [transcription record](https://github.com/chinmaymk/indus-script/blob/main/docs/M77_VERIFIED_CORPUS.md) keeps those distinctions explicit.

Duplicates matter too. Several records may refer to the same artifact, and different artifacts can carry the same inscription. Counting every record as an independent observation can make a pattern appear much stronger than it is. We grouped known artifact relationships and kept exact text duplicates together where the experiment required it.

This work was necessary. It also became an easy place to keep spending time: another page, another crosswalk, another validation. Eventually we had to ask what decision the next batch would enable.

## The gap between a pattern and a reading

Our sequence models found useful structure. Knowing neighboring signs improved prediction beyond knowing only sign frequencies or positions. Some signs strongly preferred particular parts of an inscription.

That still leaves the meanings open.

Imagine assigning every sign an arbitrary label. Give one the label “grain,” another “king,” and another “river.” Then replace those labels with a completely different set, preserving the one-to-one mapping.

Every sign count and pair count stays the same. The same sequence model, with its parameters relabelled, gives the same probabilities. Entropy and mutual information stay the same too. These scores have no way to tell which set of labels describes the ancient meanings.

We wrote this down as a [precise limitation](https://github.com/chinmaymk/indus-script/blob/main/docs/IDENTIFIABILITY.md), with an executable example. It doesn’t establish that decipherment is impossible. It identifies information that these internal statistics cannot supply.

There is a related problem with calling any structured sequence “language.” Weather icons can have regular ordering and predictable neighbors. So can administrative categories. A successful sequence model gives us constraints a reading should explain; identifying spoken-language writing requires more evidence.

For the autonomy experiment, this gap was especially important. Finding another pattern could be a reasonable local step while leaving the decipherment problem unresolved. Choosing an observation that could distinguish the competing interpretations required a different research decision.

## A numeral hypothesis and its hidden assumption

Repeated strokes seemed like a tractable place to start. Counting marks is easier than assigning sounds to an unfamiliar sign. Some inscriptions retain a main sequence while nearby stroke counts vary, which makes a quantity interpretation worth investigating.

Comparisons between tablet faces produced conditional equations. Let `a`, `b` and `c` represent the contributions of particular stroke forms in their respective sign contexts. If the compared faces record equal quantities, the selected examples give:

```text
3a = 2b
3a = 3c
```

Under those assumptions, `c / b = 2 / 3`.

The algebra works. The claim that the faces represent equal quantities is the difficult part. Shared placement or similar inscriptions do not establish that equality. A further catalogue example, H-1923, conflicts with the same fixed conversion assumptions. Leaving it out shows what happens in a sensitivity analysis; it does not justify discarding it.

The [numeral synthesis](https://github.com/chinmaymk/indus-script/blob/main/docs/CONVERGENCE.md) preserves the conditional result and the conflict. We have no independently authenticated quantity pair that establishes the proposed conversion.

This was a useful failure mode to encounter. An agent can solve the equations, verify them with a second method, and produce a tidy explanation. All that work remains conditional on the historical premise that created the equations.

## Bringing in Opus and Sol

One documented part of the later collaboration was asking Opus, through Claude Code, to review the method and help identify a faster experiment.

Its useful criticism concerned the equality assumption, duplicates and prior exposure to the data. Selecting apparently equivalent examples after seeing their stroke counts risks making the hypothesis impossible to falsify. Re-transcribing an inscription we have already examined does not turn it into an unseen test case.

We also checked Claude’s recommendations. Some suggestions depended on claims its review had not established, or gave structural evidence more semantic weight than it could carry. The [review record](https://github.com/chinmaymk/indus-script/blob/main/docs/CLAUDE_SECOND_OPINION.md) separates the criticism we accepted from the claims we did not adopt.

One recommendation led to a bounded experiment using existing data: look for associations between inscription signs and the animal motifs recorded on seals.

We fixed the selection and analysis rules before computing the new associations. The screen used a restricted Mohenjo-daro export subset, treated each distinct complete text as one text family, and shuffled motif assignments within exact inscription lengths. Because we examined many sign–motif pairs, the comparison accounted for the strongest result across the whole screen.

The experiment included 716 eligible text families and 748 sign–motif pairs. After 9,999 shuffles, the global permutation p-value was 0.7609. Zero pairs passed the frozen selection threshold. There was no candidate to take into the planned follow-up checks. [The complete result is saved here](https://github.com/chinmaymk/indus-script/blob/main/docs/MOTIF_FAST_ROUTE.md).

That result does not prove animal motifs carry no information. It says this particular screen supplied no selected lead. We closed it without changing the bins, features or threshold to obtain a more attractive outcome.

## What the autonomy experiment showed

Across the project, the models helped turn proposed explanations into explicit assumptions, code and checks. They helped review transcription decisions, find inconsistencies between representations, and criticize experiments.

Working with agents also made continuing cheap. There was always another statistic to calculate or another plausible interpretation to explore. That is a real difficulty when the question has no easy success criterion and the data can support many stories.

We started keeping one next action, the evidence it should produce, and a finite stopping rule. If an experiment needed repeated combinations absent from the selected sample, more simulation could not supply them. If a screen selected no candidates, its downstream work stopped. If a proposed meaning could survive every failure by inventing another unit or category, it needed a more restrictive prediction.

The later work happened with additional models and explicit constraints on continuing. That context matters when judging the original test of autonomy.

The investigation has left us with structural constraints and some testable hypotheses. Reading the signs still requires a connection to something independently known: a quantity, an archaeological context, a linguistic constraint, or perhaps a bilingual text. A useful next result would make a prediction about evidence we did not use to construct the hypothesis.

Astra did not decipher the script during its two-week attempt, and bringing in Opus and Sol has not yet produced a verified reading either. This experience made me pay closer attention to the evidence an agent obtains and the research decisions it makes. The volume of work is much easier to see.

I still want to decipher the script. I also want to understand what it would take for an agent to lead that investigation successfully. At the moment, both questions remain open.
