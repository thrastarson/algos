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

if __name__ == '__main__':
    a = [3, 10, 3, 11, 4, 5, 6, 7, 8, 12]
    print(longest_increasing_subsequence(a))
