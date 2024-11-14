'''
4) a. Write a program that accepts a sentence and calculate the number of capital letters, lowercase letters and
digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
CAPS 0
LOWERCASE 10
DIGITS 3
b. Write a program with function name calculate_sum() that computes the value of a+aa+aaa+aaaa with a given
digit as the value of a. Suppose the following input is supplied to the program:
9
Then, the function must return 11106 as output. '''

#a: 

# Read the sentence from the user
sentence = input("Enter a sentence: ")

# Initialize counters
caps_count = 0
lowercase_count = 0
digit_count = 0

# Loop through each character in the sentence
for char in sentence:
    if char.isupper():  # Check if the character is uppercase
        caps_count += 1
    elif char.islower():  # Check if the character is lowercase
        lowercase_count += 1
    elif char.isdigit():  # Check if the character is a digit
        digit_count += 1

# Print the results
print("CAPS", caps_count)
print("LOWERCASE", lowercase_count)
print("DIGITS", digit_count)

#b: 
def calculate_sum(a):
    # Convert a to string for easy concatenation
    a_str = str(a)

    # Create the four terms: a, aa, aaa, aaaa
    term1 = int(a_str)
    term2 = int(a_str * 2)  # "aa"
    term3 = int(a_str * 3)  # "aaa"
    term4 = int(a_str * 4)  # "aaaa"

    # Calculate the total sum
    result = term1 + term2 + term3 + term4
    return result

# Read the single-digit number from the user
a = int(input("Enter a single-digit number: "))

# Call the function and print the result
print("Result:", calculate_sum(a))
