import pytest
from faker import Faker
import random

fake = Faker()

# Allow passing --num_records to pytest
def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=10, type=int, help="Number of test records")

@pytest.fixture(scope="session")
def num_records(request):
    return request.config.getoption("--num_records")

@pytest.fixture
def fake_calculator_data():
    """Generates random test data for calculator operations."""
    operations = ['add', 'subtract', 'multiply', 'divide']
    
    a = fake.random_int(min=1, max=100)  
    b = fake.random_int(min=1, max=100)  
    operation = random.choice(operations)  

    if operation == "add":
        expected_result = a + b
    elif operation == "subtract":
        expected_result = a - b
    elif operation == "multiply":
        expected_result = a * b
    elif operation == "divide":
        expected_result = a / b if b != 0 else "An error occurred: Cannot divide by zero"

    return a, b, operation, expected_result
 
