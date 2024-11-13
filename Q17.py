#a
def analyze_string(input_string):
    vowels = "aeiouAEIOU"
    vowel_indices = []
    consonant_indices = []
    capital_count = 0
    lowercase_count = 0

    for index, char in enumerate(input_string):
        if char.isalpha():
            if char in vowels:
                vowel_indices.append(index)
            else:
                consonant_indices.append(index)

            if char.isupper():
                capital_count += 1
            elif char.islower():
                lowercase_count += 1

    return vowel_indices, consonant_indices, [capital_count, lowercase_count]

input_string = input("Enter a string")
vowel_indices, consonant_indices, case_counts = analyze_string(input_string)

print("Indices of Vowels:", vowel_indices)
print("Indices of Consonants:", consonant_indices)
print("Capital and Lowercase counts:", case_counts)
