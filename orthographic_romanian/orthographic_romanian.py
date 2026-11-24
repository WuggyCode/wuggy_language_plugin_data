"""Romanian orthographic language plugin for Wuggy (WuggyCode/wuggy).

Word list and canonical syllabifications are derived from RoLEX (The Romanian
Lexicon; Lőrincz, Irimia, Stan, & Barbu Mititelu, 2022, Natural Language
Engineering, https://github.com/adrianastan/rolex), with frequencies computed
from Romanian Wikipedia (`wikimedia/wikipedia`, `20231101.ro`).
"""

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

    # Longest intra-syllabic vocalic nuclei first (quadriphthongs, triphthongs,
    # diphthongs / geminate 'ii', diacritic vowels, and base vowels).
    # Non-syllabic final '-i' (e.g. 'ani', 'oameni', 'aceleași', 'români') remains
    # in the final syllable coda.
    quad_letters = ["ioai", "eoai", "euai"]
    triple_letters = [
        "eai", "eau", "eoa", "eao", "eia",
        "iai", "iau", "iei", "ieu", "ioa", "ioi",
        "oai", "oau", "uai", "uau", "uei", "uie", "uio",
    ]
    double_letters = [
        "ii", "ea", "oa", "ia", "ie", "io", "iu", "ua", "uă",
        "eo", "ue", "iă", "uâ", "aa", "ee", "oo", "uu",
        "ai", "ăi", "âi", "îi", "ei", "oi", "ui",
        "au", "ău", "âu", "îu", "eu", "ou",
    ]
    accented_letters = ["ă", "â", "î"]
    single_letters = ["a", "e", "i", "o", "u"]

    quad_letter_pattern = "|".join(quad_letters)
    triple_letter_pattern = "|".join(triple_letters)
    double_letter_pattern = "|".join(double_letters)
    accented_letter_pattern = "|".join(accented_letters)
    single_letter_pattern = "|".join(single_letters)

    nucleuspattern = "%s|%s|%s|%s|%s" % (
        quad_letter_pattern,
        triple_letter_pattern,
        double_letter_pattern,
        accented_letter_pattern,
        single_letter_pattern,
    )
    oncpattern = re.compile("(.*?)(%s)(.*)" % nucleuspattern)

    def transform(self, input_sequence, frequency=1):
        return self.pre_transform(input_sequence, frequency=frequency, language=self)
