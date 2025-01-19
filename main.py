def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

if __name__ == "__main__":
    # Example usage (optional, not needed for unit tests)
    x = 5
    y = 3
    print(f"The sum of {x} and {y} is: {add(x, y)}")
    print(f"The difference of {x} and {y} is: {subtract(x, y)}")
    print(f"The product of {x} and {y} is: {multiply(x, y)}")
