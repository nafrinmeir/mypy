
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": "add",
    '-': "subtract",
    "*": "multiply",
    "/": "divide"
}

num1 = int(input("what's the first number? "))

for symbol in operations:
    print(symbol)

operations_symbol = input("pice an operation from the line above: ")

num2 = int(input("what's the second number? "))

calculation_function = operations[operations_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {operations_symbol} {num2} = {answer}")