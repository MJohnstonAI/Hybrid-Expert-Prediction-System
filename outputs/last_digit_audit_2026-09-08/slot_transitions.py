from pathlib import Path
import json
import numpy as np

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[1]
base=json.loads((OUT/'results.json').read_text())
rows=[json.loads(x) for x in (ROOT/'data/draw_history.jsonl').read_text().splitlines() if x.strip()]
dates={d for a in base['audit'] for d in a['dates']}
p0=np.array(base['null']['slot_digit_probabilities'])

def run(rows):
 d=np.array([[v%10 for v in r['main_numbers']] for r in rows]); n=len(d)
 def table(a):
  return np.array([np.bincount(a[:-1,j]*10+a[1:,j],minlength=100).reshape(10,10) for j in range(5)])
 obs=table(d)
 rng=np.random.default_rng(202609081)
 # Whole-row permutations preserve contemporaneous cross-slot dependence.
 pc=np.array([table(d[rng.permutation(n)]) for _ in range(20000)])
 mu=pc.mean(axis=0); sd=pc.std(axis=0)
 z=np.divide(obs-mu,sd,out=np.zeros_like(mu),where=sd>0)
 pz=np.divide(pc-mu,sd,out=np.zeros_like(pc,dtype=float),where=sd>0)
 mx=pz.max(axis=(1,2,3))
 entries=[]
 for j in range(5):
  den=obs[j].sum(axis=1)
  for y in range(10):
   for x in range(10):
    if den[y]>=3 and obs[j,y,x]>0:
     entries.append(dict(slot=j+1,previous=y,next=x,count=int(obs[j,y,x]),denominator=int(den[y]),rate=float(obs[j,y,x]/den[y]),exact_slot_baseline=float(p0[j,x]),target_sample_rate=float(np.mean(d[1:,j]==x)),permutation_expected_count=float(mu[j,y,x]),standardized_excess=float(z[j,y,x]),nominal_permutation_p=float((1+(pc[:,j,y,x]>=obs[j,y,x]).sum())/20001),max500_adjusted_p=float((1+(mx>=z[j,y,x]).sum())/20001)))
 entries.sort(key=lambda a:-a['standardized_excess'])
 losses={k:[] for k in ['null','frequency','conditional']}
 for t in range(8,n):
  by={k:[] for k in losses}
  for j in range(5):
   h=d[:t,j]; hcond=d[1:t,j][d[:t-1,j]==d[t-1,j]]
   probs=[p0[j],(np.bincount(h,minlength=10)+20*p0[j])/(t+20),(np.bincount(hcond,minlength=10)+20*p0[j])/(len(hcond)+20)]
   for key,p in zip(losses,probs):by[key].append(float(-np.log(p[d[t,j]])))
  for key in losses:losses[key].append(by[key])
 a={k:np.array(v) for k,v in losses.items()}
 gain=a['null']-a['conditional']
 current=[]
 for j in range(5):
  y=d[-1,j]; h=d[1:,j][d[:-1,j]==y]; cnt=np.bincount(h,minlength=10)
  pred=(cnt+20*p0[j])/(len(h)+20)
  current.append(dict(slot=j+1,previous_digit=int(y),prior_examples=len(h),next_counts=cnt.tolist(),shrunk_probabilities=pred.tolist(),null_probabilities=p0[j].tolist()))
 return dict(n=n,start=rows[0]['draw_date'],end=rows[-1]['draw_date'],all_transition_counts=obs.tolist(),top_transitions=entries[:15],global_max500_p=float((1+(mx>=z.max()).sum())/20001),global_max_z=float(z.max()),global_max_location=[int(i) for i in np.unravel_index(z.argmax(),z.shape)],test_targets=n-8,mean_logloss_by_slot={k:v.mean(axis=0).tolist() for k,v in a.items()},conditional_gain_vs_null_by_slot=gain.mean(axis=0).tolist(),conditional_gain_vs_frequency_by_slot=(a['frequency']-a['conditional']).mean(axis=0).tolist(),conditional_gain_sd_by_slot=gain.std(axis=0,ddof=1).tolist(),mean_marginal_gain_vs_null=float(gain.mean()),per_draw_mean_gain_sd=float(gain.mean(axis=1).std(ddof=1)),latest_digit_diagnostics=current)

result={'workbook':run([r for r in rows if r['draw_date'] in dates]),'canonical':run(rows)}
(OUT/'slot_transition_results.json').write_text(json.dumps(result,indent=2))
for name,r in result.items():
 print(name,json.dumps({k:v for k,v in r.items() if k not in ['all_transition_counts','latest_digit_diagnostics','top_transitions']},indent=2))
 print('TOP',json.dumps(r['top_transitions'][:6],indent=2))
