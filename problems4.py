from graphs import bf_search, get_sample_graph
from trees import BinaryTreeNode, bst_insert
from queues import MyQueue
from lists import LinkedList

#Problem 4.1
#Given a directed graph, design an algorithm to find out whether there is
#a route between two nodes.
def route_between_two_nodes(s, t):
    """
    This solution runs a BFS starting at node s.
    For each node visited it checks to see if
    the visited node is t.
    """
    is_same_node = lambda x: True if x is t else False
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
def minimal_tree(a):
    if len(a) == 0:
        return None

    m = len(a) // 2
    root = BinaryTreeNode(a[m])
    
    left_tree = minimal_tree(a[:m])
    right_tree = minimal_tree(a[m + 1:])
    
    root.left = left_tree
    root.right = right_tree
    
    return root

#Problem 4.3
#Given a binary tree, design an algorithm which creates a linked list
#of all the nodes at each depth (e.g. if you have a tree with depth D,
#you'll have D linked lists).
def list_of_depths(root):
    """
    This solution is a modification of breadth first search.
    """
    q = MyQueue()
    depth_lists = []

    seen = []
    q.add((root, 0))
    seen.append(root)

    while not q.is_empty():
        q.print_queue()
        node, depth = q.remove().data
        
        try:
            depth_lists[depth].insert(node)
        except IndexError:
            depth_lists.append(LinkedList())
            depth_lists[depth].insert(node)
        
        adjacent_nodes = [node.left, node.right]
        for child in adjacent_nodes:
            if child is not None and child not in seen:
                seen.append(child)
                q.add((child, depth + 1))

    return depth_lists

def test_list_of_depths():
    root = BinaryTreeNode(5)
    bst_insert(root, BinaryTreeNode(4))
    bst_insert(root, BinaryTreeNode(0))
    bst_insert(root, BinaryTreeNode(2))
    bst_insert(root, BinaryTreeNode(8))
    bst_insert(root, BinaryTreeNode(9))
    bst_insert(root, BinaryTreeNode(1))

    depth_lists = list_of_depths(root)
    for li in depth_lists:
        li.print_list()
