from stacks import Stack
from utils import swap, get_random_list

#The following problems are from the book Cracking the Coding Interview
#by Gayle Laakmann McDowell. I reserve no rights for them.

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

#Problem 3.2
#How would you design a stack which, in addition to push and pop,
#has a function min which returns the minimum element?
#Push, pop, and min should all operate in O(1) time.
class MinStack(Stack):
    def __init__(self):
        super().__init__()
        self.min_idx = None

    def push(self, data):
        if self.is_empty():
            self.min_idx = 0

        min_val = self.get_min_val()
        if data < min_val:
            self.min_idx = len(self._list)

        super().push(data)

    def pop():
        min_val = self.get_min_val()
        data = super().pop()
        if data == min_val:
            self._find_new_min() 
        return data

    def get_min_value(self):
        return self._list[min_idx]

    def _find_new_min(self):
        min_val = min(self._list)
        self.min_idx = self._list.index(min_val)

#Problem 3.3
#Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
#Therefore, in real life, we would likely start a new stack when the previous stack
#exceeds some threshold. Implement a data structure SetOfStacks that mimics this.
#SetOfStacks should be composed of several stacks and should create a new stack
#once the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop()
#should behave identically to a single stack (that is, pop() should return the same
#values as it would if there were just a single stack).
#Follow up:
#Implement a function popAt(int index) which performs a pop operation on a specific
#sub-stack.
class SetOfStacks:
    def __init__(self, limit=10):
        self.stacks = [Stack()]
        self.limit = limit
        self.current_stack = 0

    def push(self, data):
        current_size = self._get_current_size()
        if current_size >= self.limit:
            self._add_new_stack()
        
        current_stack = self._get_current_stack()
        current_stack.push(data)

    def pop(self):
        current_size = self._get_current_size()
        if current_size == 0:
            self._remove_stack()    
        current_stack = self._get_current_stack()
        if not current_stack.is_empty():
            return current_stack.pop()
        else:
            return None

    def pop_at(self, index):
        if index > self.current_stack:
            return None
        else:
            stack = self.stacks[index]
            return stack.pop()

    def _remove_stack(self):
        _ = self.stacks.pop()
        if self.current_stack > 0:
            self.current_stack -= 1

    def _add_new_stack(self):
        self.stacks.append(Stack())
        self.current_stack += 1

    def _get_current_stack(self):
        return self.stacks[self.current_stack]

    def _get_current_size(self):
        current_stack = self._get_current_stack()
        return current_stack.size()

    def print_stacks(self):
        for i, stack in enumerate(self.stacks[::-1]):
            print('SubStack %s:' % str(i + 1))
            stack.print_stack()

def test_set_of_stacks():
    a = get_random_list(13)
    print(a)

    stacks = SetOfStacks(limit=5)
    for x in a:
        stacks.push(x)
    stacks.print_stacks()

    print('Popping 5 values...')
    for i in range(5):
        _ = stacks.pop()
    stacks.print_stacks() 
    







