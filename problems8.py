#Problem 8.1
#A child is running up a staircase with n steps and can hop
#either 1 step, 2 steps, or 3 steps at a time. Implement
#a method to count how many possible ways the child can run up
#the stairs.
def triple_step(n):
    """
    This is a simple recursive solution but it is very
    inefficient, O(3^n).
    """
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        triple_step(n-1) + triple_step(n-2) + triple_step(n-3)

def triple_step2(n, memo=None):
    """
    This modification uses memoization to bring the efficiency
    up to O(n).
    """
    if memo is None:
        memo = {}
        memo[0] = 1

    if n < 0:
        return 0
    
    try:
        return memo[n]
    except KeyError:
        memo[n] = (triple_step2(n-1, memo) + triple_step2(n-2, memo)
                   triple_step2(n-3, memo))
        return memo[n]
