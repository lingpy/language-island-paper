from lingpy.compare.sanity import *
from lingpy import *

def sublist(wordlist, concepts, languages):
    """Retrieve a sublist of a given wordlist."""
    
    D_ = {idx: wordlist._data[idx] for idx in wordlist._data if
            wordlist._data[idx][wordlist._colIdx] in languages}
    D = {idx: row for idx, row in D_.items() if row[wordlist._rowIdx] in
            concepts}
    D[0] = [c for c in wordlist.columns]
    return Wordlist(D)

wl = Wordlist('D_base_list.tsv')
languages = [y[0] for y in sorted(wl.coverage().items(), key=lambda x: x[1],
    reverse=True)][:22]
concepts = [c for c, _ in sorted(wl.get_etymdict(ref='concept').items(),
    key=lambda x: len([y for y in x[1] if y]), reverse=True)]

# compute best coverage for 100 concepts
for num in [100, 200, 300]:
    #for i in range(len(languages), 1, -1):
    wlx = sublist(wl, concepts[:num], languages)
    print(wlx.height, wlx.width)
    ac = average_coverage(wlx)
    mmc = mutual_coverage_check(wlx, int(num * 0.5))
    if ac >= 0.7 and mmc:
        print('AC: {0:4.2f} for {1} languages'.format(ac, len(languages)))
        wlx.output('tsv', filename='D_subset-{0}-{1}'.format(wlx.height,
            wlx.width))
        print(', '.join([l for l in wl.cols if l not in wlx.cols]))


