[GitHub repository: chinmaymk/indus-script](https://github.com/chinmaymk/indus-script)

# Asking Astra to decipher the Indus script: 891 million tokens later

Chinmay Kulkarni · October 17, 2026

![Three Indus seals with short inscriptions above animal motifs](https://media.githubusercontent.com/media/chinmaymk/indus-script/main/data/processed/blog-images/indus-seals.jpg)

*Short inscriptions above animal motifs. [Marshall (1931), vol. III, plate CV, seals 41–43](https://archive.org/download/in.gov.ignca.48270/page/n185.jpg).*

I gave Astra a goal: decipher the Indus script.

I let it choose its research directions, collect sources and write code. I kept it running across multiple usage resets. For about two weeks, it struggled to turn that work into a reading. Eventually, I brought in Opus and Sol to help.

At the October 17 audit cutoff, the research models, their subagents and automatic reviews together accounted for **about 891 million tokens**.

We still haven’t deciphered the script. None of the 417 signs this project tracks has an established sound or meaning.

The experiment became a study of how an agent chooses what to investigate, and how easily a research project can keep moving while its central question stays unanswered.

## Giving it the problem

The Indus script survives in short inscriptions on seals, tablets, pottery and other objects. We lack an accepted bilingual inscription and a securely identified underlying language. An agent proposing a translation has no simple answer key. [Background on the decipherment problem](https://www.harappa.com/answers/why-has-language-harappa-not-been-deciphered).

My [original instruction](https://github.com/chinmaymk/indus-script/blob/main/data/raw/blog-research-instructions-oct11-v1.json) was broad:

> /goal decipher indus script, come up with reasonable conclusions that fit for all the symbols, use any additional data as you see fit, persist proof and scripts you may need for processing the data

The next day, I asked it to log “all the things you tried and their results.” I wanted to follow the investigation like an engineering project: inspect the assumptions, reproduce the experiments and understand why an approach had failed.

The [research log](https://github.com/chinmaymk/indus-script/blob/main/docs/RESEARCH_LOG.md) grew alongside the code. Rejected hypotheses and critiques stayed in the repository. That made the work inspectable. It also made the accumulation of work very visible.

## Where it stalled

We found patterns. Some signs preferred particular positions, and neighboring signs helped predict what came next. Those regularities didn’t identify meanings.

Imagine labelling a sign “grain,” then changing its label to “king.” Its frequency and neighbors stay the same. Those statistics alone cannot choose between the two labels. We saved an [executable demonstration](https://github.com/chinmaymk/indus-script/blob/main/docs/IDENTIFIABILITY.md) of that limitation.

Repeated strokes offered a more concrete lead: perhaps they represented quantities. Comparisons between tablet faces produced equations and a possible conversion ratio. But the equations assumed the faces recorded equal quantities. That premise was unproved, and another example conflicted with the conversion. [The result remains conditional](https://github.com/chinmaymk/indus-script/blob/main/docs/CONVERGENCE.md).

![The two faces of tablet H-924 showing different arrangements of strokes](https://media.githubusercontent.com/media/chinmaymk/indus-script/main/data/processed/blog-images/h924-tablet-faces.png)

*Two faces of H-924. The stroke arrangements differ; equal quantities remain a hypothesis. [CISI II, p. 339 and our review](https://github.com/chinmaymk/indus-script/blob/main/docs/BALANCED_TABLET_PRIMARY_REVIEW.md).*

An agent can get the algebra right while the historical assumption underneath it remains unresolved.

Checking another catalogue page always offered a clear next task. I began pushing on what decision that task would actually enable.

## Bringing in criticism

After Astra’s roughly two-week solo attempt, I brought in Opus and Sol. I asked for Claude Code second opinions and a faster route to decipherment. The later findings belong to that broader collaboration.

Opus challenged the equality assumption, duplicate observations and the selection of examples after seeing their contents. Re-transcribing an inscription we had already examined did not make it an unseen test. We checked the criticism too; some recommendations assumed more than their evidence supported. [The review and response](https://github.com/chinmaymk/indus-script/blob/main/docs/CLAUDE_SECOND_OPINION.md) are saved.

One suggestion led to a test of associations between signs and animal motifs on seals. We fixed the rules before running it. Across 716 distinct text families and roughly 10 thousand shuffles, **no candidate passed the threshold**. We closed [that experiment](https://github.com/chinmaymk/indus-script/blob/main/docs/MOTIF_FAST_ROUTE.md).

Later work looked for clues in archaeological context. A [seal impression on a jar fragment at Salūt](https://github.com/chinmaymk/indus-script/blob/main/results/salut_impressed_jar_functional_gate_v1/decision.json) gave us an identifiable object, but no independently known contents or sound correspondence to connect to its signs. A concrete artifact still left the reading open.

![Salūt jar fragment and close-up beside a separate Harappa tablet](https://media.githubusercontent.com/media/chinmaymk/indus-script/main/data/processed/blog-images/salut-jar-impression.jpg)

*Salūt jar fragment and detail; the Harappa tablet at right is a separate comparison. [Frenez et al. (2016), fig. 10](https://www.harappa.com/sites/default/files/pdf/Bronze-Age-Indus-Connections.pdf).*

I tightened the working instructions: one next action, the evidence it should produce, and a finite stopping rule. A compact active state held the current decision; the log held the history. Reopening a failed route required new evidence or a specific defect in the earlier test.

## What the tokens bought us

The combined count is about **871 million research-model tokens** plus **20.5 million for automatic reviews**. Astra and its subagents account for 817 million; Sol for 52.5 million; Opus for 1.4 million; and Fable for 10 thousand.

About **861 million tokens were cached input reads** across successive calls. Recorded output, including reasoning, was about **3.5 million tokens**. The headline counts input and output, including cache reads; it doesn’t measure dollar cost or subscription-limit usage. The [exact audit](https://github.com/chinmaymk/indus-script/blob/main/docs/RESEARCH_TOKEN_USAGE_OCT17.md) preserves the counting method and excludes writing this post.

The models helped make assumptions explicit, expose conflicts and rule out particular leads. They have not supplied a verified reading.

I started by asking whether Astra could lead a decipherment. The hardest part turned out to be choosing evidence that could distinguish competing explanations. More budget kept the investigation running; finding that evidence remained difficult.

The repository is open, the failures are recorded, and the goal is still decipherment.
