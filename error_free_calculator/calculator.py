import logging

# Configure logging to file
logging.basicConfig(filename='error_log.txt', level=logging.ERROR,
                    format='%(asctime)s %(levelname)s:%(message)s')

def get_number(prompt):
    while True:
        try:
            value = input(prompt)
            number = float(value)
            return number
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            logging.error(f"ValueError occurred: invalid input '{value}'")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print("Oops! Division by zero is not allowed.")
        logging.error(f"ZeroDivisionError occurred: {e}")
        return None

def main():
    print("Welcome to the Error-Free Calculator!")
    while True:
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        choice = input("> ")

        if choice == '5':
            print("Goodbye!")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please enter a number between 1 and 5.")
            continue

        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        try:
            if choice == '1':
                result = add(num1, num2)
            elif choice == '2':
                result = subtract(num1, num2)
            elif choice == '3':
                result = multiply(num1, num2)
            elif choice == '4':
                result = divide(num1, num2)
                if result is None:
                    continue
        except Exception as e:
            print("An unexpected error occurred.")
            logging.error(f"Unexpected error: {e}")
            continue
        else:
            print(f"The result is {result}.")
        finally:
            print("Operation completed.")

if __name__ == "__main__":
    main()
