'''5) a. Implement a Python program to create 2 threads(using _thread module) in which one thread will display
multiples of a number given by the user and the other thread will display prime numbers for a given range.
b. Implement a Python program to create 2 threads(threading module) in which one thread will display multiples of
5 and second will display multiples of 7 synchronously.'''

#a:
import _thread
import time

# Function to display multiples of a given number
def display_multiples():
    num = int(input("Enter a number for multiples: "))
    print(f"Multiples of {num}:")
    for i in range(1, 11):
        print(num * i)
        time.sleep(0.5)

# Function to display prime numbers up to a given range
def display_primes():
    limit = int(input("Enter the limit for prime numbers: "))
    print(f"Prime numbers up to {limit}:")
    for num in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)
        time.sleep(0.5)

# Start threads
_thread.start_new_thread(display_multiples, ())
_thread.start_new_thread(display_primes, ())

# Keep the main program running
time.sleep(10)

#b:
import threading
import time

# Function to display multiples of 5 and 7 alternately
def display_multiples(factor, label):
    for i in range(1, 6):
        print(f"{label} multiple: {factor * i}")
        time.sleep(0.5)

# Create threads
thread1 = threading.Thread(target=display_multiples, args=(5, "Multiple of 5"))
thread2 = threading.Thread(target=display_multiples, args=(7, "Multiple of 7"))

# Start and join threads
thread1.start()
thread2.start()

thread1.join()
thread2.join()
