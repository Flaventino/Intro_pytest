from basics.src.inverse import inverse
from basics.exercices.src.fonction_simple import add, divide, add_integer, alea_uniform
import pytest

# Test examples
def test_example():
    assert 1 == 1
    assert 2 == 2
    #assert 3 == 3

# Tests inverse function
def test_long_list():
    assert inverse(['a', 'b', 'c', 'd', 'e']) == 'edcba'

def test_4_items_list():
    assert inverse(['a', 'b', 'c', 'd']) == 'cba'

def test_integer_fail():
    with pytest.raises(ValueError): #Equivalent to test error  raising from function to test
        inverse(87)

def test_4_chars_string():
    assert inverse('hell') == 'lleh'