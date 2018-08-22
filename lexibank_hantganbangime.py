# coding=utf-8
from __future__ import unicode_literals, print_function

import attr
import lingpy
from pycldf.sources import Source

from clldutils.path import Path
from clldutils.misc import slug
from pylexibank.dataset import Metadata, Concept
from pylexibank.dataset import Dataset as BaseDataset
from pylexibank.util import pb

    

class Dataset(BaseDataset):
    dir = Path(__file__).parent

    def cmd_download(self, **kw):
        pass

    def split_forms(self, item, value):
        value = self.lexemes.get(value, value)
        return [self.clean_form(item, form) for form in [value]]


    def cmd_install(self, **kw):
        wl = lingpy.Wordlist(self.raw.posix('D_subset-300-22.tsv'))

        with self.cldf as ds:
            ds.add_sources(*self.raw.read_bib())
            
            source_dict = {}
            concept_dict = {}
            for l in self.languages:
                ds.add_language(
                    ID=slug(l['NAME']),
                    Name=l['NAME'],
                    Glottocode=l['GLOTTOLOG']
                    )
                source_dict[l['NAME']] = 'Hantgan2018'
                
            for c in self.concepts:
                ds.add_concept(
                        ID=slug(c['ENGLISH']),
                        Concepticon_ID=c['CONCEPTICON_ID'],
                        Name=c['ENGLISH'],
                        )

            for k in pb(wl, desc='wl-to-cldf'):
                if wl[k, 'tokens']:
                    for row in ds.add_lexemes(
                        Language_ID=slug(wl[k, 'doculect']),
                        Parameter_ID=slug(wl[k, 'concept'].strip('*')),
                        Value=wl[k, 'ipa'].strip() or ''.join(wl[k,
                            'tokens']),
                        Form=wl[k, 'ipa'],
                        Segments=wl[k, 'tokens'],
                        Source=source_dict.get(wl[k, 'doculect'],
                            '').split(','),
                        Comment=wl[k, 'note']
                        ):

                        cid = slug(wl[k, 'concept'])+'-'+'{0}'.format(wl[k,
                            'cogid'])
                        ds.add_cognate(
                                lexeme=row,
                                Cognateset_ID=cid,
                                Source='Hantgan2018',
                                Alignment='',
                                Alignment_Source=''
                                )
