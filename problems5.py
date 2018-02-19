from bits import to_binary_string
from collections import Counter

#The following problems are from the book Cracking the Coding Interview
#by Gayle Laakmann McDowell. I reserve no rights for them.

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

#Problem 5.5
#Explain what the following code does: ((n & (n-1)) == 0)
#Solution: It checks if n is a power of 2 (or if n is zero).

#Problem 5.6
#Write a function to determine the number of bits you would need
#to flip to convert integer A to integer B.
#Example:
#Input: 29 (or: 11101), 15 (or: 01111)
#Output: 2
def conversion(n, m):
    n = to_binary_string(n)
    m = to_binary_string(m)

    #reverse both binary strings.
    n = n[::-1]
    m = m[::-1]

    i = 0
    j = 0
    flips = 0
    while i < len(n) and j < len(m):
        if n[i] != m[j]:
            flips += 1
        i += 1
        j += 1


    while i < len(n):
        flips += 1
        i += 1

    while j < len(m):
        flips += 1
        j += 1

    return flips

def conversion2(n, m):
    """
    Take the XOR of n and m and count the occurrences
    of the bit 1.
    """
    return to_binary_strin(n ^ m).count('1')

#Problem 5.7
#Write a program to swap odd and even bits in an integer with as few
#instructions as possible (e.g., bit 0 and bit 1 are swapped, bit 2
#and bit 3 are swapped, and so on.
def pairwise_swap(n):
    n_bin = to_binary_string(n)
    
    odd_mask = ['01' for _ in range(len(n_bin)//2 + 1)]
    odd_mask = ''.join(odd_mask)
    odd_mask = int(odd_mask, 2)

    even_mask = ['10' for _ in range(len(n_bin)//2 + 1)]
    even_mask = ''.join(even_mask)
    even_mask = int(even_mask, 2)

    only_odd = n & odd_mask
    only_even = n & even_mask
    
    odd_shifted = only_odd << 1
    even_shifted = only_even >> 1
    swapped = odd_shifted ^ even_shifted
    
    return swapped

#Problem 5.8
#A monochrome screen is stored as a single array of bytes, allowing eight
#consecutive pixels to be stored in one byte. The screen has width w,
#where w is divisible by 8 (that is, no byte will be split across rows).
#The height of the screen, of course, can be derived from the length
#of the array and the width. Implement a function that draws a horizontal
#line from (x1, y) to (x2, y).
#The method signature should look something like:
#drawLine(byte[] screen, int width, int x1, int x2, int y)
def draw_line(screen, width, x1, x2, y):
    rows = screen // width
    for i in range(y * 8 + x1: y * 8 + x2 + 1):
        screen[i] = 1
    return screen
