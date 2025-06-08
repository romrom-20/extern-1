# main.py

# --- Task 1: Variables: Your First Python Intro ---
print("--- Task 1: Variables ---")

# Creating variables to describe myself 
name = "Saman Seshadri"  # A string variable for the name
age = 21  # An integer variable for age (
height = 6.0  # A floating-point variable for height 


print(f"Hey there, my name is {name}! I’m {age} year old and {height} feet tall. Nice to meet you!")

print("\n") # Adding a newline for better readability between tasks

# --- Task 2: Operators: Playing with Numbers ---
print("--- Task 2: Operators ---")

# Picking two numbers for our mathematical adventure!
num1 = 27 # My favorite number, don't ask why, it just is!
num2 = 5  # A nice, round number to play with.

# Addition
# Adding num1 and num2 together. The sum is the result!
sum_result = num1 + num2
print(f"The sum of {num1} and {num2} is: {sum_result} (Math is fun, right?)")

# Subtraction
# Taking num2 away from num1. Don't worry, no numbers were harmed in this operation.
sub_result = num1 - num2
print(f"When we subtract {num2} from {num1}, we get: {sub_result} (It's like magic, but with numbers!)")

# Multiplication
# Multiplying num1 by num2. This gets big fast!
mult_result = num1 * num2
print(f"Multiplying {num1} by {num2} gives us: {mult_result} (Cha-ching!)")

# Division
# Dividing num1 by num2. Watch out for those decimals!
div_result = num1 / num2
print(f"Dividing {num1} by {num2} results in: {div_result} (Look at that precise float!)")

print("\n") # Adding a newline for better readability between tasks

# --- Task 3: Conditional Statements: The Number Checker ---
print("--- Task 3: Conditional Statements ---")

# Ask the user to enter a number.
# The input() function gets user input as a string, so we need to convert it to a float.
try: # Using a try-except block to handle potential errors if the user doesn't enter a valid number
    user_number_str = input("Please enter a number, any number: ")
    user_number = float(user_number_str) # Convert the input string to a floating-point number

    # Now, let's use if, elif, and else to check the number!
    if user_number > 0:
        print(f"This number ({user_number}) is positive. Awesome!")
    elif user_number < 0:
        print(f"This number ({user_number}) is negative. Better luck next time!")
    else: # If it's not greater than 0 and not less than 0, it must be 0!
        print(f"Zero it is ({user_number}). A perfect balance!")

except ValueError:
    print("Oops! That wasn't a valid number. Please try again with a number.")

print("\n") # Adding a newline at the end

print("Assignment completed! You're well on your way to becoming a Python wizard! ✨")