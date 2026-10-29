"""Certificate for a(3,n) <= n+2.
States: admissible 4-tuples of columns (masks 0..7). Transition s=(c1,c2,c3,c4) -> (c2,c3,c4,c5)
allowed iff the 5-window (c1..c5) is admissible. Weight of transition = popcount(c5).
Potential Phi(s) = sup over paths from s of sum (popcount(c)-1)  (finite iff no cycle of mean > 1)."""
import itertools, sys, json
sys.path.insert(0,__import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from dp3 import window_ok
pop=lambda c: bin(c).count('1')

states=[s for s in itertools.product(range(8),repeat=4) if window_ok(s)]
S=set(states)
trans={s:[] for s in states}
for s in states:
    for c5 in range(8):
        w=s+(c5,)
        if window_ok(w):
            trans[s].append((w[1:], pop(c5)))
# longest-path potential via value iteration (Bellman-Ford style)
Phi={s:0.0 for s in states}
for it in range(10000):
    changed=False
    for s in states:
        best=0.0
        for t,w in trans[s]:
            v=(w-1)+Phi[t]
            if v>best+1e-12: best=v
        if best>Phi[s]+1e-12:
            Phi[s]=best; changed=True
    if not changed:
        break
print("states:",len(states),"iterations:",it+1,"converged:",not changed)
if changed:
    print("NOT converged: positive cycle suspected")
else:
    vals=[Phi[s]+pop_s for s,pop_s in [(s,sum(pop(c) for c in s)) for s in states]]
    D=max(vals)-min(Phi.values())
    print("min Phi:",min(Phi.values()),"max Phi:",max(Phi.values()))
    print("D = max_s(psi(s)+Phi(s)) - min Phi =",D)
    json.dump({"|".join(map(str,s)):Phi[s] for s in states}, open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'phi3.json'),'w'))
