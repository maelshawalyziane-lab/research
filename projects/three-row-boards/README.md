# Three-row boards: a(3,n) = n + 2

**Author:** Mael Shawaly

Let a(3,n) be the largest number of lattice points on a board with 3 rows and n columns that contain no right isosceles triangle. This project proves **a(3,n) = n + 2 for all n ≥ 4**.

## Status
- **Lower bound:** explicit construction, checked by computer for n = 4..120.
- **Upper bound:** computer-assisted. A potential function on 443 four-column states gives the bound. The certificate is `code/phi3.json` and is checked by `code/audit.py` and `code/check_certificate.py`.
- **Novelty:** not established. I found no prior statement of this result in OEIS, arXiv, or the square-grid surveys, but the search was not exhaustive. An expert check is still needed.
- **Not peer reviewed.**

## Contents
- `paper/`: manuscript (`main.tex`, `main.pdf`).
- `code/`: scripts, certificate and DP values. See `code/README.md`.
- `dev/`: earlier exploration (failed base sequences, cycle search). These scripts import `dp3.py` from `code/`; run them with `PYTHONPATH=../code`.
- `notes/`: publishing plan and open checks.

## Reproduce
    cd code
    python3 audit.py
    python3 check_certificate.py
    python3 dp3.py 60
