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
    """
    This solution runs in O(n) time.
    """
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
    li.build_from_collection(a)
    li.print_list()
    weave(li)
    li.print_list()

#Problem 2.2
#Implement an algorithm to find the kth to last element in a singly linked list.
def kth_to_last(li, k):
    """
    This solution runs in O(n) time.
    """
    if li.is_empty():
        return False

    curr = li.head
    count = 1
    while curr is not None:
        if count == k:
            return curr
        curr = curr._next
        count += 1
    return False

#Problem 2.3
#Implement an algorithm to delete the node in the middle (i.e. any node but the
#first and last node, not necessarily the exact middle) of a singly linked list,
#given only access to that node.
#Example: Input the node c from the linked list a -> b -> c -> d -> e -> f.
#Result: nothing is returned, 
#but the new linked list looks like a -> b -> d -> e -> f.
def delete_middle_node(node):
    prev = None
    while node._next is not None:
        node.data = node._next.data
        prev = node
        node = node._next
    prev._next = None

def test_delete_middle_node():
    a = ['a', 'b', 'c', 'd', 'e', 'f']
    
    li = LinkedList()
    li.build_from_collection(a)
    li.print_list()
    middle_node = kth_to_last(li, 3)
    delete_middle_node(middle_node)
    li.print_list()

#Problem 2.4
#Write code to partition a linked list around a value x, such that all nodes
#less than x come before all nodes greater than or equal to x. If x is contained
#with in the list, the values of x only need to be after the elements less than x.
#The partition element x can appear anywhere in the 'right partition';
#it does not need to appear between the left and right partitions.
#Example:
#Input:   3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1  [partition = 5]
#Output:  3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
def partition(li, p):
    prev = None
    curr = li.head
    while curr._next is not None:
        if curr._next.data < p:
            #Move curr._next to the head of the list.
            temp = curr._next._next
            curr._next._next = li.head
            li.head = curr._next
            curr._next = temp
        prev = curr
        curr = curr._next

    if curr.data < p:
        prev._next = None
        curr._next = li.head
        li.head = curr

def test_partition():
    a = [3, 5, 8, 5, 10, 2, 1]

    li = LinkedList()
    li.build_from_collection(a) 
    li.print_list()
    partition(li, 5)
    li.print_list()

#Problem 2.5
#You have two numbers represented by a linked list, where each node contains
#a single digit. The digits are stored in reverse order, such that the 1's
#digit is at the head of the list. Write a function that adds the two numbers
#and returns the sum as a linked list.
#Example:
#Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295.
#Output: 2 -> 1 -> 9. That is 912.
def sum_lists(a, b):
    a_num = 0
    a_mult = 1
    a_curr = a.head
    while a_curr is not None:
        a_num += a_curr.data * a_mult
        a_curr = a_curr._next
        a_mult *= 10

    b_num = 0
    b_mult = 1
    b_curr = b.head
    while b_curr is not None:
        b_num += b_curr.data * b_mult
        b_curr = b_curr._next
        b_mult *= 10

    output_num = a_num + b_num
    print(output_num)
    output_mult = 1
    while output_num // (output_mult * 10) > 0:
        output_mult *= 10

    output = LinkedList()
    if output_num == 0:
        output.insert(0)
        return output

    while output_num != 0:
        digit = int(output_num // output_mult)
        output.insert(digit)
        output_num = output_num - (digit * output_mult)
        output_mult /= 10
    
    return output

def test_sum_lists(num_a, num_b):
    a = LinkedList()
    a_str = str(num_a)
    for digit in a_str:
        a.insert(int(digit))

    b = LinkedList()
    b_str = str(num_b)
    for digit in b_str:
        b.insert(int(digit))

    a.print_list()
    b.print_list()

    result = sum_lists(a, b)
    result.print_list()

#Follow up: Suppose the digits are stored in forward order.
#Repeat the above problem.
#Example:
#Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is 617 + 295.
#Output: 9 -> 1 -> 2. That is 912.
#Solution: We'd solve this problem much the same way as above,
#          only this change requires us to scan both input number
#          once through to count the number of elements in the list.
#          Then we set mult = 10^(count-1), before proceeding
#          like before. Creating the output list would simply
#          be done in reverse order.


#Problem 2.6
#Implement a function to check if a linked list is a palindrome.
def is_a_palindrome(li):
    """
    This solution relies on the fact that the linked list
    implementation inserts nodes at the head of the list.
    It first scans the list to count the number of elements.
    Then we pop off the first half of the list while inserting
    into a new list. This will reverse the elements in a stack-like
    manner. If the original list contains an odd number
    of elements we discard the middle element. Finally, we
    check to see if the two lists we're left with match.
    This solution destroyes the original list, we could
    easily add a step to copy it into a new list first to avoid
    destroying it.
    """
    n = 0
    curr = li.head
    while curr is not None:
        n += 1
        curr = curr._next
    
    li2 = LinkedList()
    k = n // 2
    while k > 0:
        popped_node = li.get_first()
        li2.insert(popped_node.data)
        k -= 1

    if n % 2 == 1:
        #Remove the middle element and discard it.
        _ = li.get_first()

    while not li2.is_empty():
        li2_el = li2.get_first()
        li_el = li.get_first()
        if li2_el.data != li_el.data:
            return False

    return True

def test_palindrome():
    a = ['aabbaa', 'catac', 'ababab']
    for x in a:
        print(x)
        li = LinkedList()
        li.build_from_collection(x)
        li.print_list()
        print('Is a palindrome:', is_a_palindrome(li))

#Problem 2.7
#Given two (singly) linked lists, determine if the two lists intersect.
#Return the intersecting node. Note that the intersection is defined
#based on reference, not value. That is, if the kth node of the first
#linked list, is the exact same node (by reference) as the jth node
#of the second linked list, then they are intersecting.
def intersection(a, b):
    """
    This solution runs in o(A + B) time and uses
    O(N) memory where N = max(A, B) for the seen
    hash table.
    """
    seen = {}
    curr = a.head
    while curr is not None:
        seen[curr] = 1
        curr = curr._next

    curr = b.head
    while curr is not None:
        try:
            int_node = seen[curr]
        except KeyError:
            curr = curr._next
        else:
            return int_node

    return None
