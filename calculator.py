def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

# Function to calculate the percentage of a number
def percentage(part, whole):
    if whole == 0:
        return "Error: Cannot calculate percentage of zero"
    return (part / whole) * 100