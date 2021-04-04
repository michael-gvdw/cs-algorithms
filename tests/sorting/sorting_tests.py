import pytest
import importlib


from ...src.algorithms.sorting import is_sorted


unsorted_list = [200, 76, 32, 10, 7, 378, 1, 4, 8, 4]
sorted_list = [1, 4, 4, 7, 8, 10, 32, 76, 200, 378]


def is_sorted_unsorted_list_test():
    assert not is_sorted(unsorted_list)

def is_sorted_sorted_list_test():
    assert is_sorted(sorted_list)