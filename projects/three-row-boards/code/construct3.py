"""Explicit admissible sets in 3 x n with n+2 points, for all n >= 4 (lower-bound construction)."""
import itertools, sys, json
sys.path.insert(0,__import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from dp3 import window_ok
from verify import is_right_isosceles
pop=lambda c: bin(c).count('1')
NEG=-10**9
S0=(0,0,5,5)
states=[s for s in itertools.product(range(8),repeat=4) if window_ok(s)]

def best_paths(length):
    """max weight of length-column admissible sequences ending in S0, with the sequence."""
    cur={s:(sum(pop(c) for c in s), list(s)) for s in states}
    for L in range(5,length+1):
        nxt={}
        for s,(v,seq) in cur.items():
            for c in range(8):
                w=s+(c,)
                if window_ok(w):
                    t=w[1:]; cand=(v+pop(c), seq+[c])
                    if t not in nxt or cand[0]>nxt[t][0]: nxt[t]=cand
        cur=nxt
    return cur.get(S0)

def cycle4():
    """a 4-column admissible continuation from S0 back to S0 with weight 4."""
    best=None
    for c in itertools.product(range(8),repeat=4):
        seq=list(S0); s=S0; ok=True; w=0
        for x in c:
            ww=s+(x,)
            if not window_ok(ww): ok=False; break
            s=ww[1:]; w+=pop(x); seq.append(x)
        if ok and s==S0 and w==4: return list(c)
    return None

def to_points(cols):
    return [(x,y) for x,c in enumerate(cols) for y in range(3) if (c>>y)&1]

def admissible(P):
    return all(not is_right_isosceles(*t) for t in itertools.combinations(P,3))

if __name__=="__main__":
    base={}
    for b in (8,9,10,11):
        v,seq=best_paths(b)
        print("base b=",b,"weight",v,"= b+2?",v==b+2,"seq",seq)
        base[b]=seq
    cyc=cycle4(); print("cycle block:",cyc)
    # n=4 and n=7 explicit
    explicit={4:[7,0,0,7], 5:None, 6:None, 7:None}
    # find explicit optimal for 5,6,7 directly (brute via DP ending anywhere)
    cur={s:(sum(pop(c) for c in s), list(s)) for s in states}
    for L in range(5,8):
        nxt={}
        for s,(v,seq) in cur.items():
            for c in range(8):
                w=s+(c,)
                if window_ok(w):
                    t=w[1:]; cand=(v+pop(c), seq+[c])
                    if t not in nxt or cand[0]>nxt[t][0]: nxt[t]=cand
        cur=nxt
        best=max(cur.values())
        print("best length",L,"weight",best[0],"seq",best[1])
        explicit[L]=best[1]
    json.dump({"base":base,"cycle":cyc,"explicit":explicit},open('construct3.json','w'))
