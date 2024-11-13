import threading

# Function to calculate the sum of all prime numbers up to n
def sum_of_primes(n):
    prime_sum = 0
    for num in range(2, n + 1):
        # Check if num is prime
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_sum += num
    print("Sum of all prime numbers up to", n, ":", prime_sum)
    print("Thread Name:", threading.current_thread().name)

# Function to calculate the sum of squares of all numbers up to m
def sum_of_squares(m):
    square_sum = 0
    for num in range(1, m + 1):
        square_sum += num ** 2
    print("Sum of squares of all numbers up to", m, ":", square_sum)
    print("Thread Name:", threading.current_thread().name)

# Values for n and m
n = 50  # You can change this value as needed
m = 5   # You can change this value as needed

# Creating threads with specific names
first_thread = threading.Thread(target=sum_of_primes, args=(n,), name="YourFirstName")
second_thread = threading.Thread(target=sum_of_squares, args=(m,), name="YourSurname")

# Starting threads
first_thread.start()
second_thread.start()

# Waiting for both threads to finish
first_thread.join()
second_thread.join()
