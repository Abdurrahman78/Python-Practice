from twttr import shorten


def test_vowel():
    assert shorten("twitter")=="twttr"

def test_upper_case_():
    assert shorten("TWITTER")=="TWTTR"

def test_all_vowels():
    assert shorten("aeiou")==""

def test_numbers():
    assert shorten("twitter123")=="twttr123"

def test_puncuation():
    assert shorten("twitter!!!!")=="twttr!!!!"
