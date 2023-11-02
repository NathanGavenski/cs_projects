from copy import deepcopy
from unittest import TestCase
from random import randint
from typing import Callable

from sort_methods import *


class TestSort(TestCase):

    def setUp(self):
        self.unsorted_list = [randint(0, 1000) for _ in range(1000)]
        self.sorted_list = deepcopy(self.unsorted_list)
        self.sorted_list.sort()

    def fn_closure(self, fn: Callable[list[int], list[int]]) -> None:
        sorted_list = fn(self.unsorted_list)
        assert sorted_list == self.sorted_list

    def test_bubble(self) -> None:
        self.fn_closure(bubble_sort)
        self.fn_closure(bubble_sort_improvement)

    def test_bucket(self) -> None:
        self.fn_closure(bucket_sort)

    def test_counting(self) -> None:
        self.fn_closure(counting_sort)

    def test_heap(self) -> None:
        self.fn_closure(heap_sort)

    def test_insertion(self) -> None:
        self.fn_closure(insertion_sort)
        self.fn_closure(insertion_sort_less_code)

    def test_merge(self) -> None:
        self.fn_closure(merge_sort_top_down)
        self.fn_closure(merge_sort_bottom_up)

    def test_quick(self) -> None:
        self.fn_closure(quick_sort)

    def test_radix(self) -> None:
        self.fn_closure(radix_sort)

    def test_selection(self) -> None:
        self.fn_closure(selection_sort)
        self.fn_closure(selection_sort_pythonic)
