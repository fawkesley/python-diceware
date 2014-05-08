# encoding: utf-8

from distutils.core import setup

import codecs
import os
import re


def find_version(*file_paths):
    # Open in Latin-1 so that we avoid encoding errors.
    # Use codecs.open for Python 2 compatibility
    here = os.path.abspath(os.path.dirname(__file__))

    with codecs.open(os.path.join(here, *file_paths), 'r', 'latin1') as f:
        version_file = f.read()

    # The version line must have the form
    # __version__ = 'ver'
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

setup(
    name='diceware',
    version=find_version('diceware', '__init__.py'),
    description='Diceware random password generator',
    author='Paul M Furley',
    author_email='paul@paulfurley.com',
    url='https://github.com/paulfurley/diceware',
    install_requires=['docopt'],
    packages=['diceware'],
    data_files={
        'wordlists': ['wordlists/*.txt'],
    },
    entry_points={
        'console_scripts': [
            'diceware=diceware:main',
        ],
    },
)
