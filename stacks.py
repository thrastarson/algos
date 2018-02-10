from lists import LinkedList
from utils import get_random_list

class Stack:
    def __init__(self):
        self._list = []

    def push(self, data):
        self._list.append(data)

    def pop(self):
        if not self.is_empty():
            return self._list.pop()

    def is_empty(self):
        return len(self._list) == 0

    def size(self):
        return len(self._list)

    def peek(self):
        if not self.is_empty():
            return self._list[-1]
        else:
            return None

    def print_stack(self):
        print(self._list)

class ArrayStack(Stack):
    def __init__(self, size=20):
        self._list = []
        self.count = 0
        self.size = size

    def push(self, data):
        if self.count >= self.size:
            #Pretend self._list is a fixed size array.
            #Double the size of the array to increase
            #the size of the stack.
            self.size = self.size * 2
            bigger_list = [x for x in self._list]
            self._list = bigger_list
        
        self._list.append(data)
        self.count += 1

    def pop(self):
        if not self.is_empty():
            self.count -= 1
            return self._list[self.count]

    def is_empty(self):
        return self.count == 0

class ListStack(Stack):
    def __init__(self):
        self._list = LinkedList()

    def push(self, data):
        self._list.insert(data)

    def pop(self):
        if not self.is_empty():
            head = self._list.get_first()             
            return head.data

    def is_empty(self):
        return self._list.is_empty()

    def print_stack(self):
        self._list.print_list()

def main():
    a = get_random_list()
    print(a)

    stack_classes = (Stack, ArrayStack, ListStack)
    for stack_class in stack_classes:
        stack = stack_class()
        for x in a:
            stack.push(x)
        stack.print_stack()

        while not stack.is_empty():
            print('Popping %s..' % stack.pop())
        stack.print_stack()

if __name__ == '__main__':
    main()
