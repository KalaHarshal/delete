#a
def is_all_even(number):
    return all(int(digit) % 2 == 0 for digit in str(number))

even_digit_numbers = [str(number) for number in range(1000, 3001) if is_all_even(number)]

print(",".join(even_digit_numbers))


#b
def count_digits_and_letters(input_string):
    letters = sum(char.isalpha() for char in input_string)
    digits = sum(char.isdigit() for char in input_string)
    return letters, digits

input_string = input("Enter a string: ")

letters_count, digits_count = count_digits_and_letters(input_string)

print("Number of letters:", letters_count)
print("Number of digits:", digits_count)
