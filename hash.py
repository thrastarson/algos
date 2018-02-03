from utils import get_random_list

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
        print('[ ', end='')
        for index in range(self.size):
            val = self.table[index]
            if val is None:
                val = 'x'

            if index == self.size - 1:
                print(val, end='')
            else:
                print(val, end=' | ')
        print(' ]')

def main():
    a = get_random_list()
    print(a)

    htable = SimpleHashTable()
    for x in a:
        index = htable._hash(x)
        print('Inserting %3s at index %2s.' % (x, index))
        htable.insert(x)

    htable.print_table()

if __name__ == '__main__':
    main()
