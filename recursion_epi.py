
# The Eucledian algorithm for calculating the Greatest Common Divisor of two numbers
# is a classic recursion algorithm.
# The central idea is that if y > x, the GCD of x and y is the GCD of x and y - x.
# By extension, this implies that the GCD of x and y is the GCD of x and y mod x.
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

