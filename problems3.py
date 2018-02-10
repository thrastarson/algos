from utils import swap

#Problem 3.1
#Describe how you could use a single array to implement three stacks.
class ThreeStack:
    """
    This solution is implemented using a list,
    [a1, a2, ..., an, b1, b2, ..., bn, c1, c2, ..., cn],
    where [a1, an] are the elements on the first stack,
    [b1, bn] are the elements on the second stack,
    and [c1, cn] are the elements on the third stack.
    """
    def __init__(self):
        self._list = []
        first_size = 0
        second_size = 0
        third_size = 0

    def insert_first(self, data):
        self._list.append(data)
        first_size += 1

    def insert_second(self, data):
        n = len(self._list)
        self._list.append(data)
        
        i = first_size
        while i > 0:
            swap(self._list, n-1, n)
            n -= 1
            i -= 1
        
        second_size += 1

    def insert_third(self, data):
        n = len(self._list)
        self._list.append(data)

        i = first_size
        while i > 0:
            swap(self._list, n-1, n)
            n -= 1
            i -= 1

        j = second_size
        while j > 0:
            swap(self._list, n-1, n)
            n -= 1
            j -= 1

        third_size += 1

    def pop_first(self):
        if first_size > 0:
            return self._list.pop()
        else:
            return None

    def pop_second(self):
        last = len(self._list) - 1
        second_top = last - first_size
        second_size -= 1
        return self._pop(second_top)

    def pop_third(self):
        last = len(self._list) - 1
        third_top = last - first_size - second_size
        third_size -= 1
        return self._pop(third_top)

    def _pop(self, index):
        return self._list.pop(index)

    def first_is_empty(self):
        return self.first_size == 0

    def second_is_empty(self):
        return self.second_size == 0

    def third_is_empty(self):
        return self.third_size == 0
