# The Unofficial Guide

<!-- Replace this line with your name and which corpus you picked. -->

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->

This project answers questions about the `campus_life` corpus, which contains
short administrative notes, course information, dining details, and housing
advice. It retrieves the most relevant document chunks, refuses questions that
fall outside the corpus, and asks the model to answer only from the retrieved
text. Answers name the source document so the underlying fact can be checked.

## Chunking Strategy

**Chunk size:**
**Overlap:**

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

**Chunk 1** — source: `admin_add_drop_deadline.txt#0` — produced by: `chunker.py::split_documents`

```
On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.
```

**Chunk 2** — source: `course_cs_340_exams.txt#1` — produced by: `chunker.py::split_documents`

```
Start the term project in week three, not week eight; everyone learns this the hard way.
```

**Chunk 3** — source: `course_phys_130_workload.txt#0` — produced by: `chunker.py::split_documents`

```
Workload for PHYS 130 Mechanics

People keep asking so: 7 hours a week, plus 3 on lab weeks. That's real time, not optimistic time.
```

**Chunk 4** — source: `dining_verrill_street_grill_followup.txt#1` — produced by: `chunker.py::split_documents`

```
Also worth saying: one register, so the queue is a single line no matter how busy. Nobody tells you this at orientation.
```

**Chunk 5** — source: `housing_morrow_house.txt#1` — produced by: `chunker.py::split_documents`

```
The good: cheapest housing tier by about $900 a year, and the singles are real singles.
```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:**

How much printing credit does each student receive per semester?

**Answer:**

Each student receives $30 of printing credit per semester, which is roughly
600 black-and-white pages. Colour printing costs eight times as much per page.

**Source:** `admin_printing_quota.txt`

```
```

**My relevance cutoff:**

I kept the cutoff at **0.6**. The five in-corpus questions had best distances
from 0.2037 to 0.3719, while the five out-of-scope questions ranged from
0.7873 to 0.9228, leaving a clear gap between 0.3719 and 0.7873. A lower
cutoff could refuse a real question such as printing, while a higher cutoff
would admit more unrelated questions and risk unsupported answers.

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

| Question | In corpus? | Best distance |
|---|---|---|
| How are juniors and seniors prioritized in the housing lottery? | Yes | 0.2050 |
| What is the latest week when I can declare a course pass/fail? | Yes | 0.2326 |
| How much printing credit does each student receive per semester? | Yes | 0.3719 |
| What happens to my GPA if I withdraw from a course by the deadline? | Yes | 0.3525 |
| Do dining dollars roll over from spring to the following autumn? | Yes | 0.2037 |
| What is the capital of Mongolia? | No | 0.7873 |
| How do I change the oil in a diesel engine? | No | 0.9228 |
| Who won the 1994 World Cup? | No | 0.8474 |
| What is the recommended dosage of ibuprofen for a headache? | No | 0.8243 |
| How do I write a for loop in Rust? | No | 0.8768 |

## How I Used AI

<!-- Specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.**

I asked AI, "Could someone else check each of these five acceptance criteria
without asking what I meant?" It pointed out that the first three criteria
needed corpus-specific reasons and that the chunk and citation criteria needed
observable targets, so I added those explanations and measurable targets to
`criteria.md`.

**2.**

I asked AI to inspect the starter's 88-document, 88-chunk baseline and suggest a
strategy that would preserve complete thoughts in `campus_life`. Its first
paragraph-only version created heading-only chunks and grew the count to 271,
so I changed `chunker.py` to join short headings to the paragraph they
introduce; the final index produced 183 chunks.

**3.**

During Unit 2, I asked Copilot why the withdrawal question failed in every
before run even though the answer named the right fact and source. It compared
the expected phrase in `questions.py` with `scorer.py::judge` and found that the
scorer required the exact text `doesn't affect GPA`, while the answer said
`doesn't affect your GPA`. I changed the scorer to check retrieved chunks
instead; the after run then measured 5 of 5 for all five questions. That fixed
the measurement, not retrieval itself, so I reported the distinction in the
results.

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 4 of 5 | 4 of 5 | 4 of 5 | MET |
| 2. Every answer names a source | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 4. Sampled chunks contain complete thoughts | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 5. Cited source contains the expected fact | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |

**Evidence and measurement notes**

- **Criterion 1:** `results/run_2026-09-23_2129.md`, produced by
     `run_eval.py::main`, records 4 of 5 answers as passing in each run. For
     example, the withdrawal answer was: “Withdrawing puts a W on the transcript
     that doesn't affect your GPA (admin_withdrawal_deadline.txt).” The scorer
     checks for the exact expected substring `doesn't affect GPA`, so it marks
     this correct fact as a failure because the answer inserts “your.” Thus 4 of
     5 is the recorded answer-match result; the log does not independently expose
     retrieved chunk text for a direct chunk-content check.
- **Criterion 2:** The same log's `run_eval.py::main` real outputs name sources
     for all five questions in all three runs. Representative exact output:
     “You can declare a course pass/fail as late as week eight, after you've seen
     your midterm (admin_pass_fail_option.txt).”
