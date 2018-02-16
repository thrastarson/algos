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

