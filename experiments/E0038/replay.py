"""Target-excluded E0038 audit; never creates historical pre-draw predictions."""
from __future__ import annotations
import hashlib
import importlib.util
import itertools
import json
import math
import random
import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT/'scripts'))
import e0037_prequential_gate as g
from johnson_portfolio_optimizer import greedy_johnson_cover
from oracle_k13_assembly_evolution import four_plus_cover

spec=importlib.util.spec_from_file_location('e0030_original',ROOT/'experiments/E0030/prototype.py')
p=importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)

def digest(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,allow_nan=False).encode()).hexdigest()

def write(path,obj):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(obj,indent=2,allow_nan=False)+'\n',encoding='utf-8')

def forecasts_at(rows,index):
    """Only prefix is passed to any fitted algorithm; future rows are inaccessible."""
    history=rows[:index]
    assert history and all(r['date'] < rows[index]['date'] for r in history)
    return g.build_forecasts(history),g.pb_forecasts(history)

def as_original(law):
    if isinstance(law,g.MixtureLaw):
        return p.Mixture([as_original(x) for _,x in law.components],[w for w,_ in law.components])
    return p.SubsetModel(list(law.w))

def portfolio_score(lines,winner,pb_pick,pb):
    hits=[len(set(x)&winner) for x in lines]
    return {'submitted_lines':len(lines),'best_main_hits':max(hits),
            'lines_ge3':sum(h>=3 for h in hits),'lines_ge4':sum(h>=4 for h in hits),
            'lines_eq5':hits.count(5),'pb_pick':pb_pick,'pb_hit':pb_pick==pb,
            'lines_ge3_plus_pb':sum(h>=3 for h in hits) if pb_pick==pb else 0}

def freeze(history,built,pbs,positions,seed):
    laws=built['laws']
    inc=as_original(laws['E0030_incumbent'])
    initial=g.top_k(laws['E0030_incumbent'].marginals())
    swap=p.acquire(inc,initial,passes=5)
    arms={'incumbent_point':initial,'same_field_four_plus':swap['basket'],
          'frequency':g.top_k(laws['E0030_cumulative'].marginals()),
          'recent5':g.top_k(laws['E0030_recent5'].marginals())}
    forecasts={name:{'params':law.params(),'marginals':law.marginals(),
                     'k13':g.top_k(law.marginals()),'k20':g.top_k(law.marginals(),20)}
               for name,law in laws.items() if name!='uniform'}
    portfolios={}
    rng=random.Random(seed)
    pb_pick=rng.randrange(1,17) # uniform baseline; same pick/budget across all main comparisons
    full=set()
    while len(full)<20: full.add(tuple(sorted(rng.sample(range(1,51),5))))
    for name,basket in arms.items():
        universe=list(itertools.combinations(basket,5))
        assert len(universe)==1287 and len(set(basket))==13
        portfolios[name]={'basket':basket,'universe_size':len(universe),
                          'universe_sha256':digest(universe),
                          'johnson20':[[basket[j-1] for j in pos] for pos in positions],
                          'random_same_k13_20':rng.sample(universe,20),
                          'modeled_complete_line_mass':p.basket_mass(inc,basket,5),
                          'modeled_four_plus_mass':p.basket_mass(inc,basket,4)}
    return {'training_count':len(history),'training_cutoff':history[-1]['date'],
            'training_sha256':digest(history),'fits':built['fits'],'models':forecasts,
            'pb':pbs,'uniform_pb_pick':pb_pick,'fullfield_random20':sorted(full),
            'acquisition':portfolios,'swap_details':swap}

def score(frozen,built,target):
    winner=set(target['main'])
    rec={'date':target['date'],'actual':list(target['main']),'pb':target['pb'],
         'freeze_sha256':digest(frozen),'delta':{},'brier':{},'k13':{},'k13_hits':{},'k20_hits':{}}
    for name,law in built['laws'].items():
        rec['delta'][name]=-law.log_prob(target['main'])-g.LOG_TOTAL
        marg=law.marginals()
        assert abs(sum(marg)-5)<1e-8 and all(0<x<1 for x in marg)
        rec['brier'][name]=sum((v-(n in winner))**2 for n,v in enumerate(marg,1))/50
        if name!='uniform':
            m=frozen['models'][name]
            rec['k13'][name]=m['k13']
            rec['k13_hits'][name]=len(winner&set(m['k13']))
            rec['k20_hits'][name]=len(winner&set(m['k20']))
    rec['pb_delta']={name:-math.log(probs[target['pb']-1])-math.log(16) for name,probs in frozen['pb'].items()}
    rec['pb_top1_hit']={name:(max(range(16),key=lambda i:(probs[i],-i))+1==target['pb']) for name,probs in frozen['pb'].items()}
    rec['acquisition']={}
    for name,arm in frozen['acquisition'].items():
        rec['acquisition'][name]={'k13':arm['basket'],'hits':len(winner&set(arm['basket'])),
                                 'winning_line_contained':winner.issubset(arm['basket']),
                                 'johnson20':portfolio_score(arm['johnson20'],winner,frozen['uniform_pb_pick'],target['pb']),
                                 'random_same_k13_20':portfolio_score(arm['random_same_k13_20'],winner,frozen['uniform_pb_pick'],target['pb'])}
    rec['fullfield_random20']=portfolio_score(frozen['fullfield_random20'],winner,frozen['uniform_pb_pick'],target['pb'])
    return rec

