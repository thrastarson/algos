def count_bits(x):
    """
    A program to count the number of bits
    in a non-negative integer.
    It tests one bit at a time, starting with
    the least significant bit.
    """
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
        print(x)
    return num_bits

if __name__ == '__main__':
    x = 12
    print(count_bits(x))
