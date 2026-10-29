"""Exact upper bounds for a(k) with redundant 2x2 block cuts (valid: any 3 of the
4 corners of an axis-parallel unit square form a right isosceles triangle, so
each 2x2 block holds <= 2 chosen points)."""
import sys, time, json
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
from rit import triangles
from ortools.sat.python import cp_model

def exact(n, tl, workers=2, lb=None):
    tris = triangles(n)
    m = cp_model.CpModel()
    x = {(i, j): m.NewBoolVar(f"x{i}_{j}") for i in range(n) for j in range(n)}
    for t in tris:
        m.AddBoolOr([x[p].Not() for p in t])
    for i in range(n - 1):
        for j in range(n - 1):
            m.Add(x[i, j] + x[i+1, j] + x[i, j+1] + x[i+1, j+1] <= 2)
    obj = sum(x.values())
    if lb is not None:
        m.Add(obj >= lb)
    m.Maximize(obj)
    s = cp_model.CpSolver()
    s.parameters.max_time_in_seconds = tl
    s.parameters.num_workers = workers
    t0 = time.time(); st = s.Solve(m)
    res = dict(n=n, status=s.StatusName(st), time=round(time.time()-t0, 1),
               best=int(s.ObjectiveValue()) if st in (cp_model.OPTIMAL, cp_model.FEASIBLE) else None,
               bound=int(s.BestObjectiveBound()))
    if st in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        res["solution"] = [list(p) for p, v in x.items() if s.Value(v)]
    return res

if __name__ == "__main__":
    n, tl = int(sys.argv[1]), float(sys.argv[2])
    r = exact(n, tl)
    print(json.dumps({k: v for k, v in r.items() if k != "solution"}), flush=True)
    json.dump(r, open(f"exact_n{n}.json", "w"))
