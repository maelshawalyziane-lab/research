"""Exact a(3,n) via transfer over columns.
Column = 3-bit mask (bit y = point at row y). A set in 3 x n is admissible iff every
window of 5 consecutive columns is admissible (triangles have x-span <= 4, verified).
State = last 4 columns. Value = max number of points so far."""
import itertools, sys
from functools import lru_cache

# triangles: list of (dx, y-triples) relative to left column; enumerate all triangles
# as sets of cells (x, y) with x in 0..4, y in 0..2, normalized to min x = 0.
def all_triangles():
    tris=set()
    R=range(-6,7)
    for p,q in itertools.product(R,R):
        if p==0 and q==0: continue
        for w in [(-q,p),(q,-p)]:
            V=[(0,0),(p,q),w]
            ys=[v[1] for v in V]
            if max(ys)-min(ys)<=2:
                V=[(x,y-min(ys)) for x,y in V]
                x0=min(x for x,y in V)
                V=tuple(sorted((x-x0,y) for x,y in V))
                tris.add(V)
    return sorted(tris)

TRIS = all_triangles()
assert len(TRIS)==18 and max(max(x for x,y in t) for t in TRIS)==4

def window_ok(cols):
    """cols: tuple of masks for consecutive columns (len <= 5). Check every triangle
    placed at every horizontal offset inside the window."""
    L=len(cols)
    for t in TRIS:
        span=max(x for x,y in t); ytop=max(y for x,y in t)
        for o in range(L-span):
            for yo in range(3-ytop):
                ok=True
                for x,y in t:
                    if not (cols[o+x] >> (y+yo)) & 1: ok=False; break
                if ok: return False
    return True

def a3(n_max):
    # OK[k] for windows of length k (k<=5)
    # DP over sequences: state = tuple of last min(len,4) columns
    from collections import defaultdict
    res={}
    # initialize with sequences of length 1..4 (all admissible prefixes)
    cur={}
    for c in range(8):
        cur[(c,)]=bin(c).count('1')
    # build up to length 4 exactly
    for L in range(2,5):
        nxt={}
        for st,val in cur.items():
            for c in range(8):
                s2=st+(c,)
                if window_ok(s2):
                    nxt[s2]=max(nxt.get(s2,-1),val+bin(c).count('1'))
        cur=nxt
    # now cur: states of length 4, values = best total for length-4 boards
    res[4]=max(cur.values())
    L=4
    while L<n_max:
        L+=1
        nxt={}
        for st,val in cur.items():
            for c in range(8):
                w=st+(c,)
                if window_ok(w):
                    s2=w[1:]
                    nxt[s2]=max(nxt.get(s2,-1),val+bin(c).count('1'))
        cur=nxt
        res[L]=max(cur.values())
    return res

if __name__=="__main__":
    N=int(sys.argv[1])
    r=a3(N)
    for n in sorted(r):
        print(n, r[n], "n+2=",n+2, "OK" if r[n]==n+2 else "DIFF")
