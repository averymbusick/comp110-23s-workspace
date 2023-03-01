"""Exercise 04: List utility functions."""

__author__ = "730313069"

def all(list_numbers: list[int], integer: int) -> bool:
    """Returns a bool clarifying if all numbers in the list numbers are the same as the integer"""
    index: int = 0
    while index <= len(list_numbers):
        if list_numbers[index] != integer:  # if each index of the list does not equal the integer searched for
          return False
        else:
           index += 1

def max(input: list[int]) -> int:
    """Returns the max number given a list of integers"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")  # raises ValueError if list is empty
    else:
        index: int = 0
        new_max: int = 0
        while index < len(input):
            if input[index] > new_max:  # if the current index of the list is more than "new max", current index becomes new max
                new_max = input[index]
            else:
                index += 1
        return new_max  # new_max will be the greatest numb in the list
        
def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """Returns true if given two of the same lists with same indices"""
    idx: int = 0
    if len(list_one) != len(list_two):  # returns false automatically if lists are different lengths
        return False
    else:
        while idx < len(list_one):
            if list_one[idx] != list_two[idx]:  # if at any point lists do not match at same index return false
                return False
            else:
                idx += 1
        return True  # all indices matched and true is returned