"""Feasibility test: is there an admissible subset of the n x n grid with >= target points?
Strengthened with window cuts: every k x k window contains at most a(k) chosen points,
where a(k) for k <= 8 is taken from our own exact runs (1,2,4,6,9,11,14,17)."""
import sys, time, json
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
from rit import triangles
from ortools.sat.python import cp_model

A = {1: 1, 2: 2, 3: 4, 4: 6, 5: 9, 6: 11, 7: 14, 8: 17}

def build(n, target):
    tris = triangles(n)
    m = cp_model.CpModel()
    x = {(i, j): m.NewBoolVar(f"x{i}_{j}") for i in range(n) for j in range(n)}
    for t in tris:
        m.AddBoolOr([x[p].Not() for p in t])
    for k in range(2, min(8, n) + 1):
        for i in range(n - k + 1):
            for j in range(n - k + 1):
                m.Add(sum(x[i + a, j + b] for a in range(k) for b in range(k)) <= A[k])
    m.Add(sum(x.values()) >= target)
    return m, x, len(tris)

if __name__ == "__main__":
    n, target, tl = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
    m, x, nt = build(n, target)
    s = cp_model.CpSolver()
    s.parameters.max_time_in_seconds = tl
    s.parameters.num_workers = 2
    t0 = time.time(); st = s.Solve(m)
    out = dict(n=n, target=target, triangles=nt, status=s.StatusName(st), time=round(time.time()-t0, 1))
    if st in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        out["solution"] = [list(p) for p, v in x.items() if s.Value(v)]
    print(json.dumps({k: v for k, v in out.items() if k != "solution"}), flush=True)
    json.dump(out, open(f"feas_n{n}_t{target}.json", "w"))
