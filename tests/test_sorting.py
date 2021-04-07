import pytest
import importlib


from src.algorithms.sorting import (is_sorted, bubble_sort_original, bubble_sort_optimized, 
                                    selection_sort, insertion_sort, merge_sort, quick_sort, 
                                    binary_insertion_sort)


unsorted_list = [8, 3, 5, 1, 2, 9, 4, 6, 7]
sorted_ascending_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sorted_descending_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]


def test_is_sorted_unsorted():
    assert not is_sorted(unsorted_list)

def test_is_sorted_sorted_ascending():
    assert is_sorted(sorted_ascending_list)

def test_is_sorted_sorted_descending():
    assert is_sorted(sorted_descending_list)

def test_is_sorted_empty_list():
    assert is_sorted([])

def test_is_sorted_one_item_list():
    assert is_sorted([0])

def test_bubble_sort_original():
    unsorted_list_cp = unsorted_list[:]
    bubble_sort_original(unsorted_list_cp)
    assert is_sorted(unsorted_list_cp)

def test_bubble_sort_optimized():
    unsorted_list_cp = unsorted_list[:]
    bubble_sort_optimized(unsorted_list_cp)
    assert is_sorted(unsorted_list_cp)

def test_selection_sort():
    unsorted_list_cp = unsorted_list[:]
    selection_sort(unsorted_list_cp)
    assert is_sorted(unsorted_list_cp)

def test_insertion_sort():
    unsorted_list_cp = unsorted_list[:]
    insertion_sort(unsorted_list_cp)
    assert is_sorted(unsorted_list_cp)

def test_merge_sort():
    unsorted_list_cp = unsorted_list[:]
    merge_sort(unsorted_list_cp)
    assert is_sorted(unsorted_list_cp)

def test_quick_sort():
    unsorted_list_cp = unsorted_list[:]
    quick_sort(unsorted_list_cp)
    assert is_sorted(unsorted_list_cp)

def test_binary_insertion_sort():
    unsorted_list_cp = unsorted_list[:]
    temp = binary_insertion_sort(unsorted_list_cp)
    assert is_sorted(temp)

def test_foo():
    assert False