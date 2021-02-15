import string

# pip installed
import pytest  # installed with webdriver_manager
""" CHALLENGE 2: Write a new function that takes a string
(e.g., "A cow jumped over the moon")
and returns both the shortest and longest words within it.

Write as many tests as you need to assert that your
function works as expected.
"""


def len_and_alpha(word):
    return str(len(word)) + word


def shortest_and_longest(input_string):
    if not isinstance(input_string, str):
        raise ValueError("The input to this function must be a string.")
    elif not set(input_string).issubset(
            set(string.ascii_uppercase + string.ascii_lowercase + " ")):
        raise ValueError(
            "Input may only contain uppercase and/or lowercase letters,"
            " and spaces.")
    elif not len(input_string.strip()):
        raise ValueError("The input must contain more than just blanks.")

    # Sort words by length. For words of the same length, sort alphabetically.
    words = sorted(input_string.split(), key=len_and_alpha)

    return words[0], words[-1]


def test_with_integer_input():
    with pytest.raises(ValueError):
        shortest_and_longest(747)


def test_with_non_letters():
    with pytest.raises(ValueError):
        shortest_and_longest("`1234567890-=[]\\;',./~!@#$%^&*()_+`{}:\"<>?")


def test_with_blanks():
    with pytest.raises(ValueError):
        shortest_and_longest(" ")


def test_happy():
    assert shortest_and_longest("A cow jumped over the moon") == ("A",
                                                                  "jumped")


def test_happy_ordered_by_alpha():
    assert shortest_and_longest("A cow jumped moon over the") == ("A",
                                                                  "jumped")


def test_happy_ordered_by_alpha_reversed():
    assert shortest_and_longest("the over moon jumped cow A") == ("A",
                                                                  "jumped")


def test_happy_ordered_by_reverse_len():
    assert shortest_and_longest("jumped over moon the cow A") == ("A",
                                                                  "jumped")
