"""Lower bound a(3,n) >= n+2 for all n>=4, by construction.
Periodic block P = (5,5,0,0) repeated (rows 0 and 2 on columns 0,1 mod 4): admissible forever.
Base sets of lengths b = 8..11 ending in state (5,5,0,0) with n+2 points are found by DP
and then extended by appending P."""
import sys, itertools, json
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
from dp3 import window_ok
pop=lambda c: bin(c).count('1')
T=(5,5,0,0)

def best_ending(n):
    # DP over sequences of n columns; state=last 4 columns; returns best seq ending in T
    cur={}
    for s in itertools.product(range(8),repeat=4):
        if window_ok(s): cur[s]=(sum(pop(c) for c in s), s)
    # cur maps state -> (value, sequence)  (sequence = all columns so far)
    seqs={s:(v,list(s)) for s,(v,_) in cur.items()}
    for L in range(5,n+1):
        nxt={}
        for st,(v,seq) in seqs.items():
            for c in range(8):
                w=st+(c,)
                if window_ok(w):
                    s2=w[1:]
                    cand=(v+pop(c), seq+[c])
                    if s2 not in nxt or cand[0]>nxt[s2][0]:
                        nxt[s2]=cand
        seqs=nxt
    return seqs.get(T)

if __name__=="__main__":
    base={}
    for b in range(8,12):
        r=best_ending(b)
        if r is None: print(b,"no path ending in T"); continue
        v,seq=r
        print("b=",b,"max weight ending in T =",v,"  b+2 =",b+2, "seq",seq)
        base[b]=seq
    json.dump(base,open('base3.json','w'))
