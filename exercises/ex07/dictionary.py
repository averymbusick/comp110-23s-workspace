"""EX07: Dictionary Function Skeletons and Implementations."""

__author__ = "730323069"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Given a dictionary, invert will return a dictionary with inverted keys and values."""
    inverse_dict: dict[str, str] = {}
    for key, value in dictionary.items():  # checking both keys and values 
        if value in inverse_dict:  # if the value that comes up is already in inverse, an error is raised
            raise KeyError("Cannot produce inverse dictionary due to repeating values.")
        inverse_dict[value] = key  # adding the keys and values to the inverse in reverse order flipping thru all keys/values
    return inverse_dict


def favorite_color(color_list: dict[str, str]) -> str:
    """Given a dictionary of names and attached favorite colors, favorite_colors will return the most common favorite color."""
    color_count: dict[str, int] = {}
    for color in color_list.values():
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    max_count: int = max(color_count.values())
    for color in color_list.values():
        if color_count[color] == max_count:
            return color


def count(list: list[str]) -> dict[str, int]:
    """Given a list of str, returns a dict with the strs from the list, and a count of how many times they occurred in the list."""
    new_dict: dict[str, int] = {}
    for item in list:  # flip through all items in original list
        if item in new_dict:  # if current item is already added to new dict, add 1 to the value
            new_dict[item] += 1
        else:  # if not, the current item must be only listed once
            new_dict[item] = 1
    return new_dict
