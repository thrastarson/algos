from stacks import Stack
from queues import MyQueue
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

#Problems 3.4
#Implement a MyQueue class which implements a queue using two stacks.
class MyStackQueue:
    def __init__(self, data):
        self.in_stack = Stack()
        self.out_stack = Stack()
        self.first = None
        self.last = None

    def add(self, data):
        self.in_stack.push(data)

    def remove(self):
        if not self.out_stack.is_empty():
            return self.out_stack.pop()
        
        self._shift_between_stacks()

        if not self.out_stack.is_empty():
            return self.out_stack.pop()
        else:
            return None

    def peek(self):
        if not self.out_stack.is_empty():
            return self.out_stack.peek()
        
        self._shift_between_stacks()

        if not self.out_stack.is_empty():
            return self.out_stack.peek()
        else:
            return None

    def is_empty(self):
        return self.out_stack.is_empty() and self.in_stack.is_empty()
        
    def _shift_between_stacks(self):
        #Move all elements from in_stack to out_stack,
        #then pop from out_stack.
        while not self.in_stack.is_empty():
            self.out_stack.push(self.in_stack.pop())

#Problems 3.5
#Write a program to sort a stack such as the smallest items are on top.
#You can use an additional temporary stack but you may not copy th
#elements into any other data structure (such as an array).
#The stack supports the following operations (push, pop, peek, and is_empty).
def sort_stack(stack):
    if stack.is_empty():
        return stack

    temp = Stack()
    while not stack.is_empty():
        if temp.is_empty():
            temp.push(stack.pop())
        else:
            val = stack.pop()
            while not temp.is_empty() and temp.peek() > val:
                stack.push(temp.pop())
            temp.push(val)

    while not temp.is_empty():
        stack.push(temp.pop())

def test_sort_stack():
    a = get_random_list(5)
    stack = Stack()
    for x in a:
        stack.push(x)

    stack.print_stack()
    sort_stack(stack)
    stack.print_stack()

#Problem 3.6
#An animal shelter, which holds only dogs and cats, operates on a strictly
#'first in, first out' basis. People must adopt either the 'oldest'
#(based on arrival time) of all animals in the shelter, or they can select
#whether they would prefer a dog or a cat (and will receive the oldest animal
#of that type). They cannot select which specific animal they would like.
#Create the data structures to maintain this system and implement operations
#such as enqueue, dequeueAny, dequeueDog, and dequeueCat. You may use
#the built-in LinkedList data structure.
class AnimalShelter:
    def __init__(self):
        self.dog_queue = MyQueue()
        self.cat_queue = MyQueue()
        self.order = 0

    def enqueue(self, animal):
        self.order += 1
        if animal == 'dog':
            self.dog_queue.add(order)
        elif animal == 'cat':
            self.cat_queue.add(order)

    def dequeueDog(self):
        return self.dog_queue.remove()

    def dequeueCat(self):
        return self.cat_queue.remove()

    def dequeueAny(self):
        if self.cat_queue.peek() < self.dog_queue.peek():
            return self.cat_queue.remove()
        else:
            return self.dog_queue.remove()

#Extra problem.
#Given a string of opening and closing brackets, test if the
#brackets are balanced or not.
def is_matched(expression):
    if expression is None:
        return True
    
    if len(expression) % 2 == 1:
        return False
    
    stack = []
    starting = '{[('
    closing = '}])'
    matching = {i: j for i, j in zip(closing, starting)}
    for x in expression:
        if x in starting:
            stack.append(x)
        elif x in closing:
            if len(stack) == 0:
                return False
            popped = stack.pop()
            if matching[x] != popped:
                return False
    
    if len(stack) == 0:
        return True
    else:
        return False
