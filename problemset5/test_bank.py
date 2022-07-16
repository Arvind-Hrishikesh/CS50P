from bank import value

def test_one():
    assert value("Hello")==0

def test_two():
    assert value("Hi there")==20

def test_three():
    assert value("..hello there")==100

def test_four():
    assert value("Namaste")==100