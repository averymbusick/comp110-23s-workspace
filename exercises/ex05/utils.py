"""EX05: 'list' utility functions."""

__author__ = "730313069"

def only_evens(given_list: list[int]) -> list[int]:
    """Given a list of ints, will return a new list with only even ints."""
    even_list: list[int] = []
    for num in given_list:  # for every number in the list, if the remainder when divided by 2 is 0, add to new list of even numbs
        if num % 2 == 0:
            even_list.append(num)
    return even_list

def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Given two lists, returns a new list with all elements of list1 followed by list2."""
    new_list: list[int] = []
    for elem in list1:  # append each elem of list1 to new list
        new_list.append(elem)
    for elem in list2:  # then append each elem of list2 to new list already including list1
        new_list.append(elem)
    return new_list

def sub(a_list: list[int], start_idx: int, end_idx: int) -> list[int]:
    """Given a list, returns a new list with only ints between the given start and end index."""
    subset: list[int] = []
    if start_idx < 0:  # Handles if the start idx is a negative number, sets it to 0
        start_idx = 0
    if end_idx > len(a_list):  # Handles if end idx is higher than len of list, sets it as len of list
        end_idx = int(len(a_list))
    if len(a_list) == 0 or end_idx < 0 or start_idx > len(a_list):  # returns an empty list if given list len is 0, if end idx is less than 0 or if start idx is longer than len(list)
        return []
    for idx in range(start_idx, end_idx):  # for every index within the range of the start and end idx, append it to the subset list
        subset.append(a_list[idx])
    return subset