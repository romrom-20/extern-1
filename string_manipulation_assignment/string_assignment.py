# String Manipulation Assignment
# Author: saman

def string_slicing_indexing():
    # Task 1: String slicing and indexing
    s = "Python is amazing!"
    first_word = s[:6]
    amazing_part = s[10:17]
    reversed_string = s[::-1]

    print("First word:", first_word)
    print("Amazing part:", amazing_part)
    print("Reversed string:", reversed_string)

def string_methods():
    # Task 2: String methods
    s = " hello, python world! "
    print("Original string:", repr(s))
    print("After strip():", repr(s.strip()))
    print("After capitalize():", s.strip().capitalize())
    print("After replace():", s.strip().replace("world", "universe"))
    print("After upper():", s.strip().upper())

def palindrome_check():
    # Task 3: Palindrome check
    word = input("Enter a word: ")
    if word == word[::-1]:
        print(f"Yes, '{word}' is a palindrome!")
    else:
        print(f"No, '{word}' is not a palindrome.")

def main():
    print("Welcome to the String Manipulation Assignment by saman!")
    string_slicing_indexing()
    print("\n")
    string_methods()
    print("\n")
    palindrome_check()

if __name__ == "__main__":
    main()
