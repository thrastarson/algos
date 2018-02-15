from utils import get_random_list

class Node:
    def __init__(self, data):
        self.data = data
        self._next = None

class DoubleNode(Node):
    def __init(self, data):
        super().__init__(data)
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        node._next = self.head
        self.head = node

    def insert_last(data):
        node = Node(data)
        curr = self.head
        while curr._next is not None:
            curr = curr._next
        curr._next = node

    def build_from_collection(self, a):
        a = list(a)
        while len(a) > 0:
            self.insert(a.pop())

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

    def get_first(self):
        first_node = self.head
        self.head = self.head._next
        return first_node

    def get_last(self):
        if self.head is None:
            return None

        prev = None
        curr = self.head
        
        while curr._next is not None:
            curr = curr._next
            prev = prev._next

        if prev is not None:
            prev._next = None
        
        return curr

    def is_empty(self):
        return self.head is None

    def clone(self):
        cloned = LinkedList()
        curr_node = self.head
        while curr_node is not None:
            node = Node(curr_node.data)
            cloned.insert(node)
        cloned.reverse()
        return cloned

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

    def reverse(self):
        """
        This implementation of reverse manipulates the pointers
        in our list in one traversal.
        """
        prev_node = None
        current_node = self.head
        while current_node is not None:
            temp = current_node._next
            current_node._next = prev_node
            prev_node = current_node
            current_node = temp
        
        self.head = prev_node

    def reverse2(self):
        """
        This implementation of reverse creates a new list
        and builds up a reverse version of our list by
        repeatedly popping and deleting the head
        before inserting to the new list.
        """
        reverse_list = LinkedList()
        while not self.is_empty():
            data = self.head.data
            self.delete(data)
            reverse_list.insert(data)
        self.head = reverse_list.head

    def print_list(self, token=' -> '):
        current_node = self.head
        while current_node is not None:
            if current_node._next is not None:
                print(current_node.data, end=token)
            else:
                print(current_node.data)
            current_node = current_node._next

class DoubleLinkedList(LinkedList):
    def insert(self, data):
        node = DoubleNode(data)
        
        if not self.is_empty():
            self.head.prev = node
        
        node._next = self.head
        self.head = node

    def delete(self, data):
        if self.is_empty():
            return

        if self.head.data == data:
            if self.head._next is not None:
                self.head._next.prev = None
            self.head = self.head._next
            return

        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                
                if current_node.prev is not None:
                    current_node.prev._next = current_node._next
                
                if current_node._next is not None:
                    current_node._next.prev = current_node.prev

                break
            else:
                current_node = current_node._next
    
    def get_first(self):
        first_node = self.head
        self.head = self.head._next
        self.head.prev = None
        return first_node

    def reverse(self):
        current_node = self.head
        while current_node is not None:
            self.head = current_node
            next_node = current_node._next
            current_node._next = current_node.prev
            current_node.prev = next_node
            current_node = next_node

    def print_list(self):
        super().print_list(token=' <-> ')

def main():
    a = get_random_list()
    print(a)
   
    list_classes = (LinkedList, DoubleLinkedList)
    for list_class in list_classes:
        _list = list_class()
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
       
        print('Reversing list...')
        _list.reverse()
        _list.print_list()

        print('Re-reversing the list...')
        _list.reverse2()
        _list.print_list()

if __name__ == '__main__':
    main()
