import pandas as pd
# Add comment
ds = e.load_evoked_stc('good', model='context%eventivity%transitivity', morph_ndvar=True)
src = ds['srcm']
src.source.set_parc('Frankland-25')
ds['cond'] = Factor(['%s_%s_%s' %(i['context'], i['eventivity'], i['transitivity']) for i in ds.itercases()])
conds = set(ds['cond'])

data = pd.DataFrame()
data['time'] = src.time.times
for cond in conds:
    ds_sub = ds.sub("cond==%r" %cond)
    ts = ds_sub['srcm'].summary(source='lmSTC-lh').mean('case')
    data[cond] = ts.x

data.to_csv('lmSTC_data.csv', index=False)
