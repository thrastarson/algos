from utils import get_random_list
from lists import LinkedList

class SimpleHashTable:
    """
    This implementation of a simple hash table is data lossy.
    It is not collision resistent, and will overwrite previous
    data on collision.
    However, it is useful to subclass and overwrite with a better
    hash function and collision resistance.
    """
    def __init__(self, size=20):
        self.table = [None for i in range(size)]
        self.size = size

    def _hash(self, val):
        return (val % self.size) - 1

    def insert(self, val):
        index = self._hash(val)
        self.table[index] = val

    def print_table(self):
        for index in range(self.size):
            val = self.table[index]
            if val is None:
                val = 'x'

            print('%3s: %s' % (index, val))

class HashTable(SimpleHashTable):
    def insert(self, val):
        index = self._hash(val)
        if self.table[index] is None:
            _list = LinkedList()
            self.table[index] = _list
        self.table[index].insert(val)

    def print_table(self):
        for index in range(self.size):
            _list = self.table[index]

            if _list is None:
                print('%3s: %s' % (index, 'x')) 
            else:
                print('%3s: ' % index, end='')
                _list.print_list()

def main():
    a = get_random_list()
    print(a)

    hash_classes = (SimpleHashTable, HashTable,)
    for hash_class in hash_classes:
        htable = hash_class()
        for x in a:
            index = htable._hash(x)
            print('Inserting %3s at index %2s.' % (x, index))
            htable.insert(x)

        htable.print_table()

if __name__ == '__main__':
    main()
