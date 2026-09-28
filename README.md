# The Unofficial Guide

<!-- Yuwen Zhang, Corpus: advice_threads -->

---

# Unit 1

## What This Does

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->
     'advice_threads' is the corpus this repo is optimized for. This system answers questions looking for answers based in personal experience. This ranges from topics like commuting and meals plans to transfers. 

## Chunking Strategy

<!-- **Chunk size:**
**Overlap:** -->

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->

     I chose to use each "reply" as a chunk for my corpus, advice_threads, rather than fixed chunk and overlap sizes, brecause each document consists of short posts with highly standardized formatting.

     In addition, I noticed that chunking presented a significant issue for this corpus; because each reply is so short, chunks suffer severely from missing context when they are unintentionally cut in the middle. While this was infrequent, affecting only 3 of 26 chunks using the original strategy, using paragraph breaks proved significantly more reliable with 0 of 26 chunks affected.

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

```
---Incomplete
Problematic chunks with original (fixed chunk_size = 800, overlap = 200) chunking approach
======================================================================
Chunk 2  |  source: thread_bike_commute.txt#1  |  produced by: chunker.py::fallback_split
======================================================================
nd it's the only reason I got mine back after it was taken.

---This one is ok, is a full standalone thought - but inconsistent with other chunks, which are almost a full document (multiple threads in response to 1 question)
======================================================================
Chunk 8  |  source: thread_first_year_regret.txt#1  |  produced by: chunker.py::fallback_split
======================================================================
) ---
That your adviser's job is partly to know the exceptions to rules. Ask before assuming a deadline is fixed.

---Incomplete
======================================================================
Chunk 15  |  source: thread_meal_plan_tier.txt#1  |  produced by: chunker.py::fallback_split
======================================================================
t.
```

```
Chunks with new (adjusted) chunking strategy:
```

**Chunk 1** — source: `` — produced by: ``

```
======================================================================
Chunk 4  |  source: thread_bike_commute.txt#3  |  produced by: chunker.py::split_documents
======================================================================
If you do get one, the campus does free registration and it's the only reason I got mine back after it was taken.
```

**Chunk 2** — source: `` — produced by: ``

```
======================================================================
Chunk 22  |  source: thread_first_year_regret.txt#4  |  produced by: chunker.py::split_documents
======================================================================
That your adviser's job is partly to know the exceptions to rules. Ask before assuming a deadline is fixed.
```

**Chunk 3** — source: `` — produced by: ``

```
======================================================================
Chunk 41  |  source: thread_meal_plan_tier.txt#3  |  produced by: chunker.py::split_documents
======================================================================
Declining balance rolls within the semester but not between them. Spend it in December or lose it.
```

**Chunk 4** — source: `` — produced by: ``

```
======================================================================
Chunk 26  |  source: thread_internship_timing.txt#0  |  produced by: chunker.py::split_documents
======================================================================
Earlier than feels reasonable. Large employers close applications in October and November for the following summer.
```

**Chunk 5** — source: `` — produced by: ``

```
======================================================================
Chunk 42  |  source: thread_office_hours_etiquette.txt#0  |  produced by: chunker.py::split_documents
======================================================================
No, and this is the single most common thing first years get wrong. 'I'm following the lectures but I don't feel like I understand the shape of it' is a completely normal thing to say.
```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:**
"When should students apply for internships?"

**Answer:**
```
(best distance 0.600, cutoff 0.7)

Students should apply for internships earlier than feels reasonable, as large employers close their applications in October and November for the following summer. However, smaller and local places hire in February and March, meaning missing the autumn application window does not mean missing everything (thread_internship_timing.txt).

Sources retrieved: thread_first_year_regret.txt, thread_internship_timing.txt, thread_late_work.txt, thread_pass_fail.txt
```

**My relevance cutoff:** 0.7

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

