#!/usr/bin/env python3
"""E0027 Main-only SmokeField shadow championship.

Treats sorted Main coordinates as a stochastic-particle abstraction. The code is
strictly post-2026-06-02, target-excluded, and paper-trading only.
"""
from __future__ import annotations
import itertools, json, math, random
from pathlib import Path
from math import comb

ROOT=Path(__file__).resolve().parents[1]
TOTAL=comb(50,5)


def load_main(path=ROOT/'data/draw_history.jsonl'):
    rows=[json.loads(x) for x in Path(path).read_text().splitlines() if x.strip()]
    rows=[r for r in rows if r['draw_date']>='2026-06-02']
    return rows


def slot_null():
    p=[[0.0]*51 for _ in range(5)]
    for j in range(1,6):
        for x in range(1,51):
            if x>=j and 50-x>=5-j:
                p[j-1][x]=comb(x-1,j-1)*comb(50-x,5-j)/TOTAL
    return p


def gap_null():
    p=[0.0]*51
    for d in range(1,51):
        k=d-1
        if 45-k>=0:
            p[d]=comb(49-k,4)/TOTAL
    s=sum(p)
    return [v/s for v in p]

P0=slot_null(); P0G=gap_null()


def gauss(z,h): return math.exp(-0.5*(z/h)**2)


def slot_q(draws,current,mode='delta',kappa=20,h=3.0):
    trans=[[draws[t][j]-draws[t-1][j] for j in range(5)] for t in range(1,len(draws))]
    out=[[0.0]*51 for _ in range(5)]
    if mode=='accel' and len(trans)<2: return P0
    for j in range(5):
        centers=[]
        if mode=='delta':
            centers=[current[j]+d[j] for d in trans]; n=len(trans)
        else:
            acc=[trans[t][j]-trans[t-1][j] for t in range(1,len(trans))]
            centers=[current[j]+trans[-1][j]+a for a in acc]; n=len(acc)
        k=[0.0]*51
        for x in range(1,51):
            if P0[j][x]>0:
                k[x]=sum(gauss(x-c,h) for c in centers)
        z=sum(k)
        if z: k=[v/z for v in k]
        rho=n/(n+kappa) if n else 0
        out[j]=[(1-rho)*P0[j][x]+rho*k[x] for x in range(51)]
    return out


def slot_ratio(q):
    out=[[0.0]*51 for _ in range(5)]
    for j in range(5):
        for x in range(51):
            out[j][x]=q[j][x]/P0[j][x] if P0[j][x]>0 else 0.0
    return out


def gap_ratio(draws,current,pressure=True,kappa=30,h=2.5,ridge=100.0):
    gaps=[[r[j+1]-r[j] for j in range(4)] for r in draws]
    d=[]; gp=[]
    for t in range(1,len(gaps)):
        for j in range(4):
            d.append(gaps[t][j]-gaps[t-1][j]); gp.append(gaps[t-1][j])
    beta=0.0
    if pressure and d:
        a=[8.5-g for g in gp]
        beta=sum(x*y for x,y in zip(a,d))/(sum(x*x for x in a)+ridge)
    resid=[dv-beta*(8.5-g) for dv,g in zip(d,gp)]
    curr=[current[j+1]-current[j] for j in range(4)]
    rho=len(resid)/(len(resid)+kappa) if resid else 0
    out=[[1.0]*51 for _ in range(4)]
    for j in range(4):
        shift=beta*(8.5-curr[j]) if pressure else 0.0
        k=[0.0]*51
        for g in range(1,51):
            if P0G[g]>0:
                k[g]=sum(gauss(g-(curr[j]+shift+e),h) for e in resid)
        z=sum(k)
        if z: k=[v/z for v in k]
        for g in range(1,51):
            q=(1-rho)*P0G[g]+rho*k[g]
            out[j][g]=q/P0G[g] if P0G[g]>0 else 0.0
    return out


def chain_norm(slot_r,gap_r):
    f=[[0.0]*51 for _ in range(5)]
    f[0]=slot_r[0][:]
    for j in range(1,5):
        for y in range(1,51):
            f[j][y]=slot_r[j][y]*sum(f[j-1][x]*gap_r[j-1][y-x] for x in range(1,y))
    return sum(f[4])


def raw(line,slot_r,gap_r):
    w=1.0
    for j,x in enumerate(line): w*=slot_r[j][x]
    for j in range(4): w*=gap_r[j][line[j+1]-line[j]]
    return w


def score_target(draws,t,variant):
    train=draws[:t]; current=train[-1]
    ones=[[1.0]*51 for _ in range(4)]
    if variant=='signed': sr=slot_ratio(slot_q(train,current,'delta')); gr=ones
    elif variant=='accel': sr=slot_ratio(slot_q(train,current,'accel')); gr=ones
    elif variant=='pressure': sr=[[1.0 if P0[j][x]>0 else 0.0 for x in range(51)] for j in range(5)]; gr=gap_ratio(train,current,True)
    elif variant=='signed_pressure': sr=slot_ratio(slot_q(train,current,'delta')); gr=gap_ratio(train,current,True)
    elif variant=='accel_pressure': sr=slot_ratio(slot_q(train,current,'accel')); gr=gap_ratio(train,current,True)
    else: raise ValueError(variant)
    z=chain_norm(sr,gr); w=raw(draws[t],sr,gr)
    return math.log(w/z)+math.log(TOTAL)


def main():
    rows=load_main(); draws=[r['main_numbers'] for r in rows]
    variants=['signed','accel','pressure','signed_pressure','accel_pressure']
    out={v:[] for v in variants}
    for t in range(8,len(draws)):
        for v in variants: out[v].append(score_target(draws,t,v))
    print(json.dumps({v:{'targets':len(x),'mean_log_score_delta_vs_uniform':sum(x)/len(x)} for v,x in out.items()},indent=2))

if __name__=='__main__': main()
