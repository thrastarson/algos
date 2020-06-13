import random

def quick_select(A, left, right, k):
    '''
    Returns the k-th smallest element of a list between left and right
    incluseive (left <= k <= right).
    To return the k-th largest element, set k = (right - left + 1) - k
    '''

    if left == right:
        #If the list contains only one element return that element.
        return A[left]

    #Select a pivot_index in [left..right] by any means.
    pivot_index = random.randint(left, right)
    result_index = partition(A, left, right, pivot_index)
    
    #The pivot is in its final sorted position at index result_index.
    if k == result_index:
        return A[k]
    elif k < result_index:
        return quick_select(A, left, result_index - 1, k)
    else:
        return quick_select(A, result_index + 1, right, k)

def partition(A, left, right, pivot_index):
    '''
    Partition A between left and right by the value of the
    pivot_index (left <= pivot_index <= right) such that
    all values < A[pivot_index] are in A[left..result_index-1]
    and all values >= A[pivot_index] are in A[result_index..right].
    '''
    #Store the pivot value and move it to the end of the list.
    pivot = A[pivot_index]
    swap(A, pivot_index, right)

    result_index = left
    for i in range(left, right):
        if A[i] < pivot:
            swap(A, result_index, i)
            result_index += 1
    swap(A, right, result_index)
    return result_index

def swap(A, i, j):
    A[i], A[j] = A[j], A[i]