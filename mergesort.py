from utils import test_sorting

def mergesort(a):
    if len(a) > 1:
        m = len(a) // 2
        left = a[:m]
        right = a[m:]
        
        mergesort(left)
        mergesort(right)
        a = merge(a, left, right)

def merge(a, left, right):
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1
    
    while i < len(left):
        a[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        a[k] = right[j]
        j += 1
        k += 1

    return a

def main():
    test_sorting(mergesort, returns_sorted=False)

if __name__ == '__main__':
    main()
