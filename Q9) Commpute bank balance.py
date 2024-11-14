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

# Function to process the transaction log and calculate the balance
def calculate_balance(transaction_log):
    balance = 0
    i = 0
    while i < len(transaction_log):
        if transaction_log[i] == 'D':  # Deposit
            i += 2
            amount_str = ""
            while i < len(transaction_log) and transaction_log[i].isdigit():
                amount_str += transaction_log[i]
                i += 1
            balance += int(amount_str)
        elif transaction_log[i] == 'W':  # Withdrawal
            i += 2
            amount_str = ""
            while i < len(transaction_log) and transaction_log[i].isdigit():
                amount_str += transaction_log[i]
                i += 1
            balance -= int(amount_str)
        else:
            i += 1
    return balance

# Input transaction log from the user
transaction_log = input("Enter transaction log (e.g., 'D 300 D 300 W 200 D 100'): ")
net_balance = calculate_balance(transaction_log)
print("Net Balance:", net_balance)

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
