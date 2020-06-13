from lists import LinkedList

#Merge Two Sorted Lists
#Consider two singly linked lists in which each node holds a number.
#Assume the lists are sorted, i.e., numbers in the lists appear
#in ascending order within each list. Write a program that takes
#these two lists, assumed to be sorted, and returns its merge.
#The only field your program can change in a Node is its next pointer.
def merge_sorted_lists(l1, l2):
    if l1 is None:
        return l2

    if l2 is None:
        return l1

    if l1.data <= l2.data:
        m = l1
        l1 = l1.next
    else:
        m = l2
        l2 = l2.next

    merged = m
    while l1 is not None and l2 is not None:
        if l1.data <= l2.data:
            m.next = l1
            l1 = l1.next
        else:
            m.next = l2
            l2 = l2.next
        m = m.next

    if l1 is not None:
        m.next = l1

    if l2 is not None:
        m.next = l2

    return merged

#Reverse A Single Sublist
#Write a program that takes a singly linked list l an two integers
#s and f as arguments, and reverses the order of the node from the
#s-th node to the f-th node, inclusive. The numbering begins at 1,
#the head node is the first node. Do not allocate additional nodes.
def reverse_sublist(l, start, finish):
    if start == finish:
        return l
    
    curr = l
    for _ in range(1, start):
        curr = curr.next

    prev = curr
    sublist = curr.next
    for _ in range(finish - start):
        temp = sublist.next
        sublist.next = prev
        prev = prev.next
        sublist = temp

