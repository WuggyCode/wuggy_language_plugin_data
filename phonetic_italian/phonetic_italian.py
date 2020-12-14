import re

from ...baselanguageplugin import BaseLanguagePlugin


class OfficialLanguagePlugin(BaseLanguagePlugin):
    default_data = 'phonetic_italian.txt'
    default_neighbor_lexicon = 'phonetic_italian.txt'
    default_word_lexicon = 'phonetic_italian.txt'
    default_lookup_lexicon = 'phonetic_italian.txt'

    single_letters = [u'a', u'A', u'E', u'i', u'O', u'u', u'o', u'e']
    single_letter_pattern = u'|'.join(single_letters)
    nucleuspattern = u'%s' % (single_letter_pattern)
    oncpattern = re.compile(u'(.*?)(%s)(.*)' % nucleuspattern)

    def transform(self, input_sequence, frequency=1):
        return self.pre_transform(input_sequence, frequency=frequency, language=self)
