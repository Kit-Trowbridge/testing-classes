from lib.high_value import *

def test_attributes_are_correct_when_instantiated():
    high_value = HighValue(3, 10)
    result1 = high_value.value_first
    result2 = high_value.value_second
    assert result1 == 3 and result2 == 10

def test_high_value_returns_first_value_is_higher():
    high_value = HighValue(10, 5)
    result = high_value.get_highest()
    assert result == "First value is higher"

def test_high_value_returns_second_value_is_higher():
    high_value = HighValue(5, 10)
    result = high_value.get_highest()
    assert result == "Second value is higher"

def test_high_value_returns_values_as_equal():
    high_value = HighValue(5, 5)
    result = high_value.get_highest()
    assert result == "Values are equal"

def test_high_value_returns_first_value_when_adding():
    high_value = HighValue(5, 5)
    high_value.add(2, "first")
    result = high_value.get_highest()
    assert result == "First value is higher"





