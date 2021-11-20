import pickle
from collections import defaultdict
from lingpy.convert.html import colorRange
import sys
import mpl_toolkits.basemap as bmp
import matplotlib.pyplot as plt
from lingpy import *

plt.clf()

m = bmp.Basemap(
        llcrnrlon=-4.25,
        urcrnrlon=-1.2,
        llcrnrlat=14.0,
        urcrnrlat=15.4,
        resolution='h',
        projection='merc'
        )
m.drawmapboundary(fill_color="blue")
m.drawcountries(color="black", linewidth=0.1)
m.fillcontinents(color="antiquewhite", alpha=0.5, lake_color="blue")
#m.etopo(scale=4)
m.shadedrelief(scale=7)
blacklist = ['Gourou', 'Ibi_So', 'Kindige',
    'Sangha_So', 'Soninke']

colors = {
        'Mande': 'red',
        'Atlantic': 'blue',
        'Dogon': 'green',
        'Songhai': 'orange',
        'Bangime': 'yellow'
        }
villages = csv2list('D_languages.tsv', strip_lines=False)
for line in villages[1:]:
    name = line[4].strip() or line[1]
    if name not in blacklist:
        group = line[2]
        color = colors[group]
        lon, lat = float(line[-2]), float(line[-3])
        x, y = m(lon, lat)
        plt.plot(x, 
                y, 
                'o', 
                color=color, 
                markersize=5,
                markeredgewidth=0.1,
                markeredgecolor='black')
        x2, y2 = m(lon+0.005, lat+0.005)
        plt.text(x2, y2, name, fontsize=5, bbox={'fc': 'white', 'lw': 0.1, 
            'boxstyle': 'round,pad=0.1'})

for g, c in sorted(colors.items()):
    plt.plot(-10000, -100, 'o', markersize=6, markeredgewidth=0.1,
            markeredgecolor='black', color=c, label=g)
plt.legend(loc=4)
plt.savefig('O_language_map.pdf')

