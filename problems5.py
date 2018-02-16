from bits import to_binary_string
from collections import Counter

#Problem 5.1
#You are given two 32-bit numbers, N and M, and two bit positions, i and j.
#Write a method to insert M into N such that M starts at bit j and ends at bit i.
#You can assume that the bits j through i have enough space to fit all of M.
#That is, if M=10011, you can assume that there are at least 5 bits between j and i.
#You would not, for example, have j=3 and i=2, because M could not fully fit between
#bit 3 and bit 2.
#Example:
#Input: N = 10000000000, M=10011, i=2, j=6
#Output: N = 10001001100
def insertion(n, m, i, j):
    if m > n or i >= j:
        return None

    k = i
    while k <= j:
        #Clear bits in N that will be overwritten by M.
        mask = ~(1 << i)
        n = n & mask
        k += 1

    mask = m << i
    return n | mask

#Problem 5.2
#Given a real number between 0 and 1 (e.g. 0.72) that is passed in as a double,
#print the binary representation. If the number cannot be represented accurately
#in binary with at most 32 characters, print "ERROR"
def binary_to_string(num):
    """
    This solution is a straight python implementation of Gayle's solution
    in CtCI.
    """
    if num >= 1 or num <= 0:
        return 'ERROR'

    binary = []
    binary.append('.')
    while num > 0:
        #Setting a limit on length: 32 characters
        if len(binary) >= 32:
            return 'ERROR'

        r = num * 2
        if r >= 1:
            binary.append(1)
            num = r - 1
        else:
            binary.append(0)
            num = r
    return ''.join(binary)

#Problem 5.3
#You have an integer and you can flip exactly one bit from a 0 to a 1.
#Write code to find the length of the longest sequence of 1s you could create.
#Example:
#Input: 1775 (or: 11011101111)
#Output: 8
def flip_bit_to_win(num):
    num = to_binary_string(num)
    max_length = 1
    prev_len = 0
    curr_len = 0
    max_length = 1
    last_bit = 0
    for i in num:
        if i == '1':
            curr_len += 1
        else:
            if prev_len + curr_len + 1 > max_length:
                max_length = prev_len + curr_len + 1

            if last_bit == 0:
                prev_len = 0
                curr_len = 0
            else:
                prev_len = curr_len
                curr_len = 0

            last_bit = 0

    return max_length

#Problem 5.4
#Given a positive integer, print the next smallest and the next largest number
#that have the same number of 1 bits in their binary representation.
def next_number(num):
    num_ones = count_ones(num)
    
    found_largest = False
    larger = num + 1
    while not found_largest:
        ones = count_ones(larger)
        if ones == num_ones:
            found_largest = True
        else:
            larger += 1

    found_smallest = False
    smaller = num - 1
    while not found_smallest:
        ones = count_ones(smaller)
        if ones == num_ones:
            found_smallest = True
        else:
            smaller -= 1

    return smaller, larger

def count_ones(num):
    bin_string = to_binary_string(num)
    c = Counter(bin_string)
    return c['1']



















