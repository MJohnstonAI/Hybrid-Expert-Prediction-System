"""Finite, post-hoc decade/transition championship. No slate authority."""
from __future__ import annotations
import hashlib
import itertools as it
import json
import math
import random
import statistics as st
import sys
from collections import Counter
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent
sys.path[:0]=[str(ROOT/'scripts'),str(ROOT/'experiments/E0032')]
import e0037_prequential_gate as gate
from k13_dp import SlotProductField

TOTAL=math.comb(50,5)
KAPPA=20

def compositions(total,parts,cap):
    if parts==1:
        if 0<=total<=cap: yield (total,)
        return
    for v in range(min(cap,total)+1):
        for tail in compositions(total-v,parts-1,cap): yield (v,)+tail

SHELLS=list(compositions(5,5,10))
INDEX={s:i for i,s in enumerate(SHELLS)}
COUNTS=np.array([math.prod(math.comb(10,c) for c in s) for s in SHELLS],dtype=float)
NULL=COUNTS/TOTAL
SHELL_ARRAY=np.array(SHELLS)
SHAPES=[tuple(sorted(s,reverse=True)) for s in SHELLS]
SHAPE_NULL={s:float(sum(p for shape,p in zip(SHAPES,NULL) if shape==s)) for s in set(SHAPES)}

