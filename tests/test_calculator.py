import pytest
import sys
import os

# Add the project root directory to Python's module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import calculate  # Now import should work


def test_calculator():
    """Basic test for calculator."""
    assert calculate(5, 3, "add") == "The result of 5 add 3 is equal to 8"
 
