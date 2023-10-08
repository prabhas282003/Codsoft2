def cal(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2
    else:
        return "Invalid operator"

if __name__ == "__main__":
    try:
        # Prompt the user to input two numbers and an operation
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")
        # Perform the calculation
        r = cal(num1, num2, operation)
        # Display the result
        print("Result:", r)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
