"""
Unit tests for the calculator functions.
"""
import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    """Test the add function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    """Test the subtract function."""
    assert subtract(5, 3) == 2
    assert subtract(0, 1) == -1
    assert subtract(2, 2) == 0

def test_multiply():
    """Test the multiply function."""
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10
    assert multiply(0, 100) == 0

def test_divide():
    """Test the divide function."""
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

