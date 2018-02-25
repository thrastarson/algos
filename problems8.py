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

#Problem 8.2
#Imagine a robot sitting on the upper left corner of grid with r rows
#and c columns. The robot can only move in two directions, right and down,
#but certain cells are "off limits" such that the robot cannot step
#on them. Design an algorithm to find a path for the robot from the top
#left to the bottom right.
def find_path(grid, row=None, col=None, path=None):
    if grid is None or len(grid) == 0:
        return None

    if path is None:
        path = []

    if row is None:
        row = len(grid)

    if col is None:
        col = len(grid[0])

    at_end_point = col == 0 and row == 0
    if (at_end_point 
        or find_path(grid, row-1, col, path) 
        or find_path(grid, row, col-1, path)):
        path.append((col, row))
        return True

    return False
