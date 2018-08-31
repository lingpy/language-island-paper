# Data and code accompanying the paper "Bangime: Secret language, language isolate, or language island?

## Installation of the main code to run the analyses reported in the paper

To run the code, you need to have a fresh installation of python3 (python-3.4 or higher).

To install the necessary libraries, you can use PIP:

```shell
$ pip install -r pip-requirements
```

In order to install `basemap`, you have to follow the online instructions at [https://matplotlib.org/basemap/users/installing.html][https://matplotlib.org/basemap/users/installing.html]. 

To run the scripts, open a terminal in the folder `code`, and follow the instructions in the file `code/README.md`.

## Converting the dataset into a lexibank-cldf package

In order to convert the largest of the dataset that we created into a valid `lexibank` package in `CLDF` format, you have to install the package first by typing:

```shell
$ python setup.py develop
```

After this, you should install the `pylexibank` package (version >= 0.9.0) at [https://github.com/lexibank/pylexibank](https://github.com/lexibank/pylexibank) with all its requirements (follow the instructions at the repository website).

You can then curate the dataset (and turning it into `CLDF` format), by typing:

```shell
$ lexibank curate
lexibank-curator> makecldf hantganbangime
```

The resulting CLDF package can be found in the folder `src/lexibank_hantganbangime/cldf/`.



