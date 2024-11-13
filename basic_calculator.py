# Define the main function
def main():
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))
    enter_number()

# Define the operations function
def enter_number():
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == '+':
            print(f"Result: {num1 + num2}")
        elif operator == '-':
            print(f"Result: {num1 - num2}")
        elif operator == '*':
            print(f"Result: {num1 * num2}")
        elif operator == '/':
            if num2 != 0:
                print(f"Result: {num1 / num2}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid operator. Please enter +, -, *, or /.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Call the function if the program is runned inside the program
if __name__ == "__main__":
    main()