def shell(line):
    c=[0]*5
    for n in line:c[(n-1)//10]+=1
    return tuple(c)

def choose(n,k):
    return math.comb(n,k) if 0<=k<=n else 0

SLOT_NULL=np.array([[choose(n-1,j)*choose(50-n,4-j)/TOTAL for n in range(1,51)] for j in range(5)])

class ShellLaw:
    def __init__(self,prob):
        self.prob=np.array(prob,dtype=float)
        assert abs(sum(self.prob)-1)<1e-10 and min(self.prob)>0
    def log_prob(self,line):
        i=INDEX[shell(line)]
        return math.log(self.prob[i]/COUNTS[i])
    def marginals(self):
        return np.repeat(self.prob@SHELL_ARRAY/10,10).tolist()
    def params(self):return {'shell_probabilities':self.prob.tolist()}

class ResidualLaw:
    def __init__(self,weights,diagnostics=None):
        self.field=SlotProductField(weights)
        self.weights=np.array(weights)
        self.slots=self.field.slot_marginals()
        self.marg=np.array(self.slots).sum(axis=0).tolist()
        self.diagnostics=diagnostics
    def log_prob(self,line):
        return sum(math.log(self.weights[j,n-1]) for j,n in enumerate(line))-math.log(self.field.z)
    def marginals(self):return self.marg
    def params(self):return {'weights':self.weights.tolist(),'slot_marginals':self.slots,'diagnostics':self.diagnostics}

def movement_bin(d,signed):
    magnitude=0 if d==0 else 1 if abs(d)<=3 else 2 if abs(d)<=10 else 3
    return 3+(magnitude if d>=0 else -magnitude) if signed else magnitude

def transition(history,signed):
    b=7 if signed else 4
    observed=np.zeros((5,b)); expected=np.zeros((5,b))
    for prev,current in zip(history,history[1:]):
        for j in range(5):
            observed[j,movement_bin(current['main'][j]-prev['main'][j],signed)]+=1
            for n in range(1,51):
                expected[j,movement_bin(n-prev['main'][j],signed)]+=SLOT_NULL[j,n-1]
    n=len(history)-1
    prior=KAPPA*expected/n
    ratio=np.divide(observed+prior,expected+prior,out=np.ones_like(expected),where=expected>0)
    # Unseen bins retain weight one; strictly positive shrinkage elsewhere.
    weights=[[ratio[j,movement_bin(x-history[-1]['main'][j],signed)] for x in range(1,51)] for j in range(5)]
    return ResidualLaw(weights,{'observed':observed.tolist(),'expected_null':expected.tolist(),'ratios':ratio.tolist()})

def forecast(history):
    assert len(history)>=6
    shells=[shell(r['main']) for r in history]
    counts=Counter(shells); groups=Counter(tuple(sorted(s,reverse=True)) for s in shells)
    group_prob={s:(groups[s]+KAPPA*q)/(len(history)+KAPPA) for s,q in SHAPE_NULL.items()}
    group=np.array([group_prob[shape]*p/SHAPE_NULL[shape] for shape,p in zip(SHAPES,NULL)])
    unconditional=np.array([(counts[s]+KAPPA*q)/(len(history)+KAPPA) for s,q in zip(SHELLS,NULL)])
    lastshape=tuple(sorted(shells[-1],reverse=True))
    conditional=Counter(cur for prev,cur in zip(shells,shells[1:]) if tuple(sorted(prev,reverse=True))==lastshape)
    cond=np.array([(conditional[s]+KAPPA*q)/(sum(conditional.values())+KAPPA) for s,q in zip(SHELLS,unconditional)])
    laws={'GROUP':ShellLaw(group),'SHELL':ShellLaw(unconditional),'SHELL_TRANS':ShellLaw(cond),
          'VVD_RESIDUAL':transition(history,False),'SIGNED_RESIDUAL':transition(history,True)}
    laws['SAFE_MIX']=gate.MixtureLaw([(0.5,gate.UniformLaw())]+[(0.1,v) for v in laws.values()])
    inc,info=gate.e0030_incumbent_law(history)
    laws.update(uniform=gate.UniformLaw(),incumbent=inc,frequency=info['components'][1],recent5=info['components'][2])
    return laws

def allocation_hit_table(shells,allocations,group_size=10):
    """Exact conditional hypergeometric convolution; axes shell, allocation, hits."""
    draws=sum(shells[0]); out=np.zeros((len(shells),len(allocations),draws+1))
    for si,s in enumerate(shells):
        dist=np.zeros((len(allocations),draws+1));dist[:,0]=1
        for d,c in enumerate(s):
            probs=np.array([[choose(k[d],h)*choose(group_size-k[d],c-h)/choose(group_size,c)
                             for h in range(c+1)] for k in allocations])
            new=np.zeros_like(dist)
            for h in range(c+1):new[:,h:]+=dist[:,:draws+1-h]*probs[:,h,None]
            dist=new
        out[si]=dist
    return out

def top13(marg,tie_order):
    return sorted(sorted(range(1,51),key=lambda n:(-round(marg[n-1],12),tie_order[n]))[:13])

def allocation_basket(allocation,tie_order):
    chosen=[]
    for d,k in enumerate(allocation):
        chosen+=sorted(range(d*10+1,d*10+11),key=lambda n:tie_order[n])[:k]
    return sorted(chosen)

def freeze(history,laws,seed,allocs,table):
    order=list(range(1,51));random.Random(seed).shuffle(order);tie={n:i for i,n in enumerate(order)}
    arms={}
    for name in ('SHELL','SHELL_TRANS'):
        hp=np.einsum('s,sah->ah',laws[name].prob,table)
        metrics={'mean':hp@np.arange(6),'four_plus':hp[:,4:].sum(axis=1),'five':hp[:,5],
                 'avoid_catastrophe':-hp[:,:2].sum(axis=1)}
        for objective,values in metrics.items():
            best=np.flatnonzero(values>=values.max()-1e-12)[0]
            arms[name+'_'+objective]={'allocation':allocs[best],'basket':allocation_basket(allocs[best],tie),
                                     'modeled_hit_probabilities':hp[best].tolist(),'global_under_shell_model':True}
    frozen={'training_cutoff':history[-1]['date'],'training_count':len(history),'history_sha256':digest(history),'seed':seed,
            'models':{name:{'parameters':law.params(),'marginals':law.marginals(),'k13':top13(law.marginals(),tie)} for name,law in laws.items()},
            'allocation_arms':arms}
    return frozen

def digest(obj):return hashlib.sha256(json.dumps(obj,sort_keys=True).encode()).hexdigest()

def score(laws,frozen,target):
    win=set(target['main'])
    result={'date':target['date'],'actual':list(target['main']),'freeze_sha256':digest(frozen),'models':{},'allocation_arms':{}}
    for name,law in laws.items():
        m=law.marginals()
        assert abs(sum(m)-5)<1e-9
        result['models'][name]={'delta':-law.log_prob(target['main'])-gate.LOG_TOTAL,
                              'brier':sum((v-(i in win))**2 for i,v in enumerate(m,1))/50,
                              'hits':len(win&set(frozen['models'][name]['k13']))}
    for name,arm in frozen['allocation_arms'].items():
        result['allocation_arms'][name]={'hits':len(win&set(arm['basket'])),**arm}
    return result

def hit_summary(h):
    return {'total':sum(h),'mean':st.mean(h),'null_expected_total':1.3*len(h),'catastrophes_le1':sum(x<=1 for x in h),
            'targets_ge3':sum(x>=3 for x in h),'targets_ge4':sum(x>=4 for x in h),'targets_eq5':h.count(5)}

def summarize(records):
    out={'n':len(records),'models':{},'allocation_arms':{}}
    for name in records[0]['models']:
        rows=[r['models'][name] for r in records]; d=[r['delta'] for r in rows]
        out['models'][name]={'mean_delta':st.mean(d),'se_delta':st.stdev(d)/math.sqrt(len(d)),
                            'mean_brier_minus_uniform':st.mean(r['brier']-0.09 for r in rows),
                            'mean_delta_minus_incumbent':st.mean(r['models'][name]['delta']-r['models']['incumbent']['delta'] for r in records),
                            'k13':hit_summary([r['hits'] for r in rows])}
    for name in records[0]['allocation_arms']:
        rows=[r['allocation_arms'][name] for r in records]
        out['allocation_arms'][name]=hit_summary([r['hits'] for r in rows])
    return out

def main():
    assert abs(sum(NULL)-1)<1e-12
    allocs=list(compositions(13,5,10));print('Allocations',len(allocs),flush=True)
    table=allocation_hit_table(SHELLS,allocs)
    assert np.max(abs(table.sum(axis=2)-1))<1e-12
    result={'experiment':'E0039','evidence':'INSUFFICIENT_EVIDENCE','status':'experimental','evaluation':'post_hoc_replay',
            'protocol_sha256':hashlib.sha256((HERE/'protocol.md').read_bytes()).hexdigest(),
            'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'allocations':len(allocs),'lanes':{}}
    with (HERE/'forecasts.jsonl').open('w',encoding='utf-8') as forecasts:
        for li,lane in enumerate(('MAIN','XTRA')):
            rows,audit=gate.load_lane(lane);records=[]
            for i in range(6,len(rows)):
                laws=forecast(rows[:i])
                frozen=freeze(rows[:i],laws,20261105+li*10000+i,allocs,table)
                forecasts.write(json.dumps({'lane':lane,'target':rows[i]['date'],'replay_only':True,'forecast':frozen})+'\n');forecasts.flush()
                records.append(score(laws,frozen,rows[i]))
                print(lane,rows[i]['date'],flush=True)
            result['lanes'][lane]={'audit':audit,'records':records,'all39':summarize(records),'last6':summarize(records[-6:])}
            (HERE/'results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('Complete',flush=True)

if __name__=='__main__':main()
