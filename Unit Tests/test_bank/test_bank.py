from bank import value


def test_starts_with_hello():
    assert value("hello")==0
    assert value("hello, how are you?")==0
    assert value("HELLO")==0

def test_greeting_with_h():
    assert value("h")==20
    assert value("howdy")==20
    assert value("hey, how are you")==20

def test_case_sens():
    assert value(" hey   ")==20

def test_other_words():
    assert value("what a wonderful day")==100
