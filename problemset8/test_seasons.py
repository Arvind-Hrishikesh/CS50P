
from seasons import num_to_words
from seasons import date_to_minutes

def test1():
    assert((num_to_words(date_to_minutes("2021-06-24"))+" minutes")=="Five hundred twenty-five thousand, six hundred minutes")

def test2():
    assert((num_to_words(date_to_minutes("2020-06-24"))+" minutes")=="One million, fifty-one thousand, two hundred minutes")
