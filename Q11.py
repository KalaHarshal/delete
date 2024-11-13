#a
def calculate_sum(a):
    a_str = str(a)

    term1 = int(a_str)
    term2 = int(a_str * 2)
    term3 = int(a_str * 3)
    term4 = int(a_str * 4)
    
    result = term1 + term2 + term3 + term4
    
    return result

a = int(input("Enter a single-digit number: "))
print("The result of a + aa + aaa + aaaa is:", calculate_sum(a))

#b
def check_divisibility(binary_numbers):
    binary_list = binary_numbers.split(',')
    
    divisible_by_5 = [binary for binary in binary_list if int(binary, 2) % 5 == 0]
    
    return ','.join(divisible_by_5)

binary_numbers = input("Enter 4-digit binary numbers separated by commas: ")
result = check_divisibility(binary_numbers)
print("Binary numbers divisible by 5 are:", result)
