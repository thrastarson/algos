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
