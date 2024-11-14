'''6) Create a package with name mathlib and add at least 5 related modules into it. Test each of these modules in
another application by importing them.'''

# add.py- addition module
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

# subtract.py-substraction module
def subtract(a, b):
    """Returns the difference of two numbers."""
    return a - b

# multiply.py- multiplication module
def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b


# divide.py - Division module
def divide(a, b):
    """Returns the quotient of two numbers. Raises an error if dividing by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

 # power.py- power calculation module
def power(base, exponent):
    """Returns the result of raising base to the power of exponent."""
    return base ** exponent

#importing it

# test_mathlib.py

# Import modules from the mathlib package
from mathlib import add, subtract, multiply, divide, power

# Test the addition function
print("Addition:", add.add(3, 5))  # Expected output: 8

# Test the subtraction function
print("Subtraction:", subtract.subtract(10, 4))  # Expected output: 6

# Test the multiplication function
print("Multiplication:", multiply.multiply(2, 7))  # Expected output: 14

# Test the division function
try:
    print("Division:", divide.divide(20, 4))  # Expected output: 5.0
    print("Division by zero test:", divide.divide(10, 0))  # Expected to raise an error
except ValueError as e:
    print(e)

# Test the power function
print("Power:", power.power(2, 3))  # Expected output: 8
