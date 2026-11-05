"""Append externally corroborated missing rows, preserving existing ledger bytes."""
import hashlib
import json
import sys
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
from validate_draws import validate_rows
from validate_active_data import validate_xtra_rows
from sync_manifest import sync_manifest

RESULTS = [
    ('2026-10-16', [15,33,38,42,49],4, [13,33,34,35,47],11),
    ('2026-10-20', [1,18,21,41,47],5, [3,8,18,37,39],13),
    ('2026-10-23', [2,4,6,40,45],5, [14,19,21,31,50],6),
    ('2026-10-27', [3,4,5,38,48],3, [5,15,32,33,34],13),
    ('2026-10-30', [7,9,21,27,30],8, [6,24,29,36,37],2),
    ('2026-11-03', [13,15,32,34,43],12, [1,7,10,16,24],15),
]

def main():
    receipt = {'checked_on':'2026-11-05', 'official_endpoints_returned':403, 'lanes':{}}
    pending = []
    for lane, filename, ix in [('MAIN','draw_history.jsonl',1), ('XTRA','powerball_xtra_history.jsonl',3)]:
        path = ROOT / 'data' / filename
        raw = path.read_bytes()
        rows = [json.loads(s) for s in raw.decode('utf-8').splitlines() if s.strip()]
        additions = []
        by_date = {r['draw_date']:r for r in rows}
        game = 'powerball' if lane == 'MAIN' else 'powerball-xtra'
        sources = [f'https://www.lottery.co.za/{game}/results/2026',
                   'https://www.powerball.net/southafrica/results/history/2026',
                   f'https://za.national-lottery.com/{game}/results']
        for i, r in enumerate(RESULTS):
            d, nums, pb = r[0], r[ix], r[ix+1]
            if d in by_date:
                assert by_date[d]['main_numbers'] == nums and by_date[d]['powerball'] == pb, d
                continue
            assert d > rows[-1]['draw_date']
            row = dict(draw_id=40+i if lane=='MAIN' else 1764+i, draw_date=d,
                       main_numbers=nums, powerball=pb, macro_sum=sum(nums), game_format='powerball_50_16',
                       draw_method='unknown', machine_name='unknown', source_url=sources[0],
                       corroborating_source_urls=sources[1:],
                       data_quality_flags=['draw_method_unknown','machine_name_unknown'],
                       notes='Numbers corroborated against public result archives on 2026-11-05. Official operator endpoint returned HTTP 403. No machine or method inference.')
            if lane=='XTRA':
                row['game_variant']='powerball_xtra'
                row['data_quality_flags'] += ['externally_corroborated_nonofficial_source','pending_official_source_verification','cross_checked_against_second_independent_results_archive']
            additions.append(row)
        combined = rows + additions
        numbered = list(enumerate(combined, 1))
        errors = validate_rows(numbered, enforce_active_boundary=True) if lane=='MAIN' else validate_xtra_rows(numbered)
        assert not errors, errors
        expected=[]
        day=date(2026,6,2)
        while day<=date(2026,11,5):
            if day.weekday() in (1,4): expected.append(day.isoformat())
            day += timedelta(days=1)
        assert [r['draw_date'] for r in combined] == expected
        payload = (b'' if not additions else (b'' if raw.endswith(b'\n') else b'\n') + b''.join((json.dumps(r,separators=(',',':'))+'\n').encode() for r in additions))
        pending.append((path,raw,payload,combined))
        receipt['lanes'][lane]={'original_sha256':hashlib.sha256(raw).hexdigest(), 'original_rows':len(rows),
                               'added_dates':[r['draw_date'] for r in additions], 'sources':sources,
                               'final_sha256':hashlib.sha256(raw+payload).hexdigest(), 'final_rows':len(combined),
                               'historical_bytes_preserved':True, 'missing_expected_dates':[]}
    for path,raw,payload,rows in pending:
        assert path.read_bytes()==raw, 'Concurrent ledger change'
        if payload:
            with path.open('ab') as f: f.write(payload)
        assert path.read_bytes().startswith(raw)
    sync_manifest(ROOT/'data/draw_history.jsonl',ROOT/'data/draw_manifest.json',False)
    p=ROOT/'data/powerball_xtra_manifest.json'
    manifest=json.loads(p.read_text())
    rows=pending[1][3]
    manifest.update(canonical_row_count=len(rows),latest_canonical_draw_date=rows[-1]['draw_date'],
                    latest_canonical_draw_id=rows[-1]['draw_id'],missing_expected_draw_dates=[],state_is_complete_through_latest_expected_draw=True)
    manifest['provenance_qualified_operational_state']['formal_official_source_verification_pending_dates']=[r['draw_date'] for r in rows if 'pending_official_source_verification' in r['data_quality_flags']]
    note='2026-11-05 update: 45 rows through 2026-11-03; all Tuesday/Friday dates present. Six new results corroborated from lottery.co.za and public result archives; configured official endpoint returned 403. Pending verification and unknown machine/method retained.'
    if note not in manifest['notes']: manifest['notes'].append(note)
    p.write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    out=Path(__file__).with_name('data_update_receipt.json')
    if not out.exists(): out.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(receipt,indent=2))

if __name__=='__main__': main()
