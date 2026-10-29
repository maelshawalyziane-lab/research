import sys, json
sys.path.insert(0,'.')
from rect import exact
out=[]
for m,n_lo,n_hi,tl in [(2,9,16,60),(3,9,20,120),(4,9,14,200),(5,5,12,200)]:
    for n in range(n_lo, n_hi+1):
        r=exact(m,n,tl)
        print(json.dumps({k:r[k] for k in ("m","n","status","best","bound","time")}),flush=True)
        out.append({k:r[k] for k in ("m","n","status","best","bound","time")})
json.dump(out,open('rect_more.json','w'))
