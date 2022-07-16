from fuel import convert
from fuel import gauge

import pytest

def test_one():
    assert convert("3/4")==75
    assert gauge(75)=="75%"

def test_two():
    assert convert("1/4")==25
    assert gauge(25)=="25%"

def test_three():
    assert convert("0/4")==0
    assert gauge(0)=="E"

def test_four():
    assert convert("4/4")==100
    assert gauge(100)=="F"

def test_five():
    with pytest.raises(ValueError):
        convert("4/3")

def test_six():
    with pytest.raises(ValueError):
        convert("1.5/3")

#def test_six():
#    with pytest.raises(ZeroDivisionError):
#        convert("1/0")
