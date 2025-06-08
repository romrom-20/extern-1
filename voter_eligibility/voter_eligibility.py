# Voter Eligibility Checker
# Author: saman

def check_voter_eligibility():
    # Ask the user's age and convert input to integer
    age = int(input("How old are you? "))

    # Check if the user is eligible to vote
    if age >= 18:
        print("Congratulations! You are eligible to vote. Go make a difference! 🎉")
    else:
        years_to_wait = 18 - age
        print(f"Oops! You’re not eligible yet. But hey, only {years_to_wait} more year{'s' if years_to_wait > 1 else ''} to go! 😊")

if __name__ == "__main__":
    check_voter_eligibility()
