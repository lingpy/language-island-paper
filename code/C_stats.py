from lingpy import *
from lingpy.compare.sanity import *
from lingpy.convert.cldf import to_cldf

wl = Wordlist('D_subset-300-22.tsv')

for t, i in wl.coverage().items():
    print('{0}\t{1}\t{2:.2f}'.format(t, i, i/300))

#languages = csv2list('D_languages.tsv')
#doc2glot = {line[4]: line[5] for line in languages[1:]}
#wl.add_entries('glottocode', 'doculect', lambda x: doc2glot.get(x, ''))
#concepts = csv2list('Hantgan-2018-300.tsv')
#c2id = {line[2]: line[3] for line in concepts[1:]}
#wl.add_entries('concepticon_id', 'concept', lambda x: c2id.get(x, ''))
#to_cldf(wl)

