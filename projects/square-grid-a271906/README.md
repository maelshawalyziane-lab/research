# Square grid: right-isosceles-free subsets (OEIS A271906)

**Author:** Mael Shawaly

Computations for the largest subset of the n × n grid with no right isosceles triangle.

## Status
- Exact values for n ≤ 7 by constraint programming. n = 8 is also proved (see `paper_note.md`).
- Values for n = 9–11 agree with OEIS A271906.
- Lower bounds for n = 12–16. **OEIS already lists lower bounds for n = 12–15 (29, 32, 36, 38).** My values for 12–15 add nothing and are weaker for 13–15. Only n = 16 (40) is not listed in the entry.
- No upper bounds beyond CP-SAT's trivial ones for n ≥ 9.

## Files
- `paper_note.md`: the write-up, with the erratum.
- `rit.py`, `exact.py`, `exact2.py`, `local.py`, `run_big.py`: solvers (need `ortools`).
- `verify.py`: independent checker.
- `*.json`, `rit_n*.txt`, `summary.json`: results.