def summarize(recs):
    out={'n':len(recs),'probability_models':g.summarize(recs,list(recs[0]['delta'])),
         'e0037_composite':g.eprocess(recs,g.COMPOSITE_WEIGHTS),
         'e0037_pb_composite':g.eprocess(recs,{name:0.25 for name in recs[0]['pb_delta']},key='pb_delta'),
         'pb':{},'acquisition':{},'k20_diagnostic':{}}
    for name in recs[0]['pb_delta']:
        out['pb'][name]={'mean_delta':statistics.mean(r['pb_delta'][name] for r in recs),
                         'top1_hits':sum(r['pb_top1_hit'][name] for r in recs),'null_expected_hits':len(recs)/16}
    for name in recs[0]['k20_hits']:
        out['k20_diagnostic'][name]={'hits':sum(r['k20_hits'][name] for r in recs),'null_expected':2*len(recs)}
    for name in recs[0]['acquisition']:
        a=[r['acquisition'][name] for r in recs]
        h=[x['hits'] for x in a]
        s={'hits_by_target':h,'total_hits':sum(h),'null_expected_hits':1.3*len(recs),
           'catastrophes_le1':sum(x<=1 for x in h),'targets_ge3':sum(x>=3 for x in h),
           'targets_ge4':sum(x>=4 for x in h),'targets_eq5':h.count(5),'portfolios':{}}
        for key in ['johnson20','random_same_k13_20']:
            ports=[x[key] for x in a]
            s['portfolios'][key]={'total_lines':sum(x['submitted_lines'] for x in ports),
                                 'best_hits_by_target':[x['best_main_hits'] for x in ports],
                                 **{metric:sum(x[metric] for x in ports) for metric in ['lines_ge3','lines_ge4','lines_eq5','lines_ge3_plus_pb']}}
        out['acquisition'][name]=s
    out['fullfield_random20']={'total_lines':20*len(recs),'best_hits_by_target':[r['fullfield_random20']['best_main_hits'] for r in recs],
                              **{metric:sum(r['fullfield_random20'][metric] for r in recs) for metric in ['lines_ge3','lines_ge4','lines_eq5']}}
    return out

def main():
    report=greedy_johnson_cover(tuple(range(1,14)),20,'four_plus_first')
    reproduced=four_plus_cover(13,20)
    assert report.covered_4plus==reproduced['covered_4plus']==788
    assert report.covered_5plus==20 and report.winner_universe_size==1287
    positions=report.selected_lines
    out={'experiment':'E0038','evidence_classification':'INSUFFICIENT_EVIDENCE','architecture_status':'experimental',
         'evaluation_type':'post_hoc_replay_with_separately_frozen_E0037_monitor','slate_authority':'none',
         'e0037_source_sha256':hashlib.sha256((ROOT/'scripts/e0037_prequential_gate.py').read_bytes()).hexdigest(),
         'protocol_sha256':hashlib.sha256((HERE/'protocol.md').read_bytes()).hexdigest(),
         'harness_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'geometry_reproduction':reproduced,'null_k13':g.hypergeom_pmf(13),'null_k20':g.hypergeom_pmf(20),'lanes':{}}
    for lane_index,lane in enumerate(['MAIN','XTRA']):
        rows,audit=g.load_lane(lane)
        recs=[]
        for index in range(39,len(rows)):
            print(f'Forecasting {lane} {rows[index]["date"]} from {index} previous rows',flush=True)
            built,pbs=forecasts_at(rows,index)
            frozen=freeze(rows[:index],built,pbs,positions,20261105+lane_index*10000+index)
            path=HERE/'forecasts'/f'{lane}_{rows[index]["date"]}.json'
            write(path,{'replay_not_pre_draw_artifact':True,'forecast':frozen,'sha256':digest(frozen)})
            # Result is consumed for scoring only after the serialized forecast is saved.
            rec=score(frozen,built,rows[index])
            recs.append(rec)
            write(ROOT/'cycles'/rows[index]['date']/'post_draw'/f'e0038_{lane.lower()}_replay.json',
                  {'evaluation_type':'post_hoc_replay','forecast_artifact':str(path.relative_to(ROOT)),**rec})
        out['lanes'][lane]={'audit':audit,'records':recs,'summary':summarize(recs)}
        write(HERE/'results.json',out)
    print('Wrote experiments/E0038/results.json',flush=True)

if __name__=='__main__': main()
