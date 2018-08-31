from setuptools import setup, find_packages
import sys
import json


PY2 = sys.version_info.major == 2
with open('metadata.json', **({} if PY2 else {'encoding': 'utf-8'})) as fp:
    metadata = json.load(fp)


setup(
    name='lexibank_hantganbangime',
    description=metadata['title'],
    license=metadata.get('license', ''),
    url=metadata.get('url', ''),
    py_modules=['lexibank_hantganbangime'],
                packages=find_packages(where='src'),
        package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'lexibank.dataset': [
            'hantganbangime=lexibank_hantganbangime:Dataset',
        ]
    },
    install_requires=[
        'pylexibank>=0.9.0',
    ]
)

