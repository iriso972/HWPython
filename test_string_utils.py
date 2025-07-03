import pytest
from string_utilis import StringUtils

string_utils = StringUtils()

# capitalize


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello, world", "Hello, world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

# trim


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" Skypro", "Skypro"),
    ("Hello, world", "Hello, world"),
    (" 123 cry", "123 cry"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("None", "None"),        
    ("", ""),  
    ("   ", ""),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

# contains


@pytest.mark.positive  
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Skypro", "S", True),
    ("Hello, world", "W", False),
    ("-2 cry", "-2", True),
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [       
    ("", "a", False),
    ("   ", "", True),
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected

# delete_symbol


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Sully", "S", "ully"),
    ("Hello, world", ",", "Hello world"),
    ("123 cry", "2", "13 cry"),
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [       
    ("", "a", ""),
    ("  ", "  ", ""),
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected