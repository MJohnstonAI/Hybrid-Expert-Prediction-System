#!/usr/bin/env python3
"""E0020 Main terminal-motif / symbolic-dynamics audit.

Uses only data/draw_history.jsonl. Standard library only. XTRA state is never read.
Outputs the walk-forward terminal championship, sequence-shuffle diagnostics,
finite algebraic-rule audit, and M0-M3 exact-coordinate synergy scores.
"""
from __future__ import annotations
import argparse, collections, json, math, random

POOL=50; PICKS=5; DEN=math.comb(POOL,PICKS); EPS=1e-15

def load(path):
    rows=[json.loads(x) for x in open(path,encoding='utf-8') if x.strip()]
    rows.sort(key=lambda r:r['draw_date'])
    return [r for r in rows if r['draw_date']>='2026-06-02']

def slot_pmfs():
    out=[]
    for j in range(1,6):
        p={}
        for n in range(1,51):
            p[n]=(math.comb(n-1,j-1)*math.comb(50-n,5-j)/DEN
                  if n-1>=j-1 and 50-n>=5-j else 0.0)
        out.append(p)
    return out
SLOT=slot_pmfs()
TERM=[]
for p in SLOT:
    q={r:0.0 for r in range(10)}
    for n,v in p.items(): q[n%10]+=v
    TERM.append(q)
PBTERM={r:0.0 for r in range(10)}
for n in range(1,17): PBTERM[n%10]+=1/16

def post(counts,prior,k):
    s=sum(counts.values())
    return {r:(counts.get(r,0)+k*prior[r])/(s+k) for r in prior}

def suffix(seq,prior,maxL=4,k=4.0):
    T=len(seq)
    for L in range(min(maxL,T-1),0,-1):
        word=tuple(seq[-L:]); c={r:0 for r in prior}; s=0
        for i in range(T-L):
            if tuple(seq[i:i+L])==word:
                c[seq[i+L]]+=1; s+=1
        if s: return post(c,prior,k),L,s
    return dict(prior),0,0

def markov(seq,prior,k=4.0):
    if len(seq)<2:return dict(prior),0
    c={r:0 for r in prior}; s=0; last=seq[-1]
    for i in range(len(seq)-1):
        if seq[i]==last:c[seq[i+1]]+=1;s+=1
    return post(c,prior,k),s

def cross(seqs,j,prior,maxL=4,k=8.0):
    T=len(seqs[j])
    for L in range(min(maxL,T-1),0,-1):
        word=tuple(seqs[j][-L:]); c={r:0 for r in prior}; s=0
        for z,seq in enumerate(seqs):
            if z==j:continue
            for i in range(T-L):
                if tuple(seq[i:i+L])==word:c[seq[i+L]]+=1;s+=1
        if s:return post(c,prior,k),L,s
    return dict(prior),0,0

def ll(p,y):return -math.log(max(p[y],EPS))
def br(p,y):return sum((v-(1 if r==y else 0))**2 for r,v in p.items())/len(p)
def hlr(a,b):return 'L' if b<a else ('H' if b>a else 'R')
def p0hlr(j,prev):
    p=SLOT[j]
    return {'L':sum(v for n,v in p.items() if n<prev),'R':p[prev],'H':sum(v for n,v in p.items() if n>prev)}
def runlen(states):
    if not states or states[-1]=='R':return 0
    x=states[-1]; r=0
    for s in reversed(states):
        if s!=x:break
        r+=1
    return r

def barp(hist,j):
    vals=[r['main_numbers'][j] for r in hist]; states=[hlr(a,b) for a,b in zip(vals[:-1],vals[1:])]
    rc=runlen(states); p0=p0hlr(j,vals[-1])
    if rc==0 or p0['L']==0 or p0['H']==0:return p0
    eH=eL=pH=pL=0; prior=[]
    for out in states:
        rr=runlen(prior)
        if rr>0:
            if out=='H':pH+=1
            elif out=='L':pL+=1
        if rr==rc:
            if out=='H':eH+=1
            elif out=='L':eL+=1
        prior.append(out)
    cH,cL=(pH,pL) if eH+eL<3 else (eH,eL)
    odds=((cH+1)/(cL+1))*((p0['H']/p0['L'])**0.6)
    rem=1-p0['R']; return {'L':rem/(1+odds),'R':p0['R'],'H':rem*odds/(1+odds)}
def v0(j,prev):
    q=collections.defaultdict(float)
    for n,p in SLOT[j].items():
        if p:q[abs(n-prev)]+=p
    return dict(q)
def vvdr(hist,j,k=10.0):
    prev=hist[-1]['main_numbers'][j]; q0=v0(j,prev); c=collections.Counter()
    for a,b in zip(hist[:-1],hist[1:]):c[abs(b['main_numbers'][j]-a['main_numbers'][j])]+=1
    raw={d:c[d]+k*q for d,q in q0.items()}; z=sum(raw.values())
    return {d:v/z for d,v in raw.items()},q0

def coord_models(hist,j):
    prev=hist[-1]['main_numbers'][j]; terms=[r['main_numbers'][j]%10 for r in hist]
    pt,_,_=suffix(terms,TERM[j]); ph=barp(hist,j); p0h=p0hlr(j,prev); pv,p0v=vvdr(hist,j)
    ans={}
    for name in ('M0','M1','M2','M3'):
        raw={}
        for n,base in SLOT[j].items():
            v=base
            if not v:raw[n]=0;continue
            if name!='M0':v*=pt[n%10]/TERM[j][n%10]
            if name in ('M2','M3'):
                s=hlr(prev,n);v*=ph[s]/p0h[s]
            if name=='M3':v*=pv[abs(n-prev)]/p0v[abs(n-prev)]
            raw[n]=v
        z=sum(raw.values()); ans[name]={n:v/z for n,v in raw.items()}
    return ans

