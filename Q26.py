#QA)
# Get user input
letter = input("Input a letter of the alphabet: ").lower()

# Check if the input is a single alphabet letter
if letter.isalpha() and len(letter) == 1:
    # Define vowels
    vowels = "aeiou"
    
    # Check if the letter is a vowel
    if letter in vowels:
        print(letter + " is a vowel.")
    else:
        print(letter + " is a consonant.")
else:
    print("Invalid input. Please enter a single alphabet letter.")




#QB)
import re

def validate_password(password):
    # Check for minimum and maximum length
    if len(password) < 6 or len(password) > 16:
        return "Invalid password: Must be between 6 and 16 characters long."

    # Define regex patterns for validation checks
    if not re.search("[a-z]", password):
        return "Invalid password: Must contain at least one lowercase letter."
    if not re.search("[A-Z]", password):
        return "Invalid password: Must contain at least one uppercase letter."
    if not re.search("[0-9]", password):
        return "Invalid password: Must contain at least one digit."
    if not re.search("[$#@]", password):
        return "Invalid password: Must contain at least one special character ($, #, or @)."
    
    return "Password is valid."

# Input password from the user
password = input("Enter your password: ")
# Validate the password
result = validate_password(password)
print(result)
