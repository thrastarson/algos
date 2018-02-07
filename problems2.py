from lists import LinkedList

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
