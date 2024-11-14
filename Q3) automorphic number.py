''' 3)a. Implement a Python program to check whether a given integer isan Automorphic Number A number is called an
automorphic number if and only if the square of the given number ends with the same number itself. For example,
25, 76 are automorphic numbers because their square is 625 and 5776, respectively and the last two digits of the
square represent the number itself. Some other automorphic numbers are 5, 6, 890625, etc.
b) Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-
separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without, hello, bag, world
Then, the output should be:
bag, hello, without, world'''
# a:
# Read the number from the user
num = int(input("Enter a number: "))

# Calculate the square of the number
square = num ** 2

# Check if the square ends with the number itself
if str(square).endswith(str(num)):
    print(f"{num} is an Automorphic number.")
else:
    print(f"{num} is not an Automorphic number.")




#b: 
# Read a comma-separated sequence of words from the user
words = input("Enter a comma-separated sequence of words: ")

# Split the input string into a list of words
word_list = words.split(',')

# Sort the list of words alphabetically
word_list.sort()

# Join the sorted list back into a comma-separated string
sorted_words = ', '.join(word_list)

# Print the sorted words
print("Sorted words:", sorted_words)
