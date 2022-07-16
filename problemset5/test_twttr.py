from twttr import shorten

def test_one():
    assert shorten("Arvind")=="rvnd"

def test_two():
    assert shorten("HRISHIKESH")=="hrshksh".upper()

def test_number():
    assert shorten("CS50")=="CS50"

def test_punc():
    assert shorten("Hi, I am Arvind")=="H,  m rvnd"
