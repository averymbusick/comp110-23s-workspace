"""Testing space for functions established in EX05."""

__author__ = "730313069"

from exercises.ex05.utils import only_evens, sub, concat


def test_one_even() -> None:  # use case
    """Asserts that when given a list of random numbers, only even is returned."""
    assert only_evens([1, 2, 3]) == [2]


def test_no_evens() -> None:  # edge case- should return an empty list when given no evens
    """Asserts that an empty list is returned when no evens are present."""
    assert only_evens([1, 3, 5]) == []


def test_all_even() -> None:  # use case
    """Returns entire list when all even."""
    assert only_evens([4, 4, 4]) == [4, 4, 4]


def test_two_lists() -> None:  # use case
    """Asserts concat puts list2 after list1."""
    assert concat([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]

def test_empty_list1() -> None:  # edge case- empty list1
    """Asserts list2 is still printed when list1 empty."""
    assert concat([], [4, 5, 6]) == [4, 5, 6]


def test_all_empty() -> None:  # edge case- two empty lists
    "Asserts that an empty list is returned when empty lists given."
    assert concat([], []) == []


def test_different_length() -> None:  # use case
    """Asserts that lists can be added withs different lengths."""
    assert concat([100, 200], [300]) == [100, 200, 300]


def test_normal() -> None:  # use case
    """Asserts that when given a beginning and end idx, only the indexes in range are returned."""
    assert sub([10, 20, 30, 40], 1, 3) == [20, 30]


def test_negative_start() -> None:  # edge case
    """Assserts that when start_idx is a negative number, it is changed to 0."""
    assert sub([1, 2, 3, 4, 5], -5, 3) == [1, 2, 3]


def test_zero_end() -> None:  # edge case
    """Asserts that an empty list is returned when end idx is 0."""
    assert sub([50, 60, 70], 1, 0) == []


def test_high_start() -> None:  # edge case
    """Asserts that if start idx is higher than len(list), an empty list is returned."""
    assert sub([1, 2], 5, 2) == []


def test_one_elem() -> None:  # use case
    """Asserts that function works with list of one element."""
    assert sub([500], 0, 1) == [500]