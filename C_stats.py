from lingpy import *
from lingpy.compare.sanity import *
from lingpy.convert.cldf import to_cldf

wl = Wordlist('D_subset-300-22.tsv')

for t, i in wl.coverage().items():
    print('{0}\t{1}\t{2:.2f}'.format(t, i, i/300))


