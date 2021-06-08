import pytest
from programs.count import count

def test_count_zeros():
    assert count([0,0,0], 0) == 3

def test_count_string():
    assert count(["a","a","a"], "a") == 3