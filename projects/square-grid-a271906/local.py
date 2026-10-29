"""Simulated annealing for lower bounds on a(n): maximize |S| subject to no
right isosceles triangle. Penalty = number of violated triangles inside S."""
import sys, random, json, time, math
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
from rit import triangles

def run(n, seconds, seed):
    rnd = random.Random(seed)
    tris = triangles(n)
    inc = {}                                  # point -> list of triangle ids
    for i, t in enumerate(tris):
        for p in t:
            inc.setdefault(p, []).append(i)
    pts = [(x, y) for x in range(n) for y in range(n)]
    inS = {p: False for p in pts}
    cnt = [0] * len(tris)                     # number of S-points in each triangle
    viol = 0                                  # triangles fully inside S
    size = 0
    best, best_set = 0, []
    lam = 1.5                                 # penalty weight per violated triangle
    T0, T1 = 1.0, 0.02
    t0 = time.time(); it = 0
    while time.time() - t0 < seconds:
        it += 1
        T = T0 * (T1 / T0) ** (((time.time() - t0) / seconds) % 1.0)
        p = pts[rnd.randrange(len(pts))]
        if not inS[p]:
            # add p
            dv = sum(1 for i in inc.get(p, []) if cnt[i] == 2)
            delta = 1 - lam * dv
            if delta >= 0 or rnd.random() < math.exp(delta / T):
                inS[p] = True; size += 1; viol += dv
                for i in inc.get(p, []): cnt[i] += 1
        else:
            dv = sum(1 for i in inc.get(p, []) if cnt[i] == 3)
            delta = -1 + lam * dv
            if delta >= 0 or rnd.random() < math.exp(delta / T):
                inS[p] = False; size -= 1; viol -= dv
                for i in inc.get(p, []): cnt[i] -= 1
        if viol == 0 and size > best:
            best = size; best_set = [q for q in pts if inS[q]]
    return best, best_set, it

if __name__ == "__main__":
    n, secs = int(sys.argv[1]), float(sys.argv[2])
    best, S, it = run(n, secs, seed=int(sys.argv[3]) if len(sys.argv) > 3 else 1)
    from verify import check
    ok, _ = check(n, S)
    print(json.dumps({"n": n, "best": best, "iters": it, "verified": ok, "solution": S}), flush=True)
    with open(f"local_n{n}.json", "w") as f:
        json.dump({"n": n, "best": best, "verified": ok, "solution": S}, f)
