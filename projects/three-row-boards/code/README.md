# Supplementary code and certificate: a(3,n) = n+2

This folder reproduces every computational step in the paper.

Requirements: Python 3.9+. CP-SAT cross-check needs `pip install ortools`.

## Files
- `verify.py` : brute-force test of the right-isosceles condition (used by all audits).
- `dp3.py` : dynamic program over 4-column states; `python3 dp3.py 60` prints a(3,n) for n <= 60.
- `dp_values_a3n.txt` : the DP output for n = 4..60.
- `potential3.py` : computes the longest-path potential (writes `phi3.json`).
- `phi3.json` : the potential certificate Phi on the 443 admissible 4-column states.
  SHA-256 = c32cfb1a5b4c7f2a60d4520fa11840e5665fb87fdc01f27ad9f740f96e34d82d
- `check_certificate.py` : checks Proposition (a)-(c) with the brute-force geometry only.
- `construct3.py` : base sequences and the periodic block used for the lower bound.
- `audit.py` : independent audit (triangle geometry; constructions for n = 4..120; certificate).
- `rit.py`, `rect.py` : CP-SAT models (square and rectangular boards), used for cross-checks
  (for example, a(3,n) = n+2 for 4 <= n <= 18, and the rectangular table).

## Reproduce
    python3 audit.py              # about 10 seconds
    python3 check_certificate.py  # about 1 second
    python3 dp3.py 60             # about 5 seconds

## Expected output
`audit.py` ends with `A3 certificate ... -> VALID` and `failures: []`.
