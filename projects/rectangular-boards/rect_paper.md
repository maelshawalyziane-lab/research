# Right-Isosceles-Free Subsets of Rectangular Grids: Exact Values for Narrow Boards

## Abstract

Let a(m,n) be the largest number of points of an m×n grid (m rows, n columns of lattice points) that contain no three points forming a non-degenerate right isosceles triangle. We prove a closed form for two-row boards, a(2,n) = 2⌈n/2⌉ (Theorem 1), and give a short proof of the one-row case. We compute a(m,n) exactly by constraint programming for many small boards, including all m ≤ 4 with n ≤ 8 and m = 5 with n ≤ 12, and for m = 3 with n ≤ 18. For three-row boards we prove a(3,n) = n+2 for n ≥ 4 (computer-assisted upper bound; see theorem_a3n.md and the a3n project). We did not find a table of these rectangular values in OEIS, but the check was limited (see Section 5).

## 1. Definitions

Points are lattice points (x, y) with 0 ≤ x < n and 0 ≤ y < m. Three points form a right isosceles triangle if, for some vertex V and the other two vertices P and Q, the vectors P−V and Q−V are perpendicular and of equal nonzero length. A set is *admissible* if it contains no such triple. Write a(m,n) for the maximum size of an admissible subset.

## 2. Results

### Theorem 1 (two-row and one-row boards)

For all n ≥ 1:

  (i) a(1,n) = n,
  (ii) a(2,n) = 2⌈n/2⌉.

**Proof.**

(i) All points of a one-row board are collinear, and a non-degenerate triangle has three non-collinear vertices. So no triple is forbidden, and a(1,n) = n.

(ii) *Upper bound.* Split the columns into consecutive pairs {1,2}, {3,4}, … If n is odd, the last column is alone. Each pair of columns forms a 2×2 block of lattice points. Any three of the four corners of an axis-parallel unit square form a right isosceles triangle. So each 2×2 block contains at most two points of an admissible set. Each leftover single column (when n is odd) contains at most two points. Summing over the ⌈n/2⌉ blocks or columns gives |S| ≤ 2⌈n/2⌉.

*Lower bound.* Take S = {(x,y) : x even, 0 ≤ x < n, y ∈ {0,1}}. This has 2⌈n/2⌉ points. Suppose P, Q, R ∈ S form a right isosceles triangle with right angle at P. Write u = Q − P = (a,b) and R − P = (−b,a) (the rotation of u by 90°, up to sign; the other orientation is handled the same way). All points of S have even x-coordinate, so the x-differences a and −b are even. All points of S have y ∈ {0,1}, so b and a lie in {−1, 0, 1}. Hence a and b are even and lie in {−1,0,1}, so a = b = 0. Then Q = P, which is degenerate. So S is admissible. ∎

### Computed values

The table lists values a(m,n) with m rows and n columns, for n ≥ m (the cases computed). Every entry shown was reported OPTIMAL by the solver, so the upper and lower bounds met. Entries for the 3×19 and 3×20 boards, which the solver did not close, are discussed separately below.

| m \ n | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | | | | | | | | |
| 2 | | 2 | 4 | 4 | 6 | 6 | 8 | 8 | 10 | 10 | 12 | 12 | 14 | 14 | 16 | 16 |
| 3 | | | 4 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 |
| 4 | | | | 6 | 8 | 9 | 10 | 12 | 13 | 14 | 16 | 16 | 18 | 19 | | |
| 5 | | | | | 9 | 10 | 12 | 13 | 15 | 16 | 17 | 18 | | | | |

The m = 3 row continues: a(3,19) ≥ 21 and a(3,20) ≥ 22 were found but not proved optimal (the solver's upper bounds were 37 and 39). These are consistent with the conjecture below.

### Observations and conjecture

**Observation 2.** For 3×n boards with n ≥ 4 the computed values satisfy a(3,n) = n+2 for every n from 4 to 18.

**Proposition 3 (computer-checked construction).** For n ≡ 2 (mod 4), with n ≥ 6, the set

  S_n = {(x,y) : y ∈ {0,2}, x mod 4 ∈ {0,1}}

is admissible in the 3×n board and has n+2 points. We checked this by brute force for n = 6, 10, …, 30. We did not write a general proof.

**Theorem 4 (proved, see `theorem_a3n.md`).** For all n ≥ 4, a(3,n) = n+2. The upper bound is computer-assisted (a verified potential certificate on 443 states); the lower bound is an explicit construction valid for all n.

Both bounds for all n are now proved in `theorem_a3n.md`.

**Remark on the 2-row pattern.** Restricting 3×n sets to rows 0 and 2 reaches n+2 only when n ≡ 2 (mod 4). For n ≡ 0, 1, 3 (mod 4), the optimal sets use the middle row, so no single two-row pattern gives the general lower bound.

## 3. Method

We model the problem as a constraint satisfaction problem. Each lattice point is a Boolean variable. For each right isosceles triple, we add the clause "not all three points are chosen." We add the constraint that each 2×2 block holds at most two chosen points, which is valid by the argument in Theorem 1 and tightens the linear relaxation. We maximize the number of chosen points with Google OR-Tools CP-SAT on 2 CPU cores, with time limits from 60 to 300 seconds.

Every reported solution was checked by an independent routine. That routine enumerates all triples and tests the right-isosceles condition directly, without using the solver's triangle list. All stored solutions for m ≤ 4, n ≤ 8 passed, as did the constructions in Theorem 1 and Proposition 3.

## 4. What is and isn't established

- **Proved:** Theorem 1 (both parts), with complete arguments.
- **Computed exactly:** every entry in the table marked OPTIMAL in the solver output, i.e. all of m ≤ 2 up to the displayed range, m = 3 with n ≤ 18, m = 4 with n ≤ 14, and m = 5 with n ≤ 12. These are finite computations, not general proofs.
- **Not established:** a closed form for m ≥ 4, and the values of the m = 4 and m = 5 rows beyond the table. The m = 3 closed form is now proved in `theorem_a3n.md`.
- **Asymptotics:** we do not address growth in n. The square-grid literature (Károlyi–Solymosi, arXiv:2607.22828, 2026) gives F(n) = Ω(n^1.3) and F(n) ≪ n²/(log n)^(1+c) for the square problem. Rectangular boards with fixed m are a different regime.

## 5. Novelty

We searched OEIS for right-isosceles-triangle subsets of rectangular grids. The only related entry we found was A271906, which covers square grids n×n with n ≤ 11, and no rectangular table. We did not search the broader combinatorics literature. Theorem 1 is elementary, and it is quite possible that it appears in the literature on the square-grid problem or on rectangular board problems, so we make no novelty claim for it. The computed table is the most likely new contribution, but that is contingent on a fuller literature check.

## 6. Reproducibility

Code and data are in `./`:

- `rect.py`: triangle enumeration and CP-SAT model for m×n boards.
- `rect2.py`: runs for the larger boards.
- `rect_4x8.json`, `rect_more.json`: solver output.
- `verify.py`: independent checker (square grids; the rectangular checks used the same triple test).
