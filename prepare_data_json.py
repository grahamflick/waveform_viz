import json

region = 'lmSTC-lh'

# ds = e.load_evoked_stc('good', model='context%eventivity%transitivity', morph_ndvar=True)
src = ds['srcm']
src.source.set_parc('Frankland-25')
ds['cond'] = Factor(['%s_%s_%s' %(i['context'], i['eventivity'], i['transitivity']) for i in ds.itercases()])

data = []

for row in ds.itercases():
    out = {}
    for c in ['subject', 'cond', 'context', 'eventivity', 'transitivity']:
        out[c] = row[c]
    out['values'] = []
    y = row['srcm'].summary(source=region)
    for i in range(len(y.time.times)):
        out['values'].append({'time': y.time.times[i], 'activity': y.x[i]})
    data.append(out)

with open('lmSTC_data.json', 'w') as f:
    json.dump(data, f)
