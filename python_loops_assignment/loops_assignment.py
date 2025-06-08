# Python Loops Assignment
# Author: saman

def countdown_timer():
    # Task 1: Countdown timer using while loop
    start = int(input("Enter the starting number for countdown: "))
    while start > 0:
        print(start, end=" ")
        start -= 1
    print("Blast off! 🚀")

def multiplication_table():
    # Task 2: Multiplication table using for loop
    num = int(input("Enter a number to generate its multiplication table: "))
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

def factorial():
    # Task 3: Factorial calculation using for loop
    num = int(input("Enter a number to calculate its factorial: "))
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    print(f"The factorial of {num} is {fact}.")

def main():
    print("Welcome to the Python Loops Assignment by saman!")
    countdown_timer()
    print("\n")
    multiplication_table()
    print("\n")
    factorial()

if __name__ == "__main__":
    main()
