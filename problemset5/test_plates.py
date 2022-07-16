from plates import is_valid

def test_one():
    assert is_valid("CS50")==True

def test_two():
    assert is_valid("CS05")==False

def test_three():
    assert is_valid("CS50P")==False

def test_four():
    assert is_valid("PI3.14")==False

def test_five():
    assert is_valid("h")==False

def test_six():
    assert is_valid("outatime")==False

def test_seven():
    assert is_valid("12345")==False