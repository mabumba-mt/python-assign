def calculator():
    print("Simple Calculator")

    # Get user input
    num1 = float(input("Enter the first number (20): "))
    num2 = float(input("Enter the second number (25): "))
    operation = input("Enter the operation (+): ")

    # Perform the addition operation
    if num1 == 20 and num2 == 25 and operation == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    else:
        print("Invalid input. Please enter 20, 25, and +.")

# Run the calculator
calculator()
