"""Bubble sort

Link:
    https://en.wikipedia.org/wiki/Bubble_sort
"""


def bubble_sort(unsorted_list: list[int]) -> list[int]:
    """Simple bubble sort solution"""
    while True:
        update = False

        for idx in range(len(unsorted_list) - 1):
            if unsorted_list[idx] > unsorted_list[idx + 1]:
                update = True
                first_item = unsorted_list[idx]
                second_item = unsorted_list[idx + 1]
                unsorted_list[idx + 1] = first_item
                unsorted_list[idx] = second_item

        if not update:
            break
    return unsorted_list

def bubble_sort_improvement(unsorted_list: list[int]) -> list[int]:
    """Improved bubble sort."""
    for i in range(len(unsorted_list), 0, -1):
        update = False
        for idx in range(i -1):
            if unsorted_list[idx] > unsorted_list[idx + 1]:
                update = True
                first_item = unsorted_list[idx]
                second_item = unsorted_list[idx + 1]
                unsorted_list[idx + 1] = first_item
                unsorted_list[idx] = second_item

        if not update:
            break
    return unsorted_list
