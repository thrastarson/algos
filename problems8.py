from stacks import Stack

#The following problems are from the book Cracking the Coding Interview
#by Gayle Laakmann McDowell. I reserve no rights for them.

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

#Problem 8.3
#A magic index in an array A[0...n-1] is defined to be an index such that
#A[i] = i. Given a sorted array of distinct integers, write a method to find
#a magic index, if one exists, in array A.
def magic_index(a):
    """
    The obvious solution.
    """
    return any(i == x for i, x in enumerate(a))

def magic_index1(a, i=None, j=None):
    """
    A recursive solution.
    """
    if i is None and j is None:
        i = 0
        j = len(a) - 1

    if len(a[i:j+1]) == 1:
        return a[i] == i
    else:
        m = (j - i) // 2
        return magic_index1(a, i, m) or magic_index1(a, m + 1, j)

def magic_index2(a, i=None, j=None):
    """
    A binary search inspired recursive solution.
    """
    if i is None and j is None:
        i = 0
        j = len(a) - 1


    m = (j - i) // 2
    if a[m] == m:
        return True

    if m > a[m]:
        magic_index2(a, m + 1, j)
    else:
        magic_index2(a, i, m + 1)

#Problem 8.4
#Write a method to return all subsets of a set.
def power_set(a, memo=None):
    if memo is None:
        memo = set()
        memo.add('empty')
        a = list(a)

    if len(a) == 0:
        return memo

    val = a.pop()
    memo.add(val)
    
    for subset in memo:
        if subset == 'empty':
            continue

        subset_copy = set(list(subset))
        subset_copy.add(val)
        memo.add(subset_copy)

    power_set(a, memo)

#Problem 8.5
#wrtie a recursive function to multiply two positive integers without using
#the * operator. You can use addition, subtraction, and bit shifting, but you
#should minimize the number of those operations.
def recursive_multiply(a, b):
    if a == 0 or b == 0:
        return a
    else:
        return a + recursive_multiply(a, b-1)

def recursive_multiply2(a, b):
    bigger = a if a < b else b
    smaller = a if a < b else b

    if smaller == 0:
        return 0
    elif smaller == 1:
        return bigger
    
    s = smaller // 2
    half_prod = recursive_multiply2(s, bigger)

    if smaller % 2 == 0:
        return half_prod + half_prod
    else:
        return half_prod + half_prod + bigger

#Problem 8.6
#In the classic problem of the Towers of Hanoi, you have 3 towers and N disks
#of different sizes which can slide onto any tower. The puzzle starts with
#disks sorted in ascending order of size from top to bottom (i.e. each disk
#sits on top of an even larger one). You have the following constraints:
#(1) Only one disk can be moved at a time.
#(2) A disk is slid off the top of one tower onto another tower.
#(3) A disk cannot be placed on top of a smaller disk.
#Write a program to move the disks from the first tower to the last using stacks.
def towers_of_hanoi(a, b, c):

















