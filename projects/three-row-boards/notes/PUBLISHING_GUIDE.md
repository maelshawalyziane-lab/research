# How to publish the a(3,n) = n+2 paper

## 1. Where things stand (as of this check)

| Claim | Status |
|---|---|
| a(3,n) = n+2 for all n >= 4 | Lower bound: explicit construction, checked by computer for n <= 120. Upper bound: computer-assisted potential certificate (443 states), verified by two independent implementations. |
| Lemma on horizontal extent and locality | Hand-proved, and checked by enumeration. |
| a(2,n) = 2 ceil(n/2) | Hand-proved. Probably elementary and possibly known. |
| Rectangular table (m <= 5) | Computed by CP-SAT, proved optimal by the solver. Not proved by hand. |
| Literature novelty | Not found in the sources searched (see Section 2). **Not established.** |

Corrections made during this check:
- The earlier square-grid note said our lower bounds for n = 12–16 were not in OEIS. That was wrong. OEIS A271906 already gives a(12) >= 29, a(13) >= 32, a(14) >= 36 and a(15) >= 38. The note is corrected. Only n = 16 (value 40) is not listed.
- The earlier claim that the square-grid problem was "new" should not be repeated.

## 2. Literature check: what was searched and what it found

Searched: OEIS (A271906, A271907, A272626, A187452), arXiv full-text search, the Jánosik et al. survey (arXiv:2601.14465), the Károlyi–Solymosi preprint (arXiv:2607.22828), Shkredov–Solymosi (arXiv:2103.01645), PatternBoost (arXiv:2411.00566), Wu (arXiv:1605.00180), and web search.

Results:
- No source states a(3,n) or any result for a fixed number of rows.
- Square-grid results found: A271906 (values n <= 11, with lower bounds for 12–15), A271907 (no-isosceles variant), asymptotic bounds by Bloom and Pilatte, and the Károlyi–Solymosi lower bound.
- Related but different: A272626 and Wu (1605.00180) count isosceles triangles on rectangular boards. They do not address the subset problem.
- A 2026 preprint (arXiv:2610.04194) describes an "AI-assisted proof case study" on isosceles-free grids. It is a precedent for disclosing AI assistance in this area.

Not done:
- zbMATH could not be queried successfully. Run a search there through your library, using "isosceles", "right triangle", "grid", "rows" and "subset", and check the reviews.
- Google Scholar and MathSciNet full-text searches.
- Read the full Jánosik et al. survey (only the first section was read) and the reference lists of the three 2026 papers.

**Action:** do these before submitting. If any source contains a(3,n) or an equivalent statement, the paper must be reframed or dropped.

## 3. Before you submit (required)

1. **Expert check.** Send the manuscript to two or three combinatorialists. Good sources: authors of the papers in Section 2 and colleagues in your department. Ask them specifically to (a) check the potential argument in Theorem 4 (the upper bound, with its telescoping step), and (b) say whether they know the result.
2. **Human-readable proof, if possible.** The upper bound currently depends on a finite certificate. Referees often ask for a human proof. If you can find a closed form for the potential, or a short argument, add it. If not, say clearly that the upper bound is computer-assisted (the manuscript already does).
3. **Authors.** The manuscript has a placeholder author line. Journals and arXiv require human authors who take responsibility for the content. An AI system cannot be an author. List the real authors and affiliations.
4. **AI disclosure.** Journals differ in their policies. Disclose the assistance in the manuscript (the "AI assistance" paragraph is a draft) and follow the target journal's wording.
5. **Reproducibility.** Upload the supplement folder (`code/`) to Zenodo or GitHub to get a DOI, and cite it in the paper. Its README lists the commands and the expected output. The certificate hash is in the paper.
6. **Title and abstract.** Keep "computer-assisted" in the abstract or title, so readers know the upper bound depends on a computer check.
7. **Clean up the paper.** Remove the date placeholder if you want a fixed date. Check the references: the Pilatte and Bloom citations are named in Károlyi–Solymosi and Jánosik et al., but a full bibliographic entry should be taken from the original source.

## 4. Where to post and submit

**Step 1: arXiv.** Post first to arXiv, primary category math.CO. Cross-list to cs.DM if you want. A first submission from a new account may need an endorsement, so check arXiv's current endorsement rules. arXiv gives a dated record, which helps if someone else publishes similar work.

**Step 2: journal.** Suitable venues, from best fit to more ambitious:

| Journal | Why it fits | Notes |
|---|---|---|
| Electronic Journal of Combinatorics | Accepts short papers and computer-assisted results with code. | Free to read, well-regarded in combinatorics. |
| Journal of Integer Sequences | Good for the computed table and exact values. | Strong fit for a separate short note on the rectangular values. |
| Integers | Short notes in combinatorics and number theory. | Accepts computational results. |
| Discrete Mathematics | Broader readership. | More likely to ask for more depth. |

Recommended plan: submit the main theorem (Sections 2–4 of the manuscript) to the Electronic Journal of Combinatorics or Discrete Mathematics. Submit the rectangular table and the two-row result as a separate short note to the Journal of Integer Sequences, or add them to OEIS as new sequences.

**Check the current journal policies yourself.** I did not verify these venues' current rules on computer-assisted proofs, AI disclosure, or page limits.

## 5. Likely referee objections and responses

| Objection | Response to prepare |
|---|---|
| "The upper bound is computer-assisted. Give a human proof." | The certificate is finite, and anyone can check it with the supplement. It was checked by two independent implementations. A closed form for the potential would be a stronger result, and we state this as open. |
| "This is known." | Describe the search in Section 2 precisely. If an expert knows a source, cite it and revise the novelty claim. |
| "The result is too small." | It is a complete determination of a(3,n) and a new method for narrow boards. It is a short note, and the paper should not claim more. |
| "Why not the square case?" | The square problem is open for n >= 12 (OEIS A271906). The method does not extend directly, since the state space grows with the number of rows. |
| "Is the lemma on horizontal extent correct?" | Yes. Lemma 1 has a short hand proof, and enumeration confirms it: 36 triangles fit in 3 rows, with maximum x-span 4 and maximum |p|, |q| = 2. |

## 6. Timeline (typical, not guaranteed)

- Week 1–2: literature check (Section 2) and expert feedback.
- Week 2–3: revise, add the human proof if found, post to arXiv.
- Months 1–6: journal review. Expect at least one round of revisions.

## 7. Files

- `paper/main.tex` and `main.pdf`: the manuscript.
- `code//`: code, certificate, audit scripts, README.
- `./paper.md`: the earlier square-grid note, corrected.
- `./rect_paper.md`: the rectangular-board note.
