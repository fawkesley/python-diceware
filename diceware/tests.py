from nose.tools import assert_equal
from diceware import load_words


def test_load_words():
    words = load_words()
    assert_equal(8192, len(words))
