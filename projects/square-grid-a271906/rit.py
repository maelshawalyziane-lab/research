"""Exact computation of a(n): the largest subset of the n x n grid
containing no three points forming a right isosceles triangle.
Model: CP-SAT, one Boolean per grid point, one clause per triangle."""
import sys, time
from itertools import product
from ortools.sat.python import cp_model

def triangles(n):
    pts = [(x, y) for x in range(n) for y in range(n)]
    inside = lambda p: 0 <= p[0] < n and 0 <= p[1] < n
    seen = set()
    R = range(-(n - 1), n)
    for P in pts:
        for a, b in product(R, R):
            if a == 0 and b == 0:
                continue
            Q = (P[0] + a, P[1] + b)
            W = (P[0] - b, P[1] + a)          # rotate (a,b) by +90 degrees
            if inside(Q) and inside(W):
                seen.add(frozenset([P, Q, W]))
    return [tuple(sorted(t)) for t in seen]

def solve(n, time_limit=600, workers=8):
    tris = triangles(n)
    m = cp_model.CpModel()
    idx = {(x, y): m.NewBoolVar(f"x{x}_{y}") for x in range(n) for y in range(n)}
    for t in tris:
        m.AddBoolOr([idx[p].Not() for p in t])
    m.Maximize(sum(idx.values()))
    s = cp_model.CpSolver()
    s.parameters.max_time_in_seconds = time_limit
    s.parameters.num_workers = workers
    t0 = time.time()
    st = s.Solve(m)
    best = int(s.ObjectiveValue()) if st in (cp_model.OPTIMAL, cp_model.FEASIBLE) else None
    bound = int(s.BestObjectiveBound())
    sol = [p for p, v in idx.items() if s.Value(v)] if best is not None else []
    return dict(n=n, triangles=len(tris), best=best, bound=bound,
                optimal=(st == cp_model.OPTIMAL), status=s.StatusName(st),
                time=round(time.time() - t0, 2), solution=sorted(sol))

if __name__ == "__main__":
    lo, hi, tl = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
    for n in range(lo, hi + 1):
        r = solve(n, tl)
        print(f"n={r['n']:2d} tris={r['triangles']:6d} best={r['best']} bound={r['bound']} "
              f"optimal={r['optimal']} status={r['status']} time={r['time']}s", flush=True)
        with open(f"rit_n{n}.txt", "w") as f:
            f.write(f"n={n} best={r['best']} bound={r['bound']} optimal={r['optimal']}\n")
            f.write(repr(r['solution']) + "\n")
