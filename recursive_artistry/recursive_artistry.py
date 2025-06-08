import turtle

def factorial(n):
    """Recursive function to calculate factorial of n."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    """Recursive function to calculate nth Fibonacci number."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def draw_fractal_tree(t, branch_length, level):
    """Recursive function to draw a fractal tree using turtle."""
    if level == 0 or branch_length < 5:
        return
    t.forward(branch_length)
    t.left(30)
    draw_fractal_tree(t, branch_length * 0.7, level - 1)
    t.right(60)
    draw_fractal_tree(t, branch_length * 0.7, level - 1)
    t.left(30)
    t.backward(branch_length)

def get_positive_integer(prompt):
    """Helper function to get a positive integer from user input."""
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def main():
    print("Welcome to the Recursive Artistry Program!")
    while True:
        print("\nChoose an option:")
        print("1. Calculate Factorial")
        print("2. Find Fibonacci")
        print("3. Draw a Recursive Fractal")
        print("4. Exit")
        choice = input("> ")

        if choice == '1':
            n = get_positive_integer("Enter a number to find its factorial: ")
            print(f"The factorial of {n} is {factorial(n)}.")
        elif choice == '2':
            n = get_positive_integer("Enter the position of the Fibonacci number: ")
            print(f"The {n}th Fibonacci number is {fibonacci(n)}.")
        elif choice == '3':
            print("Drawing a simple fractal tree! Close the window to continue.")
            t = turtle.Turtle()
            screen = turtle.Screen()
            t.left(90)
            t.up()
            t.backward(100)
            t.down()
            t.color("green")
            draw_fractal_tree(t, 100, 5)
            screen.exitonclick()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
