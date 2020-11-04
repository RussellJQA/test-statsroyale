import pytest


def vowel_count(string: str) -> int:  # I refactored
    """ Returns the number of vowels in the input string """
    if not isinstance(string, str):
        raise ValueError("The input to this function must be a string.")
    vowels = ["a", "e", "i", "o", "u"]
    return sum(1 for ch in string.lower() if ch in vowels)


def test_with_my_first_name():
    assert vowel_count('russell') == 2


def test_with_my_last_name():
    assert vowel_count('johnson') == 2


def test_with_my_name():
    assert vowel_count("russell johnson") == 4


def test_with_my_uppercase_name():
    assert vowel_count("RUSSELL JOHNSON") == 4


# CHALLENGE 1: Write 3 more tests for the vowel_count() function


def test_with_empty_string():
    assert vowel_count("") == 0


def test_with_non_letters():
    assert vowel_count("`1234567890-=[]\\;',./~!@#$%^&*()_+`{}:\"<>?") == 0


def test_with_integer_input():
    with pytest.raises(ValueError):
        vowel_count(7)


# I also added a 4th test which currently fails.
@pytest.mark.xfail
def test_with_unicode():
    """Test whether vowel__count properly handles non-English vowels"""
    assert vowel_count("Iñtërnâtiônàlizætiøn☃💪") == 10
