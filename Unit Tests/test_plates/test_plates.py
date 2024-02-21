from plates import is_valid


def test_start_with_two_letters():
    assert is_valid("CS50")==True
    assert is_valid("C150")==False
    assert is_valid("2250")==False

def test_max_min():
    assert is_valid("CS")==True
    assert is_valid("CS1000")==True
    assert is_valid("CS1000000")==False
    assert is_valid("C")==False
    assert is_valid("1")==False

def test_middle_numbers():
    assert is_valid("AAA222")==True
    assert is_valid("AAA22A")==False
    assert is_valid("CS0")==False

def test_no_puncuations():
    assert is_valid("CS!")==False
    assert is_valid("CS 1")==False
    assert is_valid("CS...")==False

