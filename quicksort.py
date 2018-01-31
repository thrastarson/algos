from utils import test_sorting, swap

def quicksort(a):
    a = list(a)
    qsort(a, 0, len(a) - 1)
    return a

def qsort(a, start, end):
    if start < end:
        split = partition(a, start, end)
        qsort(a, start, split - 1)
        qsort(a, split + 1, end)

def partition(a, start, end):
    pivot = start
    left = start + 1
    right = end
   
    done = False
    while not done:
        while left <= right and a[left] <= a[pivot]:
            left += 1

        while left <= right and a[right] >= a[pivot]:
            right -= 1

        if right < left:
            done = True
        else:
            swap(a, left, right)
    
    swap(a, pivot, right)
    return right

def main():
    test_sorting(quicksort)

if __name__ == '__main__':
    main()
