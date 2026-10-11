[GitHub repository: chinmaymk/indus-script](https://github.com/chinmaymk/indus-script)

# 840 million tokens trying to decipher the Indus script

Chinmay Kulkarni · October 11, 2026

I wanted to see whether Astra could decipher the Indus script on its own. So I gave it the goal, let it choose how to attack the problem, and kept it running across multiple usage resets.

For about two weeks, it struggled. There was plenty of work happening: sources collected, scripts written, patterns tested. We still had no verified reading. Eventually, I brought in Opus and Sol to help.

Across the retained research record, we used about **840 million tokens**, including automatic review. We still haven’t deciphered the script.

That gap between the amount of work and the result became the most interesting part of the experiment.

## Giving it the problem

The Indus script survives in short inscriptions on seals, tablets, pottery and other objects. We lack an accepted bilingual inscription and a securely identified underlying language. There is no answer key against which an agent can check its translation. [Background on the decipherment problem](https://www.harappa.com/answers/why-has-language-harappa-not-been-deciphered).

My [original prompt](https://github.com/chinmaymk/indus-script/blob/main/data/raw/blog-research-instructions-oct11-v1.json) was broad:

> /goal decipher indus script, come up with reasonable conclusions that fit for all the symbols, use any additional data as you see fit, persist proof and scripts you may need for processing the data

The next day, I asked it to keep a research log of “all the things you tried and their results.” I wanted an engineering log I could inspect: the approach, its assumptions, what ran, what failed, and why we should continue.

The [log](https://github.com/chinmaymk/indus-script/blob/main/docs/RESEARCH_LOG.md) grew alongside the code and data. Failed hypotheses and critiques stayed in the repository. This was useful, but it also exposed how easy it was to keep producing work without getting closer to a reading.

## Where it got stuck

We found structure. Some signs preferred particular positions; neighboring signs helped predict what came next. But those patterns didn’t tell us what the signs meant.

Imagine labelling a sign “grain,” then changing its label to “king.” Its frequency and neighbors stay exactly the same. A sequence model cannot choose between those meanings using those statistics alone. We saved an [executable demonstration](https://github.com/chinmaymk/indus-script/blob/main/docs/IDENTIFIABILITY.md) of this limitation.

Repeated strokes offered a more concrete lead: perhaps they represented quantities. Comparisons between tablet faces produced neat equations and a possible conversion ratio. But the equations assumed those faces recorded equal quantities. We had no independent evidence establishing that premise, and another example conflicted with the proposed conversion. [The conditional result and conflict](https://github.com/chinmaymk/indus-script/blob/main/docs/CONVERGENCE.md) remain in the record.

An agent can get the algebra right while the historical assumption underneath it remains unproved.

Meanwhile, checking another catalogue page or reconciling another transcription always offered a clear task. That work mattered, but I began pushing on a different question: what would the next task let us decide?

## Bringing in other models

After Astra’s roughly two-week solo attempt, I brought in Opus and Sol. I asked for Claude Code second opinions and, later, a faster route to decipherment. The subsequent findings belong to that broader collaboration.

Opus’s critique pushed on the equality assumption, duplicate observations, and the risk of selecting examples after seeing their contents. Re-transcribing something we had already examined did not make it an unseen test. We also checked the critique itself; some recommendations assumed more than the evidence supported. [The review and our response](https://github.com/chinmaymk/indus-script/blob/main/docs/CLAUDE_SECOND_OPINION.md) are saved.

One suggestion led to a test of associations between signs and animal motifs on seals. We fixed the rules before running it. Across 716 distinct text families and roughly 10 thousand shuffles, **no candidate passed the threshold**. We closed that experiment. [Full result](https://github.com/chinmaymk/indus-script/blob/main/docs/MOTIF_FAST_ROUTE.md).

I also tightened the working instructions: keep one next action, state what evidence it should produce, and give it a finite stopping rule. Keep the full history in the log and only the current decision in a compact active state. Reopening a failed route required new evidence or a specific defect in the earlier test.

## What 840 million tokens bought us

The retained records from September 22 through October 11, 2026 contain about **822 million research-model tokens**: Astra accounted for 817 million, including its subagents; Sol for 3.4 million; and Opus for 1.4 million. Automatic review added another 17 million, bringing the headline total to about 840 million.

Most of that total—about **811 million tokens**—was cached input being read again across calls. Recorded output, including reasoning, was about **3.3 million tokens**. The headline counts input and output; it doesn’t measure dollar cost or subscription-limit usage. The [exact audit](https://github.com/chinmaymk/indus-script/blob/main/docs/RESEARCH_TOKEN_USAGE.md) preserves the totals, cutoff and counting method, and excludes writing this post.

The models helped build a reproducible investigation, expose assumptions, and rule out particular leads. We still have no established sound or meaning for any of the 417 signs this project tracks.

I started by asking whether an agent could lead a decipherment. I ended up spending more time judging its research choices: which observation could distinguish two explanations, and when should a route stop?

More token budget kept the investigation moving. Finding evidence that could support a reading remained the hard part. The repository is open, the failures are recorded, and the goal is still decipherment.
