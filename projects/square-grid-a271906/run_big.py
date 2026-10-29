import sys, json
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
from rit import solve
n = int(sys.argv[1]); tl = float(sys.argv[2])
r = solve(n, tl, workers=int(sys.argv[3]))
out = {k: v for k, v in r.items() if k != "solution"}
out["solution"] = r["solution"]
with open(f"big_n{n}.json", "w") as f:
    json.dump(out, f)
print(json.dumps({k: out[k] for k in ("n","best","bound","optimal","status","time")}), flush=True)