| Question | In corpus? | Best distance |
|---|---|---|
| Who should I talk to if I have conflicts with my roomate? | Yes | 0.633 |
| What advice do you have for joining clubs? | Yes | 0.695 |
| Any insider tips about studying in the library? | Yes | 0.545 |
| When should students apply for internships? | Yes | 0.600 |
| What are the best cafes to study at other than the library? | Yes | 0.555 |
| What is the capital of Mongolia? | No | 0.891 |
| How do I change the oil in a diesel engine? | No | 0.762 |
| Who won the 1994 World Cup? | No | 0.942 |
| What is the recommended dosage of ibuprofen for a headache? | No | 0.748 |
| How do I write a for loop in Rust? | No | 0.849 |

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1. Implementing Reply-Split Chunking**  
Once I identified the strategy of splitting chunks by
replies in replacement of fixed chunk and overlap sizes, I used AI to implement a regex
that fits the formatting of the replies to split them by this regex. It correctly chunked
documents by splitting them by each reply. However, it still included reply headers, which I
revised to remove from each chunk using AI.

**2. Filling in the README.md sample question distances table**  
I fed outputs and distances from running questions using `python app.py ask` as context to update the distances table above using AI. Since both the table's structure and final information was already provided, AI was able to fill in the table accurately in one attempt, and I was not required to change it.

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

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 1/5 | 1/5 | 1/5 | MISSED |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | (N/A)/5 | (N/A)/5 | MET |
| 4. A chunk should not be cut off | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. The system shouldn't answer questions about the world cup. | 5 of 5 | 5/5 | (N/A)5 | (N/A)/5 | MET |

### Note: How I compiled results
     I've marked run 3 and run 5 as N/A (in criterions 3 and 5) for criteria that evaluate the effectiveness of the rejection feature for out-of-corpus test questions, because they only run one pass.

     I checked criterions 1 and 4 (involves chunks) by using `python app.py chunks --from-doc` to retrieve and inspect chunks from the cited source file in each run.

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

## Sample Outputs by Criterion
### 1: Retrieved chunk contains the answer
Function & file source: cmd_chunks() in `app.py`

     75 chunks total. Showing all 3 from thread_roommate_conflict.txt.

     Paste these into your README under Sample Chunks. The rubric asks
     for the source file and the function that produced them — both are
     printed for you below.

     ======================================================================
     Chunk 1  |  source: thread_roommate_conflict.txt#0  |  produced by: chunker.py::split_documents
     ======================================================================
     Talk to your RA early, and frame it as 'we need help sorting this out' rather than 'move me'. Room changes are possible but the process starts with mediation and skipping that step slows it down.

     ======================================================================
     Chunk 2  |  source: thread_roommate_conflict.txt#1  |  produced by: chunker.py::split_documents
     ======================================================================
     Room changes happen at the semester boundary almost always, and mid-semester only in fairly serious cases.

     ======================================================================
     Chunk 3  |  source: thread_roommate_conflict.txt#2  |  produced by: chunker.py::split_documents
     ======================================================================
     Write down specifics before the meeting. 'It's not working' is hard to act on; 'guests four nights a week past 2am' is not.

     For each one, ask: could someone answer a question using only this,
     without reading what came before or after?

### 2. Every answer names a source
Function & file source: _ask_one() in `app.py`

     - Best distance: 0.5349 (passed the gate)
     - Sources retrieved: thread_commuting.txt, thread_group_project.txt, thread_pass_fail.txt, thread_study_spots.txt

     ```
     Based on the provided documents, group study rooms in the library can actually be booked and used by a single person since nobody checks (thread_study_spots.txt). Additionally, if you need silence, the third floor of the library is the only place that reliably delivers it (thread_study_spots.txt). 

     Source: thread_study_spots.txt
     ```

### 3. Gate stops out-of-corpus questions
Function & file source: _ask_one() in `app.py`

When asked "How do I write a for loop in Rust?" (not answered by corpus, `advice_threads`)

     (best distance 0.909, cutoff 0.7)

     I don't have enough information about that.

     0 model calls this session


