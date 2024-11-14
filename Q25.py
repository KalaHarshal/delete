#QA)

#Accepting input from the user
input_string = input("Enter a string: ")

# Initializing counters for letters and digits
letters_count = 0
digits_count = 0

# Iterating over each character in the string
for char in input_string:
    if char.isalpha():       # Checks if the character is a letter
        letters_count += 1
    elif char.isdigit():      # Checks if the character is a digit
        digits_count += 1

# Printing the results
print("Letters", letters_count)
print("Digits", digits_count








binary_list = input("Enter comma seperated binary numbers: ").split(',')
divisible_by_5= (binary for binary in binary_list if int(binary, 2)%5==0)
print(','.join(divisible_by_5))
      
