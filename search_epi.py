import bisect

#bisect provides binary search functions assuming input
#is a sorted list.
#bisect.bisect_left(a, x) returns the index of the first entry that
#is greater than or equal to the targeted value x.

def bin_search(A, k):
    '''
    Binary search, iterative.
    Returns the index of an element with value k or -1 if it doesn't exits.
    '''
    left = 0
    right = len(A) - 1
    while left <= right:
        m = left + (right - left) // 2
        if A[m] < k:
            left = m + 1
        elif A[m] == k:
            return m
        else:
            right = m - 1
    return -1


def search_first_of_k(A, k):
    '''
    Returns the index of the first occurrence of k
    in the sorted list A, or -1 if it doesn't exist.
    '''
    left = 0
    right = len(A) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if k > A[mid]:
            left = mid + 1
        elif k == A[mid]:
            result = mid
            right = mid - 1 #Nothing to the right of mid can be the solution
        else:
            right = mid - 1
    return result
    

def search_entry_equal_to_its_index(A):
    '''
    A is a sorted array containing distinct elements
    Returns an index i such that A[i] = i, -1 if no such index exists.
    '''
    left = 0
    right = len(A) - 1
    while left <= right:
        mid = (left + right) // 2
        diff = A[mid] - mid #A[mid] == mid only if diff == 0
        if diff == 0:
            return mid
        elif diff > 0:
            #Relies on elements being distinct.
            right = mid - 1
        else:
            left = mid + 1
    return -1


def search_smallest(A):
    '''
    A is a cyclically sorted array, such that it is possible to shift its entries
    so that it becomes sorted. All elements are distinct
    Returns the index of the smalles element in the array.
    '''
    left = 0
    right = len(A) - 1
    while left < right:
        mid = (left + right) // 2
        if A[mid] <= A[right]:
            #Minimum must be in [left..mid+1]
            right = mid
        else:
            left = mid + 1
    
    #loop ends when left == right
    return left


def square_root(k):
    '''
    Returns the largest integer i such that i * i <= k.
    '''
    left = 0
    right = k
    while left <= right:
        #Candidate interval [left, right] where everything before left
        #has square <= k, everything after right has square > k. 
        mid = (left + right) // 2
        mid_squared = mid * mid
        if mid_squared <= k:
            left = mid + 1
        else:
            right = mid - 1
    return left - 1

def matrix_search(A, x):
    '''
    A is a matrix with sorted rows and sorted columns.
    Returns True if x exists, else False.
    '''
    row = 0
    col = len(A[0]) - 1
    while row < len(A) and col >= 0:
        












if __name__ == "__main__":
    A = list(range(1, 11))
    assert bin_search(A, 7) == 6

    B = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 404]
    assert search_first_of_k(B, 108) == 3
    assert bisect.bisect_left(B, 108) == 3

    C = [-2, 0, 2, 3, 6, 7, 9]
    assert search_entry_equal_to_its_index(C) in (2, 3)

    D = [378, 478, 550, 631, 103, 203, 220, 234, 279, 368]
    assert search_smallest(D) == 4