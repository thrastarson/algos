def bin_search(a, key, start, end):
    if start > end:
        return -1

    m = (start + end) // 2
    if key == a[m]:
        return m
    elif key <= a[m]:
        return bin_search(a, start, m-1)
    else:
        return bin_search(a, m+1, end)

def search(a, key, start, end):
    if start > end:
        return -1

    m = (start + end) // 2
    if key == a[m]:
        return m

    if a[start] <= a[m]:
        #a[start..m] is sorted.
        #check if key lies in this half or the other.
        if key >= a[start] and key <= a[m]:
            return search(a, key, start, m-1)
        else:
            return search(a, key, m+1, end)
    else:
        #a[start..m] is not sorted,
        #so a[m..r] must be sorted.
        if key >= a[m] and key <= a[end]:
            return search(a, key, m+1, end)
        else:
             search(a, key, start, m-1)


def check_bst(node, min_val=float('-inf'), max_val=float('inf')):
    if node is None:
        return True

    if node.data < min_val or node.data > max_val:
        return False

    return (check_bst(node.left, max_val=node.data - 1)
            and check_bst(node.right, min_val=node.data + 1))













