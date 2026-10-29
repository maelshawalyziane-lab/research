import itertools, sys
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
from dp3 import window_ok
pop=lambda c: bin(c).count('1')
states=[s for s in itertools.product(range(8),repeat=4) if window_ok(s)]
idx={s:i for i,s in enumerate(states)}
trans={s:[] for s in states}
for s in states:
    for c in range(8):
        w=s+(c,)
        if window_ok(w): trans[s].append((w[1:],pop(c)))
NEG=-10**9
def V_table(s0, bmax):
    """V[b][s] = max weight of a path of b columns (starting at a state-of-4 start) ending in s,
    where the path starts at any admissible 4-window (weight = popcounts of the 4 columns)."""
    cur={s:sum(pop(c) for c in s) for s in states}   # b = 4 columns
    tables={4:dict(cur)}
    for b in range(5,bmax+1):
        nxt={}
        for s,v in cur.items():
            for t,w in trans[s]:
                if nxt.get(t,NEG) < v+w: nxt[t]=v+w
        cur=nxt; tables[b]=dict(cur)
    return tables
tab=V_table(None,24)
# cycle of length 4, weight 4 from s back to s: s -> ... (4 transitions) -> s with total weight 4
def cycle4_ok(s):
    # DP from s, 4 steps, track weight, check returns to s with weight 4
    frontier={s:0}
    for _ in range(4):
        nf={}
        for u,v in frontier.items():
            for t,w in trans[u]:
                if nf.get(t,NEG)<v+w: nf[t]=v+w
        frontier=nf
    return frontier.get(s,NEG)==4
good=[]
for s in states:
    if not cycle4_ok(s): continue
    # which lengths b in 4..24 end at s with weight b+2 ?
    Rb=[b for b in range(4,25) if tab[b].get(s,NEG)==b+2]
    good.append((s,Rb))
print("states on weight-4 4-cycles:",len(good))
for s,Rb in good[:40]:
    res={b%4 for b in Rb}
    print(s, "lengths with n+2:",Rb, "residues covered:",sorted(res))
