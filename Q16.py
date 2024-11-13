def mountain(lst):
    n = len(lst)
    if n < 6:  
        return False

    i = 1
    while i < n and lst[i] > lst[i - 1]:
        i += 1

    if i < 3 or i == n:
        return False

    while i < n and lst[i] < lst[i - 1]:
        i += 1

    return i == n