def repstat(seqs,L):
    z=0
    for seq in seqs:
        c=collections.Counter(tuple(seq[i:i+L]) for i in range(len(seq)-L+1))
        z+=sum(v-1 for v in c.values() if v>1)
    return z
def crossstat(seqs,L):
    d=collections.defaultdict(set)
    for j,seq in enumerate(seqs):
        for i in range(len(seq)-L+1):d[tuple(seq[i:i+L])].add(j)
    return sum(len(s)-1 for s in d.values() if len(s)>1)
def abacount(seqs):return sum(sum(seq[i]==seq[i+2] and seq[i]!=seq[i+1] for i in range(len(seq)-2)) for seq in seqs)
def ababcount(seqs):return sum(sum(seq[i]==seq[i+2] and seq[i+1]==seq[i+3] and seq[i]!=seq[i+1] for i in range(len(seq)-3)) for seq in seqs)
def poisson_upper(ps,k):
    dp=[1.0]+[0.0]*len(ps)
    for p in ps:
        nd=[0.0]*len(dp)
        for i in range(len(ps)):nd[i]+=dp[i]*(1-p);nd[i+1]+=dp[i]*p
        dp=nd
    return sum(dp[k:])

def main(path,trials=5000,seed=20260901):
    rows=load(path); terms=[[r['main_numbers'][j]%10 for r in rows] for j in range(5)]; pb=[r['powerball']%10 for r in rows]
    terminal={m:{'ll':[],'br':[],'hit':[]} for m in ('M0','SS','CROSS','MK1')}; coords={m:{'ll':[],'br':[],'rank':[]} for m in ('M0','M1','M2','M3')}
    for t in range(8,len(rows)):
        hs=[x[:t] for x in terms]
        for j in range(5):
            y=terms[j][t]; ss,_,_=suffix(hs[j],TERM[j]); cr,_,_=cross(hs,j,TERM[j]); mk,_=markov(hs[j],TERM[j])
            for m,p in [('M0',TERM[j]),('SS',ss),('CROSS',cr),('MK1',mk)]:terminal[m]['ll'].append(ll(p,y));terminal[m]['br'].append(br(p,y));terminal[m]['hit'].append(max(p,key=p.get)==y)
            cm=coord_models(rows[:t],j); actual=rows[t]['main_numbers'][j]
            for m,p in cm.items():
                coords[m]['ll'].append(ll(p,actual));coords[m]['br'].append(sum((p[n]-(n==actual))**2 for n in p)/50);coords[m]['rank'].append(1+sum(v>p[actual]+1e-15 for v in p.values()))
    avg=lambda xs:sum(xs)/len(xs)
    tout={m:{'mean_logloss':avg(v['ll']),'mean_brier':avg(v['br']),'top1_rate':avg(v['hit'])} for m,v in terminal.items()}
    cout={m:{'mean_logloss':avg(v['ll']),'mean_brier':avg(v['br']),'mean_rank':avg(v['rank'])} for m,v in coords.items()}
    obs={**{f'same_L{L}':repstat(terms,L) for L in (2,3,4)},**{f'cross_L{L}':crossstat(terms,L) for L in (2,3,4)},'ABA':abacount(terms),'ABAB':ababcount(terms)}
    rng=random.Random(seed); sims={k:[] for k in obs}
    for _ in range(trials):
        ss=[]
        for q in terms:q=q.copy();rng.shuffle(q);ss.append(q)
        for L in (2,3,4):sims[f'same_L{L}'].append(repstat(ss,L));sims[f'cross_L{L}'].append(crossstat(ss,L))
        sims['ABA'].append(abacount(ss));sims['ABAB'].append(ababcount(ss))
    seq={k:{'observed':obs[k],'shuffle_mean':avg(v),'empirical_p':(sum(x>=obs[k] for x in v)+1)/(trials+1)} for k,v in sims.items()}
    rules={'absdiff':lambda a,b:abs(a-b)%10,'sum_mod10':lambda a,b:(a+b)%10,'linear_2b_minus_a':lambda a,b:(2*b-a)%10,'signed_step':lambda a,b:(b-a)%10,'repeat_b':lambda a,b:b,'pair_flip_a':lambda a,b:a}
    alg={}
    for name,f in rules.items():
        hits=0;ps=[]
        for t in range(8,len(rows)):
            for j in range(5):
                pred=f(terms[j][t-2],terms[j][t-1]);hits+=pred==terms[j][t];ps.append(TERM[j][pred])
        alg[name]={'hits':hits,'n':len(ps),'null_expected_hits':sum(ps),'p_upper':poisson_upper(ps,hits)}
    print(json.dumps({'targets':len(rows)-8,'terminal_models':tout,'coordinate_models':cout,'sequence_shuffle':seq,'algebraic_main':alg},indent=2))
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--ledger',default='data/draw_history.jsonl');ap.add_argument('--trials',type=int,default=5000);ap.add_argument('--seed',type=int,default=20260901);a=ap.parse_args();main(a.ledger,a.trials,a.seed)
