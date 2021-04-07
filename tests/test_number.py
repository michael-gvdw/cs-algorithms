import pytest

from src.algorithms.number import fibonacci, factorial

def test_fibonacci():
    assert 34 == fibonacci(9)

def test_factorial():
    assert 120 == factorial(5)