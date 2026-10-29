# Rectangular boards

**Author:** Mael Shawaly

Largest right-isosceles-free subsets of m × n boards.

## Status
- **Two rows (proved, probably elementary):** a(2,n) = 2⌈n/2⌉.
- **One row:** a(1,n) = n.
- **Three rows:** a(3,n) = n + 2 for n ≥ 4, proved in `../three-row-boards`.
- **Other sizes:** computed with CP-SAT. These are data, not theorems, and I haven't proved them for all n. I found no OEIS table for rectangular boards.
- Novelty not established: the search was not exhaustive.

## Files
- `rect_paper.md`: write-up.
- `rect.py`, `rect2.py`: CP-SAT models (need `ortools`).
- `rect_4x8.json`, `rect_more.json`: results.
