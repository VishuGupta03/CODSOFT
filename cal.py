print("Welcome to PYcalculator")

while True:
    a = float(input("Enter the first number: \n"))
    b = float(input("Enter the second number: \n"))
    operation = input("Choose the operation (+, -, *, /): \n")

    if operation == "+":
        print(f"{a} + {b} = {a + b}")
    elif operation == "-":
        print(f"{a} - {b} = {a - b}")
    elif operation == "*":
        print(f"{a} * {b} = {a * b}")
    elif operation == "/":
        if b != 0:
            print(f"{a} / {b} = {a / b}")
        else:
            print("Cannot divide by zero")
    else:
        print("Enter a valid operator")

    another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()

    if another_calculation != 'yes':
        print("Exiting PYcalculator. Goodbye!")
        break




