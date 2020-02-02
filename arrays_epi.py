from utils import get_random_list

#The input is a list of integers. Reorder its entries
#so that the even entries appear first.
def even_odd(a):
    start = 0
    end = len(a) - 1
    while start < end:
        if a[start] % 2 == 0:
            start += 1
        else:
            a[start], a[end] = a[end], a[start]
            end -= 1


#Write a program that takes an array a and an index i into a,
#and rearrange the elements such that all elements less than a[i]
#(the pivot) appear first, followed by elements equal to the pivot,
#followed by elements greater than the pivot.
def dutch_flag_partition1(a, i):
    """
    O(n) time, O(n) space.
    """
    less = []
    equal = []
    greater = []
    for x in a:
        if x < a[i]:
            less.append(x)
        elif x == a[i]:
            equal.append(x)
        else:
            greater.append(x)

    return less + equal + greater

if __name__ == '__main__':
    a = get_random_list(size=8, max_int=6)
    i = 2
    print(a, a[i])
    a_part = dutch_flag_partition1(a, i)
    print(a_part)
