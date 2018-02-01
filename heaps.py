import random
from utils import swap

class MinHeap():
    def __init__(self):
        self.heap = []
        self.size = 0

    def heapify(self, a):
        self.size = len(a)
        self.heap = a
        i = len(a) - 1
        while i >= 0:
            self._bubble_down(i)
            i -= 1

    def peek(self):
        if self.size > 0:
            return self.heap[0]
        else:
            return None

    def extract_min(self, verbose=False):
        x = self.peek()
        if x:
            self.delete_min()

        if verbose:
            print('deleting %s => %s' % (x, self.heap))
        
        return x

    def delete_min(self):
        self.heap[0] = self.heap[self.size - 1]
        self.heap.pop()
        self.size -= 1
        self._bubble_down(0)

    def insert(self, x, verbose=False):
        self.heap.append(x)
        self._bubble_up(self.size)
        self.size += 1

        if verbose:
            print('inserting %3s => %s' % (x, self.heap))

    def print_heap(self):
        print(self.heap)

    def _bubble_up(self, i):
        parent_idx = self._get_parent_index(i)
        while parent_idx is not None:
            if self.heap[i] < self.heap[parent_idx]:
                swap(self.heap, i, parent_idx)
            i = parent_idx
            parent_idx = self._get_parent_index(parent_idx)

    def _bubble_down(self, i):
        while self._has_child(i):
            min_child_idx = self._get_min_child_index(i)
            if self.heap[i] > self.heap[min_child_idx]:
                swap(self.heap, i, min_child_idx)
            i = min_child_idx

    def _has_child(self, i):
        return self._get_left_child_index(i) < self.size

    def _get_min_child_index(self, i):
        left_idx = self._get_left_child_index(i)
        right_idx = self._get_right_child_index(i)
        if right_idx >= self.size:
            return left_idx
        else:
            if self.heap[left_idx] < self.heap[right_idx]:
                return left_idx
            else:
                return right_idx

    def _get_left_child_index(self, i):
        return 2*i + 1

    def _get_right_child_index(self, i):
        return 2*i + 2

    def _get_parent_index(self, i):
        if i != 0:
            return (i - 1) // 2
        else:
            return None

def main():
    a = [random.randint(0, 100) for i in range(10)]
    h = MinHeap()
     
    #test insertion to heap
    for x in a:
        h.insert(x, verbose=True)
    h.print_heap()
    
    #test extraction from heap
    while h.peek():
        _ = h.extract_min(verbose=True)
    h.print_heap()

    h.heapify(a)
    h.print_heap()
if __name__ == '__main__':
    main()





