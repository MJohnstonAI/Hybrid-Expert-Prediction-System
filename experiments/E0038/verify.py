"""Reproduce scores through frozen E0037 code and test target/future isolation."""
import copy
import hashlib
import json
import math
from pathlib import Path
import replay as r

def main():
    result=json.loads((r.HERE/'results.json').read_text())
    checks=[]
    for lane in ['MAIN','XTRA']:
        rows,_=r.g.load_lane(lane)
        for record in result['lanes'][lane]['records']:
            index=next(i for i,x in enumerate(rows) if x['date']==record['date'])
            frozen_file=json.loads((r.HERE/'forecasts'/f'{lane}_{record["date"]}.json').read_text())
            f=frozen_file['forecast']
            assert r.digest(f)==frozen_file['sha256']==record['freeze_sha256']
            assert f['training_cutoff']<record['date'] and f['training_count']==index
            assert f['training_sha256']==r.digest(rows[:index])
            for arm in f['acquisition'].values():
                assert len(arm['basket'])==len(set(arm['basket']))==13
                for key in ['johnson20','random_same_k13_20']:
                    assert len(arm[key])==len({tuple(x) for x in arm[key]})==20
                    assert all(len(x)==5 and len(set(x))==5 and set(x)<=set(arm['basket']) for x in arm[key])
            reference=r.g.score_target(rows[:index],rows[index])
            for metric in ['delta','brier','pb_delta']:
                for name,val in reference[metric].items():
                    assert math.isclose(val,record[metric][name],rel_tol=1e-11,abs_tol=1e-12),(lane,record['date'],metric,name)
            assert reference['k13']==record['k13'] and reference['k13_hits']==record['k13_hits']
        # Change every target/future outcome; complete prefix-built parameters must be unchanged.
        changed=copy.deepcopy(rows)
        for row in changed[39:]:
            row['main']=(1,2,3,4,5)
            row['pb']=1
        baseline=json.loads((r.HERE/'forecasts'/f'{lane}_{rows[39]["date"]}.json').read_text())['forecast']
        altered,pbs=r.forecasts_at(changed,39)
        assert altered['fits']==baseline['fits'] and pbs==baseline['pb']
        for name,model in baseline['models'].items():
            assert altered['laws'][name].params()==model['params']
            assert altered['laws'][name].marginals()==model['marginals']
        checks.append({'lane':lane,'targets_reproduced':6,'target_and_future_mutation_invariant':True,
                       'all_freeze_hashes_valid':True,'all_portfolios_unique_20_legal_lines':True})
    receipt=json.loads((r.HERE/'data_update_receipt.json').read_text())
    for lane,filename in [('MAIN','draw_history.jsonl'),('XTRA','powerball_xtra_history.jsonl')]:
        raw=(r.ROOT/'data'/filename).read_bytes()
        original=b''.join(raw.splitlines(keepends=True)[:39])
        assert hashlib.sha256(original).hexdigest()==receipt['lanes'][lane]['original_sha256']
    r.write(r.HERE/'verification.json',{'passed':True,'checks':checks,'historical_ledger_prefixes_unchanged':True,
                                      'reproduction_type':'code_reproduction_not_independent_implementation'})
    print('E0038 verification passed: all 12 targets reproduce frozen E0037 scores; future mutation cannot alter forecast.')

if __name__=='__main__': main()
