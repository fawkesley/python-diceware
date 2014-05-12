from __future__ import unicode_literals

import random
from os.path import abspath, dirname, join as pjoin

_WORDLIST_FILE = 'diceware8k.txt'


def generate_passphrase(number_of_words, delimiter=' '):
    sysrandom = random.SystemRandom()

    words = list(load_words())
    return delimiter.join(
        [sysrandom.choice(words) for count in range(number_of_words)])


def load_words():
    here = abspath(dirname(__file__))
    with open(pjoin(here, '..', 'wordlists', _WORDLIST_FILE), 'r') as f:
        words = set([word.strip() for word in f])
        assert len(words) == 8192
    return words
