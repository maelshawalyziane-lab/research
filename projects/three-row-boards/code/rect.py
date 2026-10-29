"""Exact a(m,n): largest admissible subset of the m x n grid (rows m, columns n)."""
import sys, time, json, itertools
from ortools.sat.python import cp_model

def tris(m, n):
    pts = [(x, y) for x in range(n) for y in range(m)]
    inside = lambda p: 0 <= p[0] < n and 0 <= p[1] < m
    seen = set()
    R = range(-(max(m, n) - 1), max(m, n))
    for P in pts:
        for a, b in itertools.product(R, R):
            if a == 0 and b == 0: continue
            Q = (P[0]+a, P[1]+b); W = (P[0]-b, P[1]+a)
            if inside(Q) and inside(W):
                seen.add(frozenset([P, Q, W]))
    return [tuple(sorted(t)) for t in seen]

def exact(m, n, tl=600, workers=2):
    T = tris(m, n)
    md = cp_model.CpModel()
    x = {(i, j): md.NewBoolVar(f"x{i}_{j}") for i in range(n) for j in range(m)}
    for t in T: md.AddBoolOr([x[p].Not() for p in t])
    for i in range(n-1):
        for j in range(m-1):
            md.Add(x[i,j]+x[i+1,j]+x[i,j+1]+x[i+1,j+1] <= 2)
    md.Maximize(sum(x.values()))
    s = cp_model.CpSolver(); s.parameters.max_time_in_seconds = tl; s.parameters.num_workers = workers
    t0 = time.time(); st = s.Solve(md)
    sol = [p for p, v in x.items() if s.Value(v)] if st in (cp_model.OPTIMAL, cp_model.FEASIBLE) else []
    return dict(m=m, n=n, status=s.StatusName(st), best=int(s.ObjectiveValue()),
                bound=int(s.BestObjectiveBound()), time=round(time.time()-t0,2), solution=sol)

if __name__ == "__main__":
    M, N, tl = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
    res = []
    for m in range(1, M+1):
        row = []
        for n in range(m, N+1):
            r = exact(m, n, tl)
            print(json.dumps({k: r[k] for k in ("m","n","status","best","bound","time")}), flush=True)
            res.append(r)
    json.dump(res, open(f"rect_{M}x{N}.json","w"))
