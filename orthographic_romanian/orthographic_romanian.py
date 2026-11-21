"""Official-style Romanian orthographic language plugin for Wuggy (WuggyCode/wuggy)."""

import re

try:
    from wuggy.plugins.baselanguageplugin import BaseLanguagePlugin
except ImportError:
    from ...baselanguageplugin import BaseLanguagePlugin


class OfficialLanguagePlugin(BaseLanguagePlugin):
    """Wuggy orthographic plugin implementing Romanian sub-syllabic nuclei and transitions."""

    default_data = "orthographic_romanian.txt"
    default_neighbor_lexicon = "orthographic_romanian.txt"
    default_word_lexicon = "orthographic_romanian.txt"
    default_lookup_lexicon = "orthographic_romanian.txt"

    # Longest vocalic nuclei first: Romanian triphthongs, diphthongs, diacritic vowels, and base vowels
    triple_letters = [
        "eai", "eau", "iai", "iau", "iei", "ieu", "ioi", "oai",
    ]
    double_letters = [
        "ea", "oa", "ia", "ie", "io", "iu", "ua", "uă",
        "ai", "ăi", "âi", "îi", "ei", "oi", "ui",
        "au", "ău", "âu", "îu", "eu", "ou",
    ]
    accented_letters = ["ă", "â", "î"]
    single_letters = ["a", "e", "i", "o", "u"]

    triple_letter_pattern = "|".join(triple_letters)
    double_letter_pattern = "|".join(double_letters)
    accented_letter_pattern = "|".join(accented_letters)
    single_letter_pattern = "|".join(single_letters)

    nucleuspattern = "%s|%s|%s|%s" % (
        triple_letter_pattern,
        double_letter_pattern,
        accented_letter_pattern,
        single_letter_pattern,
    )
    oncpattern = re.compile("(.*?)(%s)(.*)" % nucleuspattern)

    def transform(self, input_sequence, frequency=1):
        return self.pre_transform(input_sequence, frequency=frequency, language=self)
