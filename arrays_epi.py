from utils import get_random_list

#The input is a list of integers. Reorder its entries
#so that the even entries appear first.
def even_odd(a):
    start = 0
    end = len(a) - 1
    while start < end:
        if a[start] % 2 == 0:
            start += 1
        else:
            a[start], a[end] = a[end], a[start]
            end -= 1


#Write a program that takes an array a and an index i into a,
#and rearrange the elements such that all elements less than a[i]
#(the pivot) appear first, followed by elements equal to the pivot,
#followed by elements greater than the pivot.
def dutch_flag_partition1(A, i):
    """
    O(n) time, O(n) space.
    """
    less = []
    equal = []
    greater = []
    for x in A:
        if x < A[i]:
            less.append(x)
        elif x == A[i]:
            equal.append(x)
        else:
            greater.append(x)

    return less + equal + greater

def dutch_flag_partition2(A, pivot_index):
    """
    O(n) time, O(1) space.
    """
    pivot = A[pivot_index]
    smaller = 0
    for i in range(len(A)):
        #Move all elements smaller than pivot to the front.
        if A[i] < pivot:
            A[smaller], A[i] = A[i], A[smaller]
            smaller += 1
    
    larger = len(A) - 1
    for j in reversed(range(len(A))):
        #Move all elements larger than pivot to the back.
        if A[j] > pivot:
            A[larger], A[j] = A[j], A[larger]
            larger -= 1
    
    #Now all elements equal to pivot are trivially in the middle.

def dutch_flag_partition3(A, pivot_index):
    """
    O(n) time, O(1) space.
    """
    smaller, equal, bigger = 0, 0, len(A)-1
    pivot = A[pivot_index]

    while equal < bigger:
        #A[equal] is the incoming unclassified element
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller += 1 
            equal += 1
        elif A[equal] == pivot:
            equal += 1
        else:
            A[bigger], A[equal] = A[equal], A[bigger]
            bigger -= 1


if __name__ == '__main__':
    A = get_random_list(size=8, max_int=6)
    i = 2
    print(A, A[i])
    A_part = dutch_flag_partition1(A, i)
    print(A_part)

    A = get_random_list(size=8, max_int=6)
    print(A, A[i])
    dutch_flag_partition2(A, i)
    print(A)

    A = get_random_list(size=8, max_int=6)
    print(A, A[i])
    dutch_flag_partition3(A, i)
    print(A)
