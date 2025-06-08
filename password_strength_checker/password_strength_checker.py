# Password Strength Checker
# Author: saman

import re

def password_strength_checker():
    password = input("Enter a password: ")

    score = 0
    missing_criteria = []

    # Check length
    if len(password) >= 8:
        score += 2
    else:
        missing_criteria.append("at least 8 characters")

    # Check uppercase
    if re.search(r'[A-Z]', password):
        score += 2
    else:
        missing_criteria.append("one uppercase letter")

    # Check lowercase
    if re.search(r'[a-z]', password):
        score += 2
    else:
        missing_criteria.append("one lowercase letter")

    # Check digit
    if re.search(r'\d', password):
        score += 2
    else:
        missing_criteria.append("one digit")

    # Check special character
    if re.search(r'[!@#$%^&*()\-_=+\[\]{}|;:\'",.<>?/`~]', password):
        score += 2
    else:
        missing_criteria.append("one special character")

    if score == 10:
        print("Your password is strong! 💪")
    else:
        print("Your password needs " + ", ".join(missing_criteria) + ".")

    print(f"Password strength score: {score}/10")

if __name__ == "__main__":
    password_strength_checker()
