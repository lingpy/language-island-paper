from setuptools import setup, find_packages
import json


with open('metadata.json') as fp:
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
        'pylexibank>=1.1.1',
    ]
)