- **Criterion 3:** `run_eval.py::check_out_of_scope` reports “Refused 5 of 5”
     at cutoff 0.6 in the same log. Its five distances are 0.787, 0.923, 0.847,
     0.824, and 0.877, all above the cutoff. The check is deterministic, so the
     same 5 of 5 is reported in each run column.
- **Criterion 4:** I manually checked the five actual chunks printed by
     `app.py chunks -n 5`, produced by `chunker.py::split_documents` and pasted
     above under “Sample Chunks.” All five read as complete thoughts, so this
     one-time sample check is repeated in each column; these are not three new
     chunking runs.
- **Criterion 5:** I checked each named source against its expected fact in
     `questions.py`. The generated answers and citations in
     `results/run_2026-09-23_2129.md` include: “accumulated credit hours first”
     (`admin_housing_lottery.txt`); “week eight” (`admin_pass_fail_option.txt`);
     “$30” (`admin_printing_quota.txt`); “doesn't affect your GPA”
     (`admin_withdrawal_deadline.txt`); and “left in May disappears”
     (`admin_dining_dollars.txt`). All five cited files contain the corresponding
     expected fact, so this manual source check is the same for each run.

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunks contain the answer | MET | The recorded score was 4 of 5 in each run, meeting the 4-of-5 target. This score comes from matching generated answers, not directly inspecting the retrieved chunk text. |
| 2 | Every answer names a source | MET | All five answers named a source in each of the three runs, meeting the 5-of-5 target every time. |
| 3 | Gate stops out-of-corpus questions | MET | The gate refused all five out-of-corpus questions, exceeding the 4-of-5 target. |
| 4 | Sampled chunks contain complete thoughts | MET | All five sampled chunks read as complete thoughts, meeting the 4-of-5 target. |
| 5 | Cited source contains the expected fact | MET | Each of the five cited source documents contained the expected fact recorded for its question, meeting the 5-of-5 target. |

## Diagnoses

No criterion was recorded as missed: each run met its target. The targets were
not all equally easy; criterion 1 only just met 4 of 5, while the other checks
scored 5 of 5. I cannot treat criterion 1 as a direct retrieval diagnosis,
though, because `scorer.py::judge` checks whether the generated answer contains
the expected phrase rather than whether a retrieved chunk contains the answer.
For the withdrawal question, `questions.py` expects `doesn't affect GPA`, but
the accurate answer says “doesn't affect your GPA,” so the literal substring
check marks it wrong. That is a measurement defect, not evidence that a
particular retrieval or generation stage failed. Since all five out-of-scope
questions were refused, I would tighten criterion 3 from 4 of 5 to 5 of 5 in a
future evaluation.

## The Improvement

**What I changed:**

I changed `scorer.py::judge` to search the expected phrase in the retrieved
chunks instead of requiring it to appear verbatim in the generated answer.

**Why I picked it:**

The diagnosis showed that the withdrawal answer was marked wrong only because
the answer inserted “your”; checking retrieved chunk text measures criterion 1
directly and avoids that wording-only false negative.

### Run Log — After

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 2. Every answer names a source | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 4. Sampled chunks contain complete thoughts | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 5. Cited source contains the expected fact | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |

The three-run outputs are in `results/run_2026-09-27_2128_after.md`, produced
by `run_eval.py::main`; the out-of-scope results are produced by
`run_eval.py::check_out_of_scope`. The gate refused 5 of 5. For example, the
withdrawal answer was: “Withdrawing puts a "W" on the transcript that does not
affect your GPA (admin_withdrawal_deadline.txt).” Its retrieved chunk contains
the expected fact. The five sampled chunks in Unit 1 are unchanged by this
scorer-only edit; all five remain complete thoughts.

**Did it help?**

It helped the measurement, not retrieval itself: criterion 1 now checks the
retrieved chunks directly and scored 5 of 5 in all three runs, up from the
before run's 4 of 5 answer-substring score. The withdrawal fact was present in
the retrieved chunk even though the generated answer used different wording.
The complete after run also met the source and citation targets in all three
runs, and the gate refused all five out-of-scope questions.

## What's Still Broken

No criterion was missed after the change: all five met their targets in the
after evaluation. Two limitations remain. First, `scorer.py::judge` checks for
the expected phrase literally in retrieved text, so a correct paraphrase in a
chunk could still be counted as a miss; I would replace that check with a
small, reviewed set of answer-bearing passages or a semantic check validated
against those passages. Second, whether a cited source supports the generated
answer was checked manually for these five questions, not automatically; I
would add citation-to-source checks and test more questions before relying on
it beyond this corpus. I stopped after the scorer change because the milestone
called for one measured improvement, the targets were met, and another change
would make it harder to tell what caused the results.

## What I'd Do Differently

I would rewrite criterion 1 to say: “For at least 4 of 5 questions, one of the
top five retrieved chunks contains the expected phrase listed for that
question in `questions.py`.” “Contains the answer” was too subjective to score
consistently; checking the retrieved text against a phrase chosen in advance
makes the retrieval test direct and repeatable.
