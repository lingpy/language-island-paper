# Code and data accompanying the study "Bangime: Secret Language..."

In its current state, the data are publishable, but the code is not readily readable, although it should run on most platforms, provided the software packages are installed. We will add more detailed descriptions in the near future.

## Requirements

- lingpy (v. 2.6.3), full installation with python-igraph and matplotlib (to make the plots)

## Workflow

### Drawing the language map (requires basemap)

Draws the geographic map in the study (the map was manually modified to adjust readability).
```
$ python C_makemaps.py
```

### Coverage statistics 

Extracts the sublist of 300 concepts and 22 languages.

```
$ python C_coverage.py
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

### Convert to CLDF

Convert data to cldf format for sharing:

```
$ python C_stats.py
```
