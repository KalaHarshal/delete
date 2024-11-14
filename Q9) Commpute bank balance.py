'''9) a. Write a program that computes the net amount of a bank account based a transaction log from console input.
The transaction log format is shown as following:
D 100
W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300W 200D 100
Then, the output should be: 500
b.Write a Python program to check the validity of passwords input by users.
Validation :
• At least 1 letter between [a-z] and 1 letter between [A-Z].
• At least 1 number between [0-9].
• At least 1 character from [$#@].
• Minimum length 6 characters.
• Maximum length 16 characters'''
#a:

# Initialize the balance to 0
balance = 0

# Read the transaction log inputs from the user
while True:
    transaction = input("Enter transaction (D for deposit, W for withdrawal or 'exit' to stop): ")
    if transaction.lower() == 'exit':
        break
    action, amount = transaction.split()
    amount = int(amount)
    
    if action == 'D':
        balance += amount  # Deposit adds to the balance
    elif action == 'W':
        balance -= amount  # Withdrawal subtracts from the balance

# Output the final balance
print(balance)



#b: password validation
import re

# Function to validate the password
def is_valid_password(password):
    if (6 <= len(password) <= 16 and
        re.search(r'[a-z]', password) and           # At least one lowercase letter
        re.search(r'[A-Z]', password) and           # At least one uppercase letter
        re.search(r'[0-9]', password) and           # At least one digit
        re.search(r'[$#@]', password)):             # At least one special character from [$#@]
        return True
    return False

# Input password from the user
password = input("Enter a password to validate: ")

# Check and display if the password is valid or not
if is_valid_password(password):
    print("Password is valid.")
else:
    print("Password is invalid.")
