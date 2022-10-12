"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("number_of_primes must be positive")
    primeNumbers = []
    currNum = 2
    while len(primeNumbers) < number_of_primes:
        isPrime = True # Assume number is prime
        for i in range(2, currNum):
            if currNum % i == 0:
                isPrime = False
        
        if isPrime:
            primeNumbers += [currNum]
        currNum += 1

    return primeNumbers