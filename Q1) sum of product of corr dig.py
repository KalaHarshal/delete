'''1) a.Write program, which reads two numbers (assume that both have same number of digits).The program
outputs the sum of product of corresponding digits.
Input 327 and 539 output 3x5+2x3+7x9=84.
b. Write program, which finds the sum of numbers formed by consecutive
digits. Input 2415 output 24+41+15=80.
 Q-1)'''
 
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Initialize sum
sum_product = 0

# Loop through each digit by index
for i in range(len(num1)):
    sum_product += int(num1[i]) * int(num2[i])

print("Sum of products of corresponding digits:", sum_product)

# Q-2) 
num = input("Enter a number: ")

# Initialize sum
sum_consecutive = 0

# Loop through each digit by index
for i in range(len(num) - 1):
    # Form a two-digit number from consecutive digits
    consecutive_num = int(num[i] + num[i + 1])
    sum_consecutive += consecutive_num

print("Sum of numbers formed by consecutive digits:", sum_consecutive)

