"""
Basic Calculator with functions for add, subtract, multiply, and divide.
"""

def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Return the difference between two numbers."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b

def divide(a: float, b: float) -> float:
    """Return the division of two numbers. Raises an error if dividing by zero."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return a / b

