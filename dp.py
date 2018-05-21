"""
Longest increasing subsequence
Given N elements, write a program that prints the length of the longest increasing
subsequence whose adjacent element difference is one.

Input : a[] = {3, 10, 3, 11, 4, 5, 6, 7, 8, 12}
Output : 6
Explanation: 3, 4, 5, 6, 7, 8 is the longest increasing subsequence 
whose adjacent element differs by one.
"""
def longest_increasing_subsequence(a):
    """
    Solution:
    memo[i] stores the length of the longest subsequence which ends with a[i].
    For every i, if a[i] - 1 is present in the array before the ith element,
    then a[i] will add to the increasing subsequence which has a[i] - 1.
    """
    index_of = {}
    memo = [0 for x in a]
    for i, el in enumerate(a):
        index_of[el] = i
        try:
            memo[i] = memo[index_of[el - 1]] + 1
        except KeyError:
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
                psa[i][j] = a[i][j] + psa[i-1][j] + psa[i][j-1] - psa[i-1][j-1]

    return psa

if __name__ == '__main__':
    a = [3, 10, 3, 11, 4, 5, 6, 7, 8, 12]
    print(longest_increasing_subsequence(a))

    a = [[10, 20, 30],
         [5, 10, 20],
         [2, 4, 6]]
    print(prefix_sum_of_matrix(a))
