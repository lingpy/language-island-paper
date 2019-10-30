from pathlib import Path
from pylexibank.dataset import Dataset as BaseDataset
from pylexibank import progressbar as pb
from pylexibank import Language
from clldutils.misc import slug
import attr

import lingpy

@attr.s
class CustomLanguage(Language):
    Latitude = attr.ib(default=None)
    Longitude = attr.ib(default=None)
    Village = attr.ib(default=None)
    Source = attr.ib(default=None)
    Family = attr.ib(default=None)
    SubGroup = attr.ib(default=None)
    DialectGroup = attr.ib(default=None)
    Number = attr.ib(default=None)

class Dataset(BaseDataset):
    dir = Path(__file__).parent
    id = 'hantganbangime'
    language_class = CustomLanguage
    def cmd_makecldf(self, args):
        wl = lingpy.Wordlist(self.raw_dir.joinpath('D_subset-300-22.tsv').as_posix())
        args.writer.add_sources()
        args.writer.add_languages()
        source_lookup = {language['ID']: language['Source'] for language in
                self.languages}
        concept_lookup = args.writer.add_concepts(
                id_factory=lambda x: x.id.split('-')[-1]+'_'+slug(x.english),
                lookup_factory='Name')
        for k in pb(wl, desc='wl-to-cldf', total=len(wl)):
            if wl[k, 'tokens']:
                args.writer.add_form_with_segments(
                    Language_ID=wl[k, 'doculect'],
                    Parameter_ID=concept_lookup[wl[k, 'concept']],
                    Value=wl[k, 'ipa'].strip() or ''.join(wl[k, 'tokens']),
                    Form=wl[k, 'ipa'].strip() or ''.join(wl[k, 'tokens']),
                    Segments=wl[k, 'tokens'],
                    Source=[source_lookup[wl[k, 'doculect']]],
                    Comment=wl[k, 'note']
                    )
