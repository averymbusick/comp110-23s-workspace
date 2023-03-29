"""EX07: A testing space for functions established in dictionary."""

__author__ = "730313069"

from exercises.ex07.dictionary import invert, favorite_color, count
import pytest


def test_normal_dict() -> None:
    """Use case test #1 to make sure that given a dict w no repeats, it will inverse."""
    assert invert({'a': 'z', 'b': 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_double_key() -> None:
    """Use case test #2 to make sure a key error is raised with non-unique values."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_empty_dict() -> None:
    """Edge case for inverting an empty dictionary."""
    assert invert({}) == {}


def test_clear_winner() -> None:
    """Use case #1 for when there is a clear winner. In this case: blue."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "blue"


def test_test_tie() -> None:
    """Use case #2 for a case of tie colors. Asserts the first color listed is printed."""
    assert favorite_color({'Avery': 'blue', 'Emily': 'green', 'Kate': 'green', 'Marg': 'blue'}) == "blue"


def test_two_colors() -> None:
    """Edge case to test when there are only two colors listed that the first is printed."""
    assert favorite_color({'Avery': 'blue', 'Emily': 'green'})
   

def test_some_repeats() -> None:
    """Use case #1 to test a normal list with some repeats."""
    assert count(['bananas', 'apples', 'oranges', 'bananas', 'apples', 'bananas']) == {'bananas': 3, 'apples': 2, 'oranges': 1}


def test_all_same() -> None:
    """Use case #2 to test when the list is all the same item."""
    assert count(['eggs', 'eggs', 'eggs', 'eggs']) == {'eggs': 4}
   

def test_empty_list() -> None:
    """Edge case to test when an empty list is given that an empty dict will be returned."""
    assert count([]) == {}