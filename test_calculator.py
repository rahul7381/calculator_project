"""
Unit tests for the Calculator class and its methods.
"""
import pytest
from calculator import Calculator  # Import the Calculator class


# Parameterized Tests for Arithmetic Operations
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, -1, -2),
    (0, 5, 5),
    (10, -5, 5)
])
def test_add(a, b, expected):
    """Test add with parameterized inputs."""
    assert Calculator.add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (-5, -3, -2),
    (0, 0, 0),
    (100, 50, 50)
])
def test_subtract(a, b, expected):
    """Test subtract with parameterized inputs."""
    assert Calculator.subtract(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-2, 5, -10),
    (0, 100, 0),
    (7, -7, -49)
])
def test_multiply(a, b, expected):
    """Test multiply with parameterized inputs."""
    assert Calculator.multiply(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (-9, 3, -3),
    (100, -10, -10)
])
def test_divide(a, b, expected):
    """Test divide with parameterized inputs."""
    assert Calculator.divide(a, b) == expected


def test_divide_by_zero():
    """Test division by zero raises an error."""
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(10, 0)


# Tests for History Management
def test_calculation_history():
    """Test that history stores calculations correctly."""
    Calculator.clear_history()  # Start fresh

    # Add calculations to history
    Calculator.add(1, 2)
    Calculator.subtract(5, 3)

    # Test the length of history
    assert len(Calculator.get_all_history()) == 2

    # Test the last calculation
    last_calc = Calculator.get_last_calculation()
    assert str(last_calc) == "5 subtract 3 = 2"


def test_clear_history():
    """Test that clearing history works."""
    Calculator.clear_history()
    assert len(Calculator.get_all_history()) == 0

