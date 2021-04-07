import pytest

from ...src.algorithms.sorting import bubble_sort_original, bubble_sort_optimized, is_sorted

unsorted_arr = [200, 76, 32, 10, 7, 378, 1, 4, 8, 4]

def test_bubble_sort_original():
    unsorted_arr_cp = unsorted_arr[:]
    bubble_sort_original(unsorted_arr_cp)
    assert is_sorted(unsorted_arr_cp)


