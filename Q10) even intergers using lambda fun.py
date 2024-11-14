'''10) a.Write a Python program to get a list of even integers using Lambda function and/or higher order functions
from given list of integers.
Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Output: [2, 4, 6, 8, 10]
b) Write a Python program to get a list of odd integers using Lambda function and/or higher order functions from
given list of integers.
Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Output: [1, 3, 5, 7, 9]
c) Write a Python program to get a list of integers that are divisible by 3 using Lambda function and/or higher order
functions from given list of integers.
Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Output: [ 3, 6, 9]
d) Write a Python program to square and cube every number in a given list of integers using Lambda function
and/or higher order functions.
Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Square every number of the input list:[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Cube every number of the input list:[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]'''

#a:
# Input list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get even numbers using lambda function and filter
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Even numbers:", even_numbers)

#b: 
# Get odd numbers using lambda function and filter
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

print("Odd numbers:", odd_numbers)

#c:
# Get numbers divisible by 3 using lambda function and filter
divisible_by_3 = list(filter(lambda x: x % 3 == 0, numbers))

print("Numbers divisible by 3:", divisible_by_3)

#d:
# Square every number using lambda function and map
squares = list(map(lambda x: x ** 2, numbers))
print("Square of every number:", squares)

# Cube every number using lambda function and map
cubes = list(map(lambda x: x ** 3, numbers))
print("Cube of every number:", cubes)
