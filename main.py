import sys

def calculate(a, b, operation):
    """Performs a basic calculator operation"""
    try:
        a, b = float(a), float(b)  # Convert inputs to numbers
    except ValueError:
        return f"Invalid number input: {a} or {b} is not a valid number."

    if operation == "add":
        return f"The result of {a} add {b} is equal to {a + b}"
    elif operation == "subtract":
        return f"The result of {a} subtract {b} is equal to {a - b}"
    elif operation == "multiply":
        return f"The result of {a} multiply {b} is equal to {a * b}"
    elif operation == "divide":
        return f"The result of {a} divide {b} is equal to {a / b}" if b != 0 else "An error occurred: Cannot divide by zero"
    else:
        return f"Unknown operation: {operation}"

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python main.py <num1> <num2> <operation>")
    else:
        num1, num2, operation = sys.argv[1], sys.argv[2], sys.argv[3]
        print(calculate(num1, num2, operation))
