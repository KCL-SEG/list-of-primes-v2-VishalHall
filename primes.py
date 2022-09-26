"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("number_of_primes must be positive")
    list = []
    count = 2
    while True:
        if len(list) == number_of_primes:
            break
        
        isPrime = True # Assume number is prime
        for i in range(2, count):
            if count % i == 0:
                isPrime = False
        
        if isPrime:
            list += [count]
        count += 1

    return list