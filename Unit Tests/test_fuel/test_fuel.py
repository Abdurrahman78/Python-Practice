from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("3/4")==75
    assert convert("1/4")==25
    assert convert("1/100")==1
    assert convert("99/100")==99

def test_value_error():
    with pytest.raises(ValueError):
        convert("100/5")

def test_zero_error():
    with pytest.raises(ZeroDivisionError):
        convert("100/0")

def test_gauge():
    assert gauge(88)=='88%'
    assert gauge(1)=='E'
    assert gauge(0)=='E'
    assert gauge(100)=='F'
    assert gauge(99)=='F'


