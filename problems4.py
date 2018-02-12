from graphs import bf_search, get_sample_graph
from trees import BinaryTreeNode, bst_insert

#Problem 4.1
#Given a directed graph, design an algorithm to find out whether there is
#a route between two nodes.
def route_between_two_nodes(s, t):
    """
    This solution runs a BFS starting at node s.
    For each node visited it checks to see if
    the visited node is t.
    """
    is_same_node = lambda x: if x is t: print('found!')
    bf_search(s, is_same_node)

def test_route():
    g = get_sample_graph()
    print('Graph:')
    for node in g.get_nodes():
        print(node)

    s = g.get_root()
    t = g.get_random_node()
    print('---')
    print('s: %s' % s)
    print('t: %s' % t)
    route_between_two_nodes(s, t)

#Problem 4.2
#Given a sorted (increasing order) array with unique integer elements,
#write an algorithm to create a binary search tree with minimal height.
def minimal_tree():
    a = [1, 2, 3, 4, 5]
    m = len(a) // 2
    
    root = BinaryTreeNode(a[m])
    i = m - 1
    j = m + 1
    while i >= 0 or j < len(a):
        left_tree_node = BinaryTreeNode(a[i])
        bst_insert(root, left_tree_node)
        i += 1

        right_tree_node = BinaryTreeNode(a[j])
        bst_insert(root, right_tree_node)
        j -= 1

    while i >= 0:
        left_tree_node = BinaryTreeNode(a[i])
        bst_insert(root, left_tree_node)

    while j < len(a):
        right_tree_node = BinaryTreeNode(a[j])
        bst_insert(root, right_tree_node)
