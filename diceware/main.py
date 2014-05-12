#!/usr/bin/env python
# encoding: utf-8

"""
Diceware random password generator.

Warning: This is not as secure as really rolling a dice!

Usage:
    diceware [--length=<words>] [--repeat=<count>]
    diceware -h | --help
    diceware --version

Options:
    --length=<words>   Number of diceware words to generate. [default: 6]
    --repeat=<count>  Number of passphrases to generate. [default: 10]
"""

from __future__ import unicode_literals

from docopt import docopt
from .diceware import generate_passphrase


def main():
    from __init__ import __version__
    arguments = docopt(__doc__, version='diceware {}'.format(__version__))
    number_of_words = int(arguments['--length'])
    number_of_passphrases = int(arguments['--repeat'])

    for i in xrange(number_of_passphrases):
        print(generate_passphrase(number_of_words))
