"""Independent check of the potential certificate for a(3,n) <= n+2.
Uses only brute-force geometry (verify.is_right_isosceles), not the DP's window code."""
import itertools, json, sys
sys.path.insert(0,__import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from verify import is_right_isosceles
pop=lambda c: bin(c).count('1')

def admissible_cols(cols):
    P=[(x,y) for x,c in enumerate(cols) for y in range(3) if (c>>y)&1]
    return all(not is_right_isosceles(*t) for t in itertools.combinations(P,3))

Phi={tuple(map(int,k.split('|'))):v for k,v in json.load(open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'phi3.json'))).items()}
states=[s for s in itertools.product(range(8),repeat=4) if admissible_cols(s)]
assert set(states)==set(Phi), "state sets differ"
print("admissible 4-column states:",len(states))
# (a) Phi >= 0
assert min(Phi.values())>=0
# (b) for every admissible 5-window (s,c): Phi(s) >= pop(c)-1 + Phi(s[1:]+(c,))
nb=0
for w in itertools.product(range(8),repeat=5):
    if admissible_cols(w):
        nb+=1
        s=w[:4]; t=w[1:]
        assert Phi[s] >= pop(w[4])-1+Phi[t] - 1e-9, ("edge violated", w)
print("admissible 5-windows checked:",nb)
# (c) psi(s)+Phi(s) <= 6
mx=max(sum(pop(c) for c in s)+Phi[s] for s in states)
print("max over states of psi+Phi:",mx, "(need <= 6)")
assert mx<=6
print("CERTIFICATE VALID: a(3,n) <= n+2 for all n>=4")
