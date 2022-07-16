from numb3rs import validate

def test_correct_input():
    assert(validate("127.0.0.1") == True)

def test_incorrect_input1():
    assert(validate("255.255.255.255")==True)

def test_incorrect_input2():
    assert(validate("512.512.512.512")==False)

def test_incorrect_input3():
    assert(validate("75.456.76.65")==False)

def test_incorrect_input4():
    assert(validate("cat")==False)

