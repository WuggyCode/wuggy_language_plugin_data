
import re

from ...baselanguageplugin import BaseLanguagePlugin


class OfficialLanguagePlugin(BaseLanguagePlugin):
    default_data = 'phonetic_french.txt'
    default_neighbor_lexicon = 'phonetic_french.txt'
    default_word_lexicon = 'phonetic_french.txt'
    default_lookup_lexicon = 'phonetic_french.txt'

    single_vowels = ['a', 'i', 'y', 'u', 'o', 'O', 'e',
                     'E', '�', '2', '9', '5', '1', '@', '�', '3']
    nucleuspattern = '%s' % (single_vowels)
    oncpattern = re.compile('(.*?)(%s)(.*)' % nucleuspattern)

    def transform(self, input_sequence, frequency=1):
        return self.pre_transform(input_sequence, frequency=frequency, language=self)
