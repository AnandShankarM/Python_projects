import art
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

print(art.logo)
n1 = float(input("What's the first number: "))
is_running = True
while is_running:
    for symbols in operations:
        print(symbols)
    operation_symbol = input("Pick an operation: ")
    n2 = float(input("What's the next number: "))
    print(f"{n1} {operation_symbol} {n2} = {operations[operation_symbol](n1, n2)}")
    result = operations[operation_symbol](n1, n2)
    choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

    if choice == 'y':
        n1 = result
    elif choice == 'n':
        print("\n" * 20)
        print(art.logo)
        n1 = float(input("What's the first number: "))
    else:
        print("Thank you for using calculator")
        is_running = False