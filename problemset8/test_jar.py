from jar import Jar
import pytest

def test_init():
    jar=Jar()
    assert isinstance(jar,Jar)
    assert(jar.capacity==12)

def test_str():
    jar=Jar(10)
    jar.deposit(5)
    assert(str(jar)=="🍪🍪🍪🍪🍪")

def test_deposit():
    jar=Jar(10)
    jar.deposit(5)
    assert(jar.size()==5)
    with pytest.raises(ValueError):
        jar.deposit(2)
        jar.deposit(7)

def test_withdraw():
    jar=Jar()
    jar.deposit(5)
    before=jar.size()
    jar.withdraw(3)
    after=jar.size()
    assert((before-after)==3)
    with pytest.raises(ValueError):
        jar.withdraw(1)
        jar.withdraw(5)

def test_emptyjar():
    jar=Jar(10)
    assert(jar.size()==0)