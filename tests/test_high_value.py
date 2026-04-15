from lib.high_value import *

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