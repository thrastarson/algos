import math

def is_prime(n):
    """
    This primality test implements a trial division.
    To brute force test for primality it is sufficient
    to try divisors in the range [2, ..., floor(sqrt(n))].
    Furthermore, notwithstanding 2, it is also sufficient
    to only try odd integers in that interval.
    """
    end = math.floor(math.sqrt(n))
    
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0:
        return False

    for i in range(3, end + 1):
        if i % 2 == 1 and n % i == 0:
            return False

    return True

def sieve_of_eratosthenes(n):
    """
    Implements an ancient algorithm for finding all prime numbers
    up to any given limit, n. It does so by iteratively marking
    the multiples of each prime starting with the number 2.
    At the end only (and all) prime numbers <= n are left.
    """
    flags = [True for _ in range(n + 1)]
    flags[0] = False
    flags[1] = False

    prime = 2
    while prime <= math.floor(math.sqrt(n)):
        cross_off(flags, prime)
        prime = get_next_prime(flags, prime)
    
    all_primes = [i for i, _ in enumerate(a) if a[i] is True]
    return all_primes

def cross_off(flags, prime):
    """
    Cross off remaining multiples of prime. We can start with (prime*prime)
    because if we have a k * prime, where k < prime, this value would have
    already been crossed off in a prior iteration.
    """
    i = prime * prime
    while i < len(flags):
        flags[i] = False
        i += prime

def get_next_prime(flags, prime):
    next_prime = prime + 1
    while next_prime < len(flags) and flags[next_prime] is False:
        next_prime += 1
    return next_prime
