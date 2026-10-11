# Trying to decipher the Indus script with AI

Chinmay Kulkarni · October 11, 2026

I’ve been using Codex and Claude Code to work on a question that has resisted generations of researchers: can we decipher the Indus script?

We haven’t deciphered it. We haven’t established a sound or meaning for any of the 417 signs in the catalogue this project tracks. But the attempt has taught me something useful about doing research with AI: an agent can make an investigation move much faster while leaving its central uncertainty untouched.

The interesting part has been working out which experiments could actually reduce that uncertainty, and getting the agents to stop when an experiment has answered its question.

## The problem we started with

The Indus civilization left short inscriptions on seals, tablets, pottery and other objects. Many seals combine a small sequence of signs with an animal image. The surviving texts average roughly five signs. We lack an accepted bilingual inscription and a securely identified underlying language. Those are substantial obstacles when even a long text gives you very little material to work with. [Researchers discussing the decipherment problem](https://www.harappa.com/answers/why-has-language-harappa-not-been-deciphered) describe these gaps in more detail.

There is a long history of computational work on the script. Researchers have studied sign frequencies, preferred positions, recurring sequences and statistical similarities to language. Rajesh Rao’s [2010 overview](https://www.harappa.com/sites/default/files/pdf/indus-script-analysis.pdf) is a useful introduction. Our use of AI builds on that kind of investigation; the existence of recurring structure is already an established research question with a substantial literature.

I approached this as an engineering project. Make the evidence inspectable. Write down assumptions. Build tests that can fail. Keep enough provenance that a promising result can be traced back to the objects and catalogues behind it.

The [repository](https://github.com/chinmaymk/indus-script) contains the sources, scripts, results and failed hypotheses. The goal remains reading the inscriptions. A larger repository does not tell us whether we are closer to that goal.

## Getting the data right

One early complication was deciding what our sign IDs actually represented.

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

Once I understood that gap, “the model found a pattern” became a much less satisfying endpoint. The next question was what observation could distinguish the competing interpretations.

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

## Asking Claude to criticize the route

I brought in Claude Code to review the method and help identify a faster experiment.

Its useful criticism concerned the equality assumption, duplicates and prior exposure to the data. Selecting apparently equivalent examples after seeing their stroke counts risks making the hypothesis impossible to falsify. Re-transcribing an inscription we have already examined does not turn it into an unseen test case.

We also checked Claude’s recommendations. Some suggestions depended on claims its review had not established, or gave structural evidence more semantic weight than it could carry. The [review record](https://github.com/chinmaymk/indus-script/blob/main/docs/CLAUDE_SECOND_OPINION.md) separates the criticism we accepted from the claims we did not adopt.

One recommendation led to a bounded experiment using existing data: look for associations between inscription signs and the animal motifs recorded on seals.

We fixed the selection and analysis rules before computing the new associations. The screen used a restricted Mohenjo-daro export subset, treated each distinct complete text as one text family, and shuffled motif assignments within exact inscription lengths. Because we examined many sign–motif pairs, the comparison accounted for the strongest result across the whole screen.

The experiment included 716 eligible text families and 748 sign–motif pairs. After 9,999 shuffles, the global permutation p-value was 0.7609. Zero pairs passed the frozen selection threshold. There was no candidate to take into the planned follow-up checks. [The complete result is saved here](https://github.com/chinmaymk/indus-script/blob/main/docs/MOTIF_FAST_ROUTE.md).

That result does not prove animal motifs carry no information. It says this particular screen supplied no selected lead. We closed it without changing the bins, features or threshold to obtain a more attractive outcome.

## What AI helped with

AI helped turn proposed explanations into explicit assumptions, code and checks. It helped review transcription decisions, find inconsistencies between representations, and criticize an experiment before we spent more time on it.

It also made continuing cheap. There was always another statistic to calculate or another plausible interpretation to explore. That is a real difficulty when the question has no easy success criterion and the data can support many stories.

We started keeping one next action, the evidence it should produce, and a finite stopping rule. If an experiment needed repeated combinations absent from the selected sample, more simulation could not supply them. If a screen selected no candidates, its downstream work stopped. If a proposed meaning could survive every failure by inventing another unit or category, it needed a more restrictive prediction.

Those rules helped me decide when another agent run would be useful.

The investigation has left us with structural constraints and some testable hypotheses. Reading the signs still requires a connection to something independently known: a quantity, an archaeological context, a linguistic constraint, or perhaps a bilingual text. A useful next result would make a prediction about evidence we did not use to construct the hypothesis.

I still want to decipher the script. For now, the most valuable contribution of the agents has been helping us state what would have to be true for a proposed reading to deserve belief—and recognize when our evidence cannot yet decide.
