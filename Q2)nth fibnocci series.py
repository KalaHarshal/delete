'''2)a.Implement a Python program to display nth Fibonacci number of Fibonacci series, Read value of n from user.
b. Implement a Python program to check whether a given integer is Krishnamurthy number or not.
Krishnamurthy number can be defined as a number when the sum of the factorial of all digits is equal to the
original number. This Krishnamurthy number is also called the Strong number, Special number and Peterson
number. E.g. n=145 1!+4!+5!=1+24+120=145'''
# a: 
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# Read the value of n from the user
n = int(input("Enter the position (n) of the Fibonacci number: "))
result = fibonacci(n)
print(f"The {n}th Fibonacci number is: {result}")

#b: 
import math

# Read the integer from the user
num = int(input("Enter a number: "))

# Initialize sum of factorials
sum_factorials = 0

# Calculate the sum of factorials of each digit
for digit in str(num):
    sum_factorials += math.factorial(int(digit))

# Check if the sum of factorials is equal to the original number
if sum_factorials == num:
    print(f"{num} is a Krishnamurthy number.")
else:
    print(f"{num} is not a Krishnamurthy number.")
