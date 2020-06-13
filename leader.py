# Given a sequence a_0, a_1, ..., a_{n-1}, a leader of this sequence
# is the element whose value occurs more than n/2 times.
# There can be at most one leader in a sequence of n elements.

def slow_leader(A):
    # Count the occurences of each element. O(n^2).
    n = len(A)
    leader = -1
    for x in A:
        count = 0
        for y in A:
            if x == y:
                count += 1
        
        if count > n // 2:
            leader = x
    
    return leader

def fast_leader(A):
    # If A is sorted, notice that the leader value must be at index n/2,
    # because the leader value occurs more than n/2 times by definition.
    n = len(A)
    A.sort()
    leader = -1

    m = n // 2
    count = 1
    i = m + 1
    while A[i] == A[m]:
        count += 1
        i += 1
    
    while A[j] == A[m]:
        count += 1
        j -= 1

    if count > n // 2:
        leader = A[m]
    
    return leader

def slow_max_slice(A):
    # O(n^3) to find the maximum sub-sum of a slice in an array.
    n = len(A)
    if n == 0:
        return 0

    result = 0
    for p in range(n):
        for q in range(p, n):
            slice_sum = 0
            for i in range(p, q + 1):
                slice_sum += A[i]
            result = max(result, slice_sum)
    
    return result

def quadradic_max_slice(A):
    # O(n^2) to find the maximum sub-sum of a slice in an array.
    # Pre-computing the prefix sums allows us to calculate the sum
    # of any given slice in constant time.
    n = len(A)
    if n == 0:
        return 0

    pref = prefix_sum(A)
    result = 0
    for p in range(n):
        for q in range(p, n):
            slice_sum = A[q] + pref[q] - pref[p]
            result = max(result, slice_sum)
    
    return result

def prefix_sum(A):
    n = len(A)
    if n == 0:
        return []

    pref = [0] * n
    pref[0] = 0
    for i in range(1, n):
        pref[i] = pref[i-1] + A[i-1]

    return pref

def quadradic_max_slice2(A):
    # O(n^2) to find the maximum sub-sum of a slice in an array.
    # This solution uses no prefix sums and therefore no extra space.
    n = len(A)
    if n == 0:
        return 0

    result = 0
    for p in range(n):
        slice_sum = 0
        for q in range(p, n):
            slice_sum += A[q]
            result = max(result, slice_sum)
    
    return result

def fast_max_slice(A):
    # O(n) to find the maximum sub-sum of a slice in an array.
    # We use a solution for shorter sequences to find the solution
    # for longer sequences. 
    n = len(A)
    if n == 0:
        return 0

    max_ending = 0 #maximum sum of any slice ending in i
    max_slice = 0 
    for x in A:
        if x > 0:
            max_ending = max(0, max_ending + x)
            max_slice = max(max_slice, max_ending)
    return max_slice

def sub_array_sum(A, s):
    # Given an unsorted array of integers, find a subarray which adds to a given number. 
    # If there are more than one subarrays with the sum as the given number, print any of them.
    n = len(A)
    if n == 0:
        return None

    sub_sum_map = {}
    curr_sum = 0
    for i, val in enumerate(A):
        curr_sum += val

        if curr_sum == s:
            return (0, i)
        
        try:
            start_index = sub_sum_map[s - curr_sum]
        except KeyError:
            # Sub-array with s not found. Add curr_sum and current index to map.
            sub_sum_map[curr_sum] = i
        else:
            # Sub-array with s found. sum(A[start_index:i+1]) == s.
            return (start_index, i)

    return None
    