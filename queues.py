from utils import get_random_list

class MyQueue:
    class QueueNode:
        def __init__(self, data):
            self.data = data
            self._next = None

    def __init__(self):
        self.first = None
        self.last = None

    def add(self, data):
        node = self.QueueNode(data)
        if self.is_empty():
            self.first = node
        else:
            self.last._next = node
        self.last = node

    def remove(self):
        if self.is_empty():
            return None
        else:
            node = self.first
            self.first = self.first._next
            if self.first is None:
                self.last = None
            return node

    def peek(self):
        if not self.is_empty():
            return self.first.data
        else:
            return None

    def is_empty(self):
        return self.first is None and self.last is None

    def print_queue(self, token=' < '):
        curr = self.first
        while curr is not None:
            if curr._next is not None:
                print(curr.data, end=token)
            else:
                print(curr.data)
            curr = curr._next

def main():
    a = get_random_list()
    print(a)    
    
    q = MyQueue()
    for x in a:
        q.add(x)
    q.print_queue()

if __name__ == '__main__':
    main()
