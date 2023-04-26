"""Challenge Question 04: Dict Function Writing."""

__author__ = "730313069"

def zip(list1: list[str], list2: list[int]) -> dict[str,int]:
    """Produces a dict where the elements of list1 are keys, and values correspond at the same index of list2."""
    new_dict: dict[str, int] = {}
    idx: int = 0
    if len(list1) != len(list2) or len(list1) == 0 or len(list2) == 0:
        return {}
    while idx < len(list1):
        new_dict[list1[idx]] = list2[idx]
        idx += 1
    return new_dict