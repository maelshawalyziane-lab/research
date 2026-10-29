"""Independent audit of the a(3,n) = n+2 argument. Uses only brute-force geometry
(exact integer arithmetic), not the DP or certificate code."""
import itertools, json, hashlib

def is_rt_iso(A,B,C):
    for V,P,Q in ((A,B,C),(B,A,C),(C,A,B)):
        u=(P[0]-V[0],P[1]-V[1]); w=(Q[0]-V[0],Q[1]-V[1])
        if u==(0,0) or w==(0,0): continue
        if u[0]*w[0]+u[1]*w[1]==0 and u[0]**2+u[1]**2==w[0]**2+w[1]**2: return True
    return False

# A1: every right isosceles triangle in a 3-row strip (any position) has |p|,|q|<=2 and x-span<=4.
worst_x=0; worst_pq=0; count=0
R=range(-5,6)
for p,q in itertools.product(R,R):
    if (p,q)==(0,0): continue
    for w in [(-q,p),(q,-p)]:
        pts=[(0,0),(p,q),w]
        if max(y for _,y in pts)-min(y for _,y in pts)<=2:   # fits in 3 rows
            count+=1
            worst_x=max(worst_x,max(x for x,_ in pts)-min(x for x,_ in pts))
            worst_pq=max(worst_pq,abs(p),abs(q))
print("A1 triangles fitting 3 rows (enumerated):",count,"max x-span:",worst_x,"max |p|,|q|:",worst_pq)
assert worst_x<=4 and worst_pq<=2

# A2: independent check of the constructions for n = 4..120 (full triple check)
def construction(n):
    if n==4: cols=[7,0,0,7]
    elif n==5: cols=[7,0,2,4,5]
    elif n==6: cols=[7,0,2,2,0,7]
    elif n==7: cols=[7,0,2,4,4,4,3]
    else:
        base={8:[7,0,0,7,0,0,5,5],9:[7,0,2,1,5,0,0,5,5],10:[3,4,1,1,4,3,0,0,5,5],11:[6,1,1,1,1,4,3,0,0,5,5]}
        b=8+((n-8)%4); cols=base[b]+[0,0,5,5]*((n-b)//4)
    return cols
def pts(cols): return [(x,y) for x,c in enumerate(cols) for y in range(3) if (c>>y)&1]
bad=[]
for n in range(4,121):
    cols=construction(n); assert len(cols)==n
    P=pts(cols)
    if len(P)!=n+2 or any(is_rt_iso(*t) for t in itertools.combinations(P,3)): bad.append(n)
print("A2 constructions (size n+2, admissible) for n=4..120; failures:",bad)
assert not bad

# A3: independent check of the potential certificate (Phi in phi3.json)
Phi={tuple(map(int,k.split('|'))):v for k,v in json.load(open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'phi3.json'))).items()}
pop=lambda c: bin(c).count('1')
def adm_cols(cols): return not any(is_rt_iso(*t) for t in itertools.combinations(pts(cols),3))
states=[s for s in itertools.product(range(8),repeat=4) if adm_cols(s)]
assert set(states)==set(Phi)
assert min(Phi.values())>=0
ne=0
for w in itertools.product(range(8),repeat=5):
    if adm_cols(w):
        ne+=1
        assert Phi[w[:4]] >= pop(w[4])-1+Phi[w[1:]]-1e-9
mx=max(sum(pop(c) for c in s)+Phi[s] for s in states)
assert mx<=6
print("A3 certificate: states",len(states),"windows",ne,"max(psi+Phi)=",mx,"-> VALID")
h=hashlib.sha256(open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'phi3.json'),'rb').read()).hexdigest()
print("A3 sha256(phi3.json) =",h)
