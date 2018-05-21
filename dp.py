"""
Longest increasing subsequence by one
Given N elements, write a program that prints the length of the longest increasing
subsequence whose adjacent element difference is one.

Input : a[] = {3, 10, 3, 11, 4, 5, 6, 7, 8, 12}
Output : 6
Explanation: 3, 4, 5, 6, 7, 8 is the longest increasing subsequence 
whose adjacent element differs by one.
"""
def longest_increasing_subsequence_by_one(a):
    """
    Solution:
    memo[i] stores the length of the longest subsequence which ends with a[i].
    For every i, if a[i] - 1 is present in the array before the ith element,
    then a[i] will add to the increasing subsequence which has a[i] - 1.
    """
    index_of = {}
    memo = [0 for _ in a]
    for i, el in enumerate(a):
        index_of[el] = i
        try:
            memo[i] = memo[index_of[el - 1]] + 1
        except KeyError:
            memo[i] = 1

    return max(memo)

"""
The Longest Increasing Subsequence (LIS) problem is to find the length 
of the longest subsequence of a given sequence such that all elements 
of the subsequence are sorted in increasing order. 
For example, the length of LIS for {10, 22, 9, 33, 21, 50, 41, 60, 80} 
is 6 and LIS is {10, 22, 33, 50, 60, 80}.
"""
def longest_increasing_subsequence(a):
    """
    Solution:
    Let arr[0..n-1] be the input array and L(i) be the length of the LIS 
    ending at index i such that arr[i] is the last element of the LIS.
    Then, L(i) can be recursively written as:
        L(i) = 1 + max( L(j) ) where 0 < j < i and arr[j] < arr[i]; or
        L(i) = 1, if no such j exists.
    To find the LIS for a given array, we need to return max(L(i)) where 0 < i < n.
    """
    memo = [0 for _ in a]
    for i in range(len(a)):
        prefix_path = [path for j, path in enumerate(memo[:i]) if a[j] < a[i]]
        if len(prefix_path) > 0:
            memo[i] = max(prefix_path) + 1
        else:
            memo[i] = 1

    return max(memo)

"""
Prefix sum of Matrix.
Given a matrix (or 2D array) a[][] of integers, find the prefix sum matrix for it. 
Let the prefix sum matrix be psa[][]. The value of psa[i][j] contains the sum 
of all values which are above it or on left of it.

a = [[10, 20, 30],  psa = [[10, 30,  60],
     [ 5, 10, 20],         [15, 45,  95],
     [ 2,  4,  6]]         [17, 51, 107]]
"""
def prefix_sum_of_matrix(a):
    psa = [[0 for col in a] for row in a]
    
    for i, row in enumerate(a):
        for j, el in enumerate(row):
            if i == 0 and j == 0:
                psa[i][j] = a[i][j]
            elif i == 0:
                psa[i][j] = a[i][j] + psa[i][j-1]
            elif j == 0:
                psa[i][j] = a[i][j] + psa[i-1][j]
            else:
                #The tricky part is to remember to subtract psa[i-1][j-1]
                #so as not to double count.
                psa[i][j] = a[i][j] + psa[i-1][j] + psa[i][j-1] - psa[i-1][j-1]

    return psa

"""
Longest Common Subsequence
Given two sequences a and b, find the length of the longest subsequence 
present in both of them. A subsequence is a sequence that appears 
in the same relative order, but not necessarily contiguous. 
For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc 
are subsequences of “abcdefg”. 
So a string of length n has 2^n different possible subsequences.
"""
def longest_common_subsequence(a, b):
    memo = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                memo[i+1][j+1] = memo[i][j] + 1
            else:
                memo[i+1][j+1] = max(memo[i][j+1], memo[i+1][j])
    n = len(a)
    m = len(b)
    return memo[n][m]

"""
Minimum Edit Distance
Given two strings a and b and the operations insert, remove, replace,
find the minimum number of edits required to convert a into b.
All of the operations are of equal cost.
"""
def minimum_edit_distance(a, b):
    memo = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
    for i in range(len(a) + 1):
        for j in range(len(b) + 1):
            if i == 0:
                #If a is empty, the only option is to insert
                #all characters of b.
                memo[i][j] = j
            elif j == 0:
                #if b is empty, the only option is to delete
                #all characters from a.
                memo[i][j] = i
            elif a[i-1] == b[j-1]:
                memo[i][j] = memo[i-1][j-1]
            else:
                memo[i][j] = 1 + min(memo[i][j-1],     #Insert
                                     memo[i-1][j],     #Delete
                                     memo[i-1][j-1])     #Replace
    
    n = len(a)
    m = len(b)
    return memo[n][m]

"""
Subset Sum Problem
Given a set of non-negative integers a, and a value s, 
determine if there is a subset of a with sum equal to s.
"""
def has_subset_sum_rec(a, s):
    """
    Recursive solution. Running time is O(2^n).
    """
    if s == 0:
        return True

    if len(a) == 0 and s > 0:
        return False

    if a[-1] > s:
        #If last element is greater than s,
        #we can ignore it.
        return has_subset_sum_rect(a[:-1], s)
    else:
        #Check both remaining possibilities:
        #   a) exclude the last element, search for subset in prefix
        #   b) include the last element, search for remainder of s
        #      in prefix
        return (has_subset_sum_rec(a[:-1], s) 
                or has_subset_sum_rec(a[:-1], s - a[-1]))

if __name__ == '__main__':
    a = [3, 10, 3, 11, 4, 5, 6, 7, 8, 12]
    print('Longest increasing subsequence by one:')
    print(a)
    print(longest_increasing_subsequence_by_one(a))

    a = [[10, 20, 30],
         [5, 10, 20],
         [2, 4, 6]]
    print('Prefix sum of a matrix:')
    print(a)
    print(prefix_sum_of_matrix(a))

    a = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    print('Longest increasing subsequence:')
    print(a)
    print(longest_increasing_subsequence(a))

    a = 'ABCDGH'
    b = 'AEDFHR'
    print('Longest common subsequence:')
    print(a, b)
    print(longest_common_subsequence(a, b))

    a = 'AGGTAB'
    b = 'GXTXAYB'
    print(a, b)
    print(longest_common_subsequence(a, b))

    a = 'sunday'
    b = 'saturday'
    print('Minimum edit distance:')
    print(a, b)
    print(minimum_edit_distance(a, b))

    a = 'intention'
    b = 'execution'
    print(a, b)
    print(minimum_edit_distance(a, b))

    a = [3, 34, 4, 12, 5, 2]
    s = 9
    print('Subset sum problem:')
    print('Recursive:')
    print(a, s)
    print(has_subset_sum_rec(a, s))
