# There is a simple yet powerful technique that allows for the fast calculation of sums of
# elements in given slice (contiguous segments of array). Its main idea uses prefix sums which 
# are defined as the consecutive totals of the first 0, 1, 2, . . . , n elements of an array.

def prefix_sums(A):
    #Counts prefix sums in O(n).
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k-1] + A[k-1]
    return P

# Using prefix (or suffix) sums allows us to calculate the total of any slice of the array very quickly. 
# For example, assume that you are asked about the totals of m slices [x..y] such that 0  <= x <= y <= n,
# where the total is the sum a_x + a_{x+1} + . . . + a_{y−1} + a_y.
# If we calculate the prefix sums then we can answer each question directly in constant time.

def count_total(P, x, y):
    #Total of one slice O(1).
    return P[y+1] - P[x]

# Using this approach, the total time complexity is O(n + m), dominated by creating the prefix sums once.

# You are given a non-empty, zero-indexed array A of n (1 <= n <= 100000) integers a_i, 0 <= a_i <= 1000.
# This array represents number of mushrooms growing on the consecutive spots along a road.
# You are also given integers k and m, k >= 0, m < n.
# A mushroom picker is at spot number k on the road and should perform m moves. In
# one move she moves to an adjacent spot. She collects all the mushrooms growing on spots
# she visits. The goal is to calculate the maximum number of mushrooms that the mushroom
# picker can collect in m moves.
def pick_mushrooms(A, k, m):
    n = len(A)
    result = 0
    pref = prefix_sums(A)

    for p in range(min(m, k) + 1):
        left_pos = k - p
        right_pos = min(n - 1, max(k, k + m - 2 * p))
        result = max(result, count_total(pref, left_pos, right_pos))
    
    for p in range(min(m + 1, n - k)):
        left_pos = max(0, min(k, k - (m - 2 * p)))
        right_pos = k + p
        result = max(result, count_total(pref, left_pos, right_pos))
    
    return result
        