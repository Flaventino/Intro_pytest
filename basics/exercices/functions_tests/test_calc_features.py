from basics.exercices.src.fonction_simple import add, divide, add_integer, alea_uniform
import pytest

# Tests exercices functions
# 1. `add` function
def test_add_function_on_positive_integers():
    assert add(3,5) == 8

def test_add_function_on_positive_floats():
    assert add(3.1,5.5) == 8.6

def test_add_function_on_negative_values():
    assert add(-3.1,2) == -1.1

# 2. `divide` function
def test_integers_division():
    assert divide(50, 10) == 5.0

def test_floats_division():
    assert divide(10.6, 2) == 5.3

def test_division_by_0():
    pass

# 3. `add_integer` function
def test_integers_sum():
    assert add_integer(50, 10) == 60

def test_floats_sum():
    with pytest.raises(TypeError):
        add_integer(10.6, 2)
    with pytest.raises(TypeError):
        add_integer(2, 5.5)


# 4. `alea_unidorm` function
def test_alea_uniform():
    value = alea_uniform(5,15)
    assert isinstance(value, float) and (5 < value < 15)