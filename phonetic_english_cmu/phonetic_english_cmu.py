from ...baselanguageplugin import BaseLanguagePlugin


class OfficialLanguagePlugin(BaseLanguagePlugin):
    default_data = 'phonetic_english_cmu.txt'
    default_neighbor_lexicon = 'phonetic_english_cmu.txt'
    default_word_lexicon = 'phonetic_english_cmu.txt'
    default_lookup_lexicon = 'phonetic_english_cmu.txt'

    hidden_sequence = False

    def transform(self, input_sequence, frequency=1):
        return self.copy_onc(input_sequence, frequency=frequency)
