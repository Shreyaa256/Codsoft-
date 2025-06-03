def calculator():
    print("Simple Calculator")
    print("Choose an operation:")
    print("1: Addition (+)")
    print("2: Subtraction (-)")
    print("3: Multiplication (*)")
    print("4: Division (/)")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation number (1/2/3/4): ")

        if operation == '1':
            result = num1 + num2
            op_symbol = '+'
        elif operation == '2':
            result = num1 - num2
            op_symbol = '-'
        elif operation == '3':
            result = num1 * num2
            op_symbol = '*'
        elif operation == '4':
            if num2 == 0:
                print("Error: Cannot divide by zero")
                return
            result = num1 / num2
            op_symbol = '/'
        else:
            print("Invalid operation choice")
            return

        print(f"{num1} {op_symbol} {num2} = {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    calculator()

