from lists import LinkedList

#The following problems are from the book Cracking the Coding Interview
#by Gayle Laakmann McDowell. I reserve no rights for them.

#Problem 2.1
#Write code to remove duplicates from an unsorted linked list.
#Follow up: How would you solve this problem if a temporary buffer
#is not allowed?
def remove_dups(_list):
    """
    This solution uses a hash table to record the first time
    a data value is seen. If a previously seen value
    is encountered, its node is removed.
    """
    seen = {}
    curr = _list.head
    seen[curr.data] = 1
    while curr._next is not None:
        val = curr._next.data
        if seen.get(val):
            #The next node is a duplicate.
            curr._next = curr._next._next
        else:
            seen[val] = 1

        curr = curr._next

def remove_dups2(_list):
    """
    This solution uses no external memory to record previously
    seen values. For each node it scans the nodes behind it
    to see if a duplicate exists, and removes it if it does.
    """
    curr = _list.head
    while curr._next is not None:
        val = curr.data
        runner = curr
        while runner._next is not None:
            if runner._next.data == val:
                runner._next = runner._next._next
            runner = runner._next
        curr = curr._next

#Extra problem.
#You get a linked list a1 -> a2 -> a3 -> an -> ... -> b1 -> b2 -> b3 ... -> bn.
#The length of the list is unknown, but it can be assumed to be of even length.
#Re-arrange the list like so a1 -> b1 -> a2 -> b2 -> ... -> an -> bn.
def weave(li):
    front = li.head
    back = li.head._next
    while back._next is not None:
        front = front._next
        back = back._next._next

    #now front = an, back = bn
    
    a = li.head
    b = front._next
    while a is not None and b is not None:
        
        if b._next is None:
            #We are finished weaving, but must fix a._next pointer
            #or else it will cause an infinite loop.
            a._next = b
            break

        next_a = a._next
        next_b = b._next

        a._next = b
        b._next = next_a

        a = next_a
        b = next_b

def test_weave():
    a = ['a1', 'a2', 'a3', 'a4', 'b1', 'b2', 'b3', 'b4'] 
    print(a)
    
    li = LinkedList()
    while len(a) > 0:
        li.insert(a.pop())

    li.print_list()
    weave(li)
    li.print_list()
