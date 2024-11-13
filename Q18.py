def is_palindrome(s):
    return s == s[::-1]

def find_palindromes(string_list):
    
    palindromes = list(filter(is_palindrome, string_list))
    non_palindromes = [s for s in string_list if s not in palindromes]

    print("Palindrome Strings:", ",".join(palindromes))
    print("Total Palindromes:", len(palindromes))
    print("Total Non-palindromes:", len(non_palindromes))

string_list = ["madam", "hello", "racecar", "world", "level", "python"]
find_palindromes(string_list)
