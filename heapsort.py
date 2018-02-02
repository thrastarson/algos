from heaps import MinHeap
from utils import test_sorting

def heapsort(a):
    a = list(a)
    heap = MinHeap()
    heap.heapify(a)
    a_sorted = []
    while heap.peek():
        a_sorted.append(heap.extract_min())

    return a_sorted

def main():
    test_sorting(heapsort)

if __name__ == '__main__':
    main()
