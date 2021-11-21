# Code and data accompanying the study "Bangime: Secret Language..."

The code provided here is not in the best state with respect to readability, also because some ideas that have been formulated first in 2017 have now been superceded by new software packages. This being said, we emphasize, however, that it does not mean that the code does not run, and we have confirmed on 20th of November 2021 that the code runs with a fresh virtual environment for all scripts apart from the script `C_makemaps.py`, which was using the now deprecated `basemap` library. For now, we decided *not* to update the code for the map plotting routines, since they are not an essential aspect with respect to the replicability of the study. Given that the data has been made available in the form of a CLDF package, geolocations can be easily plotted with the help of the tools accompanying CLDF, like [cldfviz](https://github.com/cldf/cldfviz) or [cldfbench](https://github.com/cldf/cldfbench). 

## Requirements

To install all requirements, use a fresh virtual environment, and just type:

```
$ pip install -r requirements.txt
```

## Workflow

### Drawing the language map (requires basemap)

**Note that this part of the code will be difficult to replicate, since `basemap` has been deprecated, as mentioned above, so you better ignore this part of the code.**

Draws the geographic map in the study (the map was manually modified to adjust readability).
```
$ python C_makemaps.py
```

### Coverage statistics 

Extracts the sublist of 300 concepts and 22 languages.

```
$ python C_coverage.py
```

### Check overlap with other concept lists

We use the `pyconcepticon` API for this purpose along with the most recent verson of the Concepticon.

```
$ pip install pyconcepticon
$ git clone https://github.com/concepticon/concepticon-data
$ for i in "Blust-2008-210" "Gregersen-1976-217" "Matisoff-1978-200" "Swadesh-1955-100" "Swadesh-1952-200" "Tadmor-2009-100"; do echo $i `concepticon --repos=concepticon-data --repos-versino=v2.5.1 intersection Hantgan-2021-300.tsv $i | wc -l`  ; done
```
This yields as output:

```
Blust-2008-210 125
Gregersen-1976-217 122
Matisoff-1978-200 118
Swadesh-1955-100 72
Swadesh-1952-200 116
Tadmor-2009-100 69
```
### Cognate detection and heatmaps (requires matplotlib)

Extracts cognate sets for two different approaches and compares shared pairwise similarities.

```
$ python C_lexstat.py
```

### Barcharts

Creates barcharts of shared vocabulary.

```
$ python C_barcharts.py sca
```

For the lexstat analysis, write:

```
$ python C_barcharts.py
```


