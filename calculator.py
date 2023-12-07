# calculator.py
def calculator(a, b, operation):
    if operation == 'addition':
        return a + b
    elif operation == 'subtraction':
        return a - b
    elif operation == 'multiplication':
        return a * b
    elif operation == 'division':
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"
