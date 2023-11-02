"""Implementations for selection sort.

Links:
    https://en.wikipedia.org/wiki/Selection_sort

We are using deepcopy so we dont mess up with the variable for the rest of the tests.
If we wanted to reduce memory we should avoid using deepcopy into a list.
"""
from copy import deepcopy


def selection_sort(unsorted_list: list[int]) -> list[int]:
    """Simple selection sort solution"""
    _unsorted_list = deepcopy(unsorted_list)
    sorted_list = []
    while len(_unsorted_list) > 0:
        min_value = _unsorted_list[0]
        for num in _unsorted_list[1:]:
            if min_value > num:
                min_value = num
        _unsorted_list.remove(min_value)
        sorted_list.append(min_value)
    return sorted_list


def selection_sort_pythonic(unsorted_list: list[int]) -> list[int]:
    """A more pythonic way of writing the insertion sort."""
    _unsorted_list = deepcopy(unsorted_list)
    sorted_list = []
    while len(_unsorted_list) > 0:
        min_value = min(_unsorted_list)
        _unsorted_list.remove(min_value)
        sorted_list.append(min_value)
    return sorted_list
