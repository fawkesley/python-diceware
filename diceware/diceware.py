from __future__ import unicode_literals

_WORDLIST_FILE = 'diceware8k.txt'
import random


def generate_passphrase(number_of_words, delimiter=' '):
    words = list(load_words())
    return delimiter.join(
        [random.choice(words) for count in range(number_of_words)])


def load_words():
    from os.path import abspath, dirname, join as pjoin
    here = abspath(dirname(__file__))
    with open(pjoin(here, '..', 'wordlists', _WORDLIST_FILE), 'r') as f:
        words = set([word.strip() for word in f])
        assert len(words) == 8192
    return words