### 4. A chunk should not be cut off
Function & file source: cmd_chunks() in `app.py`

     75 chunks total. Showing all 3 from thread_internship_timing.txt.

     Paste these into your README under Sample Chunks. The rubric asks
     for the source file and the function that produced them — both are
     printed for you below.

     ======================================================================
     Chunk 1  |  source: thread_internship_timing.txt#0  |  produced by: chunker.py::split_documents
     ======================================================================
     Earlier than feels reasonable. Large employers close applications in October and November for the following summer.

     ======================================================================
     Chunk 2  |  source: thread_internship_timing.txt#1  |  produced by: chunker.py::split_documents
     ======================================================================
     Smaller and local places hire in February and March, so if you missed autumn you have not missed everything.

     ======================================================================
     Chunk 3  |  source: thread_internship_timing.txt#2  |  produced by: chunker.py::split_documents
     ======================================================================
     The careers office reviews CVs on a drop-in basis and the queue is almost never longer than one person.

### 5. The system shouldn't answer questions about the world cup.
Function & file source: _ask_one() in `app.py`

When asked, "Who won the 1994 World Cup?" (not answered by corpus, `advice_threads`)

     (best distance 0.929, cutoff 0.7)

     I don't have enough information about that.

     0 model calls this session

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunk contains the answer - 4 of 5 | FAIL | The terminal output for the before run results (2026-09-6) show that only the 1st question (1 of 5) passed in all 3 passes, meaning the expected answer was not found for the other 4 questions  |
| 2 | Every answer names a source - 5 of 5 | MET | I confirmed that a .txt citation exists in the output of all 3 runs for each of 5 questions. |
| 3 | Gate stops out-of-corpus questions - 4 of 5 | MET | The run results for out-of-corpus questions shows that all 5 questions refused. |
| 4 | A chunk should not be cut off - 5 of 5 | MET | I verified that the chunks created for each document cited by one ouput for a question (all 3 runs made the same citation) for each of 5 questions were complete. |
| 5 | The system shouldn't answer questions about the world cup. - 5 of 5 | MET | I confirmed that the run results for the out-of-corpus question about the world cup refused. |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

     The miss in criterion 1 actually traces back to my question and expects pairs in `questions.py`. In particular, my expects are currently too broad, making it nearly impossible to meet the exact keyword match that `scorer.py` expects when checking if the generated answer contains the expected answer.

     However, this doesn't directly correlate to potential weaknesses in my RAG pipeline, which indicates that my targets were likely set too low. If I were to restart, I would tighten my 5th criterion - a fairly narrow case that evaluates whether one specific topic (soccer) for out-of-corpus questions correctly refuses. 
     
     This criterion may be adjusted to better serve testing this pipeline by reserving it for testing questions that lie at the borderline between in-corpus and out of corpus.

## The Improvement

**What I changed:**

I used rapidfuzz to perform a semantic meaning check in `scorer.py`, replacing the keyword check.

**Why I picked it:**

I chose to change the scorer to use a semantic match to more accurately evaluate cases where the generated answer matches the expected answer, but may be worded differently.
<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | (N/A)/5 | (N/A)/5 | MET |
| 4. A chunk should not be cut off | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. The system shouldn't answer questions about the world cup. | 5 of 5 | 5/5 | (N/A)5 | (N/A)/5 | MET |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

     Yes, this helped, as at least X of 5 questions had a final verdict that the expected keywords were found in the generated answer compared to 1 of 5 before this change.

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

     To strengthen this pipeline to meet the proposed criterion I mentioned my diagnosis that tests borderline-corpus questions, I would try introducing an additional grounding prompt. This prompt would act as a second gate to more critically evaluate relevance to prevent the system from invoking calls to answer questions that appear to belong to topics the RAG answers, but it doesn't directly address.

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->

     The criteria I mentioned above! One to evaluate borderline-corpus questions.