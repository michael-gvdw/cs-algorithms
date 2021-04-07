import pytest

from src.algorithms.search import (linear_search, binary_search, binary_search_recursive, jump_search, 
                                    interpolation_search, exponential_search, fibonacci_search, ternary_search, 
                                    ternary_search_recursive)


arr_includes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr_excludes = [1, 2, 3, 4, 5, 5, 7, 8, 9]

key = 6
index_includes = 5
index_excludes = -1


def test_linear_seach_includes():
    index = linear_search(arr_includes, key)
    assert index_includes == index

def test_linear_seach_excludes():
    index = linear_search(arr_excludes, key)
    assert index_excludes == index

def test_binary_search_includes():
    index = binary_search(arr_includes, key)
    assert index_includes == index

def test_binary_search_excludes():
    index = binary_search(arr_excludes, key)
    assert index_excludes == index

def test_binary_search_recursive_includes():
    index = binary_search_recursive(arr_includes, key)
    assert index_includes == index

def test_binary_search_recursive_excludes():
    index = binary_search_recursive(arr_excludes, key)
    assert index_excludes == index

def test_jump_search_includes():
    index = jump_search(arr_includes, key)
    assert index_includes == index

def test_jump_search_excludes():
    index = jump_search(arr_excludes, key)
    assert index_excludes == index

def test_interpolation_search_includes():
    index = interpolation_search(arr_includes, key)
    assert index_includes == index

def test_interpolation_search_excludes():
    index = interpolation_search(arr_excludes, key)
    assert index_excludes == index

def test_exponential_search_includes():
    index = exponential_search(arr_includes, key)
    assert index_includes == index

def test_exponential_search_excludes():
    index = exponential_search(arr_excludes, key)
    assert index_excludes == index

def test_fibonacci_search_includes():
    index = fibonacci_search(arr_includes, key)
    assert index_includes == index

def test_fibonacci_search_excludes():
    index = fibonacci_search(arr_excludes, key)
    assert index_excludes == index

def test_ternary_search_includes():
    index = ternary_search(arr_includes, key)
    assert index_includes == index

def test_ternary_search_excludes():
    index = ternary_search(arr_excludes, key)
    assert index_excludes == index

def test_ternary_search_recursive_includes():
    index = ternary_search_recursive(arr_includes, key)
    assert index_includes == index

def test_ternary_search_recursive_excludes():
    index = ternary_search_recursive(arr_excludes, key)
    assert index_excludes == index



