from utils import get_random_list

class Node:
    def __init__(self, data):
        self.data = data
        self._next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        node._next = self.head
        self.head = node

    def delete(self, data):
        if self.is_empty():
            return
        
        if self.head.data == data:
            self.head = self.head._next
            return

        current_node = self.head
        while current_node._next is not None:
            if current_node._next.data == data:
                current_node._next = current_node._next._next
                break
            else:
                current_node = current_node._next

    def is_empty(self):
        return self.head is None

    def size(self):
        current_node = self.head
        count = 0
        while current_node is not None:
            count += 1
            current_node = current_node._size
        return count

    def search(self, data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                return True
            else:
                current_node = current_node._next
        return False

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            if current_node._next is not None:
                print(current_node.data, end=' -> ')
            else:
                print(current_node.data)
            current_node = current_node._next

def main():
    a = get_random_list()
    print(a)
    
    _list = LinkedList()
    for x in a:
        _list.insert(x)
    _list.print_list()

    
    mid_element = a[len(a) // 2]
    first_element = a[-1]
    last_element = a[0]
    test_elements = (mid_element, first_element, last_element)
    for element in test_elements:
        print('Deleting %s...' % element)
        _list.delete(element)
        _list.print_list()
   
if __name__ == '__main__':
    main()


    
