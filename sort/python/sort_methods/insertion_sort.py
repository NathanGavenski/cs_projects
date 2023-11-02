"""Insertion sort.

Links:
    https://en.wikipedia.org/wiki/Insertion_sort
"""


def insertion_sort(unsorted_list: list[int]) -> list[int]:
    """Simple insertion sort implementation."""
    sorted_list = []
    for num in unsorted_list:
        if len(sorted_list) == 0:
            sorted_list.append(num)
            continue
        for idx, sorted_num in enumerate(sorted_list):
            if num < sorted_num:
                sorted_list = sorted_list[:idx] + [num] + sorted_list[idx:]
                break
        else:
            sorted_list.append(num)
    return sorted_list


def insertion_sort_less_code(unsorted_list: list[int]) -> list[int]:
    """simple insertion sort implementation."""
    sorted_list = [unsorted_list[0]]
    for num in unsorted_list[1:]:
        for idx, sorted_num in enumerate(sorted_list):
            if num < sorted_num:
                sorted_list = sorted_list[:idx] + [num] + sorted_list[idx:]
                break
        else:
            sorted_list.append(num)
    return sorted_list
