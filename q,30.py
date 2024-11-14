# Sample input list
from functools import reduce 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using higher-order functions

# 1. Check for even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# 2. Square all numbers
squared_numbers = list(map(lambda x: x ** 2, numbers))

# 3. Find the sum of all numbers
sum_of_numbers = reduce(lambda x,y:x+y, numbers)

# Output results
print("Even Numbers:", even_numbers)
print("Squared Numbers:", squared_numbers)
print("Sum of Numbers:", sum_of_numbers)



# Function to find the longest string in a list
def find_longest_string(strings):
    # Use the max function with key=len to find the longest string
    return max(strings, key=len)

# Sample input
input1 = ['cat', 'car', 'fear', 'center']
input2 = ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']

# Output the longest string for both inputs
print("Longest string in input1:", find_longest_string(input1))
print("Longest string in input2:", find_longest_string(input2))
