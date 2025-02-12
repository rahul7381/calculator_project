"""
Advanced Calculator with calculation history.
"""

class Calculation:
    """Represents a single calculation."""
    def __init__(self, operation: str, a: float, b: float, result: float):
        self.operation = operation  # Operation type (add, subtract, etc.)
        self.a = a  # First operand
        self.b = b  # Second operand
        self.result = result  # Result of the operation

    def __repr__(self) -> str:
        """Return a string representation of the calculation."""
        return f"{self.a} {self.operation} {self.b} = {self.result}"


class Calculator:
    """A calculator with support for history and operations."""
    history = []  # Class-level variable to store calculation history

    # Static Methods for Arithmetic Operations
    @staticmethod
    def add(a: float, b: float) -> float:
        """Perform addition and store in history."""
        result = a + b
        Calculator.history.append(Calculation("add", a, b, result))
        return result

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Perform subtraction and store in history."""
        result = a - b
        Calculator.history.append(Calculation("subtract", a, b, result))
        return result

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Perform multiplication and store in history."""
        result = a * b
        Calculator.history.append(Calculation("multiply", a, b, result))
        return result

    @staticmethod
    def divide(a: float, b: float) -> float:
        """Perform division and store in history. Raise error if dividing by zero."""
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        result = a / b
        Calculator.history.append(Calculation("divide", a, b, result))
        return result

    # Class Methods for Managing History
    @classmethod
    def get_last_calculation(cls):
        """Return the last calculation in the history."""
        return cls.history[-1] if cls.history else None

    @classmethod
    def get_all_history(cls):
        """Return the entire calculation history."""
        return cls.history

    @classmethod
    def clear_history(cls):
        """Clear the calculation history."""
        cls.history = []

