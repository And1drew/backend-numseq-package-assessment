def primes(n):
    """Returns a list of all prime numbers less than n"""
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes


def is_prime(n):
    """Returns a boolean indicating whether `m` is a prime number"""
    if n in [2, 3]:
        return True
    elif n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True
