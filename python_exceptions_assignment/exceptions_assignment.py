# Python Exceptions Assignment
# Author: saman

def handle_division():
    while True:
        try:
            num = input("Enter a number: ")
            number = int(num)
            result = 100 / number
        except ZeroDivisionError:
            print("Oops! You cannot divide by zero.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
        else:
            print(f"100 divided by {number} is {result}.")
            break

def raise_and_handle_exceptions():
    # IndexError
    try:
        lst = [1, 2, 3]
        print(lst[5])
    except IndexError:
        print("IndexError occurred! List index out of range.")

    # KeyError
    try:
        d = {"a": 1, "b": 2}
        print(d["c"])
    except KeyError:
        print("KeyError occurred! Key not found in the dictionary.")

    # TypeError
    try:
        x = "string" + 5
    except TypeError:
        print("TypeError occurred! Unsupported operand types.")

def division_with_try_except():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = num1 / num2
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
    else:
        print(f"The result is {result}.")
    finally:
        print("This block always executes.")

def main():
    print("Task 1 - Understanding Python Exceptions")
    handle_division()
    print("\nTask 2 - Types of Exceptions")
    raise_and_handle_exceptions()
    print("\nTask 3 - Using try...except...else...finally")
    division_with_try_except()

if __name__ == "__main__":
    main()
