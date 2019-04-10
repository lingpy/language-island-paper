# coding=utf-8
from __future__ import unicode_literals, print_function

from clldutils.path import Path
from pylexibank.dataset import Dataset as BaseDataset
from pylexibank.util import pb
from clldutils.misc import slug

import lingpy

SOURCE = 'Hantgan2018'


class Dataset(BaseDataset):
    dir = Path(__file__).parent
    id = 'hantganbangime'

    def cmd_download(self, **kw):
        pass

    def split_forms(self, item, value):
        value = self.lexemes.get(value, value)
        return [self.clean_form(item, form) for form in [value]]

    def cmd_install(self, **kw):
        wl = lingpy.Wordlist(self.raw.posix('D_subset-300-22.tsv'))
        source_dict = {}
        concept_dict = {}
        sources = {source.id: source for source in self.raw.read_bib()}
        
        with self.cldf as ds:
            ds.add_sources(sources[SOURCE])
            
            for l in self.languages:
                ds.add_language(ID=l['ID'], Name=l['Name'], Glottocode=l['Glottocode'])
                source_dict[l['Name']] = [l['Source'], l['ID']]
                ds.add_sources(sources[l['Source']])
            
            for c in self.concepts:
                ds.add_concept(
                    ID=c['ID'],
                    Concepticon_ID=c['Concepticon_ID'],
                    Concepticon_Gloss=c['Concepticon_Gloss'],
                    Name=c['Gloss'],
                )
                concept_dict[c['Gloss']] = c['ID']

            for k in pb(wl, desc='wl-to-cldf', total=len(wl)):
                if wl[k, 'tokens']:
                    ds.add_lexemes(
                        Language_ID=source_dict[wl[k, 'doculect']][1],
                        Parameter_ID=concept_dict[wl[k, 'concept']],
                        Value=wl[k, 'ipa'].strip() or ''.join(wl[k, 'tokens']),
                        Form=wl[k, 'ipa'],
                        Segments=wl[k, 'tokens'],
                        Source=[source_dict[wl[k, 'doculect']][0]],
                        Comment=wl[k, 'note']
                        )
