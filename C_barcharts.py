from lingpy import *
from collections import defaultdict
from matplotlib import pyplot as plt
import colorsys
from sys import argv

ref = 'scaid' if 'sca' in argv else 'lexstatid'

wl = Wordlist('D_subset-300-22.tsv-cognates.tsv')

langs = csv2list('D_languages.tsv')

# make dictionary to get the groups quickly from a language name
lang2group = {k[4]: k[2] for k in langs[1:]}

patterns = {l: [] for l in lang2group}
allpats = defaultdict(list)

etd = wl.get_etymdict(ref=ref)
for k, vals in etd.items():
    idxs = [v[0] for v in vals if v and wl[v[0], 'doculect'] in lang2group]
    lngs = [wl[idx, 'doculect'] for idx in idxs]
    groups = defaultdict(list)
    for idx, lng in zip(idxs, lngs):
        groups[lang2group[lng]] += [lng]
    gstruc = ' '.join(['{0}:{1}'.format(y, len(groups[y])) for y in
        sorted(groups)])
    for idx, lng in zip(idxs, lngs):
        patterns[lng] += [(gstruc, idx)]
    allpats[gstruc] += [k]

bars =  [0, 0, 0, 0, 0, 0]
bars2 = [0, 0, 0, 0, 0, 0]
bars3 = [0, 0, 0, 0, 0, 0]
bars4 = [0, 0, 0, 0, 0, 0]
bars5 = [0, 0, 0, 0, 0, 0]

with open('O_patterns-{0}.tsv'.format(ref), 'w') as f:
    f.write('PATTERN\tAtlantic\tBangime\tDogon\tMande\tSonghai\tExamples\tCOGID\n')
    for k, v in allpats.items():
        nums = ['0', '0', '0', '0', '0']
        grps = ['Atlantic', 'Bangime', 'Dogon', 'Mande', 'Songhai']
        cncs = [wl[[y[0] for y in etd[cogid] if y][0], 'concept'] for cogid in
                v]
        for key in k.split():
            a, b = key.split(':')
            kidx = grps.index(a)
            nums[kidx] = b
        f.write('{0}\t{1}\t{2}\t{3}\t{4}\n'.format(k, '\t'.join(nums),
            len(v), ' '.join([str(x) for x in
            v]), ', '.join(cncs)))
        if 'Bangime' in k:
            nums = [int(x) for x in nums]
            if nums.count(0) == 3:
                for i, (a, b) in enumerate(zip(grps, nums)):
                    if b > 0 and a != 'Bangime':
                        this_lng = a
                        bars[i] += len(v)
            elif nums.count(0) == 4:
                bars[1] += len(v)
            else:
                bars[-1] += len(v)
        if 'Atlantic' in k:
            nums = [int(x) for x in nums]
            if nums.count(0) == 3:
                for i, (a, b) in enumerate(zip(grps, nums)):
                    if b > 0 and a != 'Atlantic':
                        this_lng = a
                        bars2[i] += len(v)
            elif nums.count(0) == 4:
                bars2[0] += len(v)
            else:
                bars2[-1] += len(v)

        if 'Dogon' in k:
            nums = [int(x) for x in nums]
            if nums.count(0) == 3:
                for i, (a, b) in enumerate(zip(grps, nums)):
                    if b > 0 and a != 'Dogon':
                        this_lng = a
                        bars3[i] += len(v)
            elif nums.count(0) == 4:
                bars3[2] += len(v)
            else:
                bars3[-1] += len(v)
        if 'Mande' in k:
            nums = [int(x) for x in nums]
            if nums.count(0) == 3:
                for i, (a, b) in enumerate(zip(grps, nums)):
                    if b > 0 and a != 'Mande':
                        this_lng = a
                        bars4[i] += len(v)
            elif nums.count(0) == 4:
                bars4[3] += len(v)
            else:
                bars4[-1] += len(v)

        if 'Songhai' in k:
            nums = [int(x) for x in nums]
            if nums.count(0) == 3:
                for i, (a, b) in enumerate(zip(grps, nums)):
                    if b > 0 and a != 'Mande':
                        this_lng = a
                        bars5[i] += len(v)
            elif nums.count(0) == 4:
                bars5[4] += len(v)
            else:
                bars5[-1] += len(v)




plt.clf()
labels = grps + ['?']
explode = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgray', 'orange']
plt.pie(bars, explode=explode, labels=labels, colors=colors, shadow=True,
        startangle=140, autopct='%1.1f%%')
plt.axis('equal')
plt.savefig('O_bangime-{0}.pdf'.format(ref))
plt.clf()
#explode = [0.2, 0.0, 0.0, 0.2, 0.2, 0.2]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgray', 'orange']
plt.pie(bars2, explode=explode, labels=labels, colors=colors, shadow=True,
        startangle=140, autopct='%1.1f%%')
plt.axis('equal')
plt.savefig('O_atlantic-{0}.pdf'.format(ref))
plt.clf()
#explode = [0.2, 0.0, 0.0, 0.2, 0.2, 0.2]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgray', 'orange']
plt.pie(bars3, explode=explode, labels=labels, colors=colors, shadow=True,
        startangle=140, autopct='%1.1f%%')
plt.axis('equal')
plt.savefig('O_dogon-{0}.pdf'.format(ref))
plt.clf()
#explode = [0.2, 0.0, 0.0, 0.2, 0.2, 0.2]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgray', 'orange']
plt.pie(bars4, explode=explode, labels=labels, colors=colors, shadow=True,
        startangle=140, autopct='%1.1f%%')
plt.axis('equal')
plt.savefig('O_mande-{0}.pdf'.format(ref))
plt.clf()
#explode = [0.2, 0.0, 0.0, 0.2, 0.2, 0.2]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgray', 'orange']
plt.pie(bars5, explode=explode, labels=labels, colors=colors, shadow=True,
        startangle=140, autopct='%1.1f%%')
plt.axis('equal')
plt.savefig('O_songhai-{0}.pdf'.format(ref))
