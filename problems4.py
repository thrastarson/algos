import random
from itertools import permutations
from graphs import bf_search, get_sample_graph, GraphNode, Graph
from trees import BinaryTreeNode, bst_insert, search
from queues import MyQueue
from stacks import Stack
from lists import LinkedList

#The following problems are from the book Cracking the Coding Interview
#by Gayle Laakmann McDowell. I reserve no rights for them.

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

def get_binary_tree():
    root = BinaryTreeNode(5)
    bst_insert(root, BinaryTreeNode(4))
    bst_insert(root, BinaryTreeNode(0))
    bst_insert(root, BinaryTreeNode(2))
    bst_insert(root, BinaryTreeNode(8))
    bst_insert(root, BinaryTreeNode(9))
    bst_insert(root, BinaryTreeNode(1))
    return root

def test_list_of_depths():
    root = get_binary_tree()
    depth_lists = list_of_depths(root)
    for li in depth_lists:
        li.print_list()

#Problem 4.4
#Implement a function to check if a binary tree is balanced.
#For the purposes of this question, a balanced tree is defined
#to be a tree such that the heights of the two subtrees of any
#node never differ by more than one.
def check_balanced(root):
    if root is None:
        return True

    left_height = height(root.left)
    right_height = height(root.right)
    balanced = abs(left_height - right_height) <= 1

    return (balanced 
            and check_balanced(root.left) 
            and check_balanced(root.right))

def test_balanced():
    root = get_binary_tree()
    print(check_balanced(root))

def test_height():
    root = get_binary_tree()
    print(height(root))

def height(root):
    if root is None:
        return 0
    elif root.left is None and root.right is None:
        return 1
    else:
        left_height = height(root.left)
        right_height = height(root.right)
        return max(left_height, right_height) + 1

#Problem 4.5
#Implement a function to check if a binary tree is a binary
#search tree.
def validate_bst(root):
    """
    This solution does an inorder traversal, checking
    if the BST conditions hold for every node 
    in the tree.
    """
    if root is not None:
        validate_bst(root.left)
        
        if root.left is not None:
            if root.left.data > root.data:
                return False

        if root.right is not None:
            if root.right.data <= root.data:
                return False

        validate_bst(root.right)
    return True

#Problem 4.6
#Write an algorithm to find the 'next' node (i.e. in-order successor)
#of a given node in a binary search tree. You may assume that each
#node has a link to its parent.
def successor(node):
    if node is None:
        return Node

    if node.right is None:
        return node.parent

    curr_node = node.right
    while curr_node.left is not None:
        curr_node = curr_node.left

    return curr_node

#Problem 4.7
#You are given a list of projects and a list of dependencies
#(which is a list of pairs of projects, where the second project
#is dependent on the first project). All of a project's dependencies
#must be built before the project is. Find a build order that will
#allow the projects to be built. If there is no valid build order,
#return an error.
#Example:
#Input: projects     a, b, c, d, e, f
#       dependencies (a, d), (f, b), (b, d), (f, a), (d, c)
#Output: f, e, a, b, d, c
def build_order(projects, dependencies):
    """
    The solution to this problem is a topological search.
    It builds a graph from the tasks and dependencies,
    finds the independent tasks, and then performs a breadth first
    search to identify a legal topological ordering.
    """
    #Build a graph where each projects is a node
    #and each dependency is a directed edge from
    #the dependent project to the earlier project.
    node_dict = {x: GraphNode(val=x) for x in projects}
    for dependency in dependencies:
        first, second = dependency
        node_dict[second].add_edge(node_dict[first])
    
    g = Graph()
    for node in node_dict.values():
        g.add(node)

    nodes = node_dict.values()
    independents = [node for node in nodes if len(node.adjacent)==0]

    for node in nodes:
        #Delete all edges from node.
        node.adjacenct = []

    for dependency in dependencies:
        #Flip edge from original setup. Now projects that
        #come first point to ones that should follow
        first, second = dependency
        node_dict[first].add_edge(node_dict[second])

    q = MyQueue()
    for node in independents:
        q.add(node)

    task_list = []
    while not q.is_empty():
        node = q.remove().data
        task_queue.append(node.val)
        node.marked = True
        for adjacent_node in node.adjacent:
            if adjacent_node.marked is False:
                adjacent_node.marked = True
                q.add(adjacent_node)

    return task_list

#Problem 4.8
#Design an algorithm and write code to find the first common
#ancestor of two nodes in a binary tree. Avoid storing additional
#nodes in a data structure. Note: This is not necessarily
#a binary search tree.
def first_common_ancestor(root, s, t):
    curr_node = root
    both_in_left = search(curr_node.left, s) and search(curr_node.left, t)
    both_in_right = search(curr_node.right, s) and search(curr_node.right, t)
    while both_in_left or both_in_right:
        if both_in_left:
            curr_node = curr_node.left
        elif both_in_right:
            curr_node = curr_node.right

    return curr_node

#Problem 4.9
#A binary search tree was created by traversing through an array
#from left to right and inserting each element. Given a binary
#search tree with distinct elements, print all possible arrays
#that could have led to this tree.
def bst_sequences(root):
    """
    This is a Python implementation of Gayle's solution from CtCI.
    I struggled with this problem so I just want to move past it.
    """
    result = LinkedList()

    if root is None:
        result.insert(LinkedList())
        return result

    prefix = LinkedList()
    prefix.add(root.data)

    #Recurse on left and right subtrees
    left_sequences = bst_sequences(root.left)
    right_sequences = bst_sequences(root.right)

    #Weave together each list from the left and right sides.
    while not left_sequences.is_empty():
        left = left_sequences.get_first().data
        while not right_sequences.is_empty():
            right = right_sequences.get_first().data
            weaved = LinkedList()
            weave_lists(left, right, weaved, prefix)
            result.add_all(weaved)

    return result

def weave_lists(first, second, results, prefix):
    """
    Weave lists together in all possible ways. The algorithm works
    by removing the head from one list, recursing, and then doing
    the same thing with the other list.
    """
    #One list is empty. Add a remainder [to a cloned] prefix and store results.
    if first.is_empty() or second.is_empty():
        result = prefix.clone()
        result.add_all(first)
        result.add_all(second)
        results.insert(result)
        return

    #Recurse with head of first added to the prefix. Removing the head
    #will damage first, so we'll need to put it back where we found it
    #afterwards.
    head_first = first.get_first().data
    prefix.insert_last(head_first)
    weave_lists(first, second, results, prefix)
    _ = prefix.get_last()
    first.insert(head_first)

    #Do the same thing with second, damaging and then restoring the list.
    head_second = second.get_first().data
    prefix.insert_last(head_second)
    weave_lists(first, second, results, prefix)
    _ = prefix.get_last()
    second.insert(head_second)

#Problem 4.10
#T1 and T2 are two very large binary trees, with T1 much bigger than T2.
#Create an algorithm to determine if T2 is a subtree of T1.
def check_subtree(t1, t2):
    t1_string = data_string(t1)
    t2_string = data_string(t2)
    return t1_string in t2_string

def data_string(node, li=None):
    if li is None:
        li = []

    if node is not None:
        li.append(node.data)
        data_string(node.left, li)
        data_string(node.right, li)

    return '*'.join(li)

#Problem 4.11
#You are implementing a binary tree class from scratch which, in addition to
#insert, find, and delete, has a method getRandomNode() which returns a random
#node from the tree. All nodes should be equally likely to be chosen.
#Design and implement an algorithm for getRandomNode, and explain how you would
#implement the rest of the methods.
class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, node, root=self.root):
        if root is None:
            self.root = node
        else:
            if node.data <= root.data:
                if root.left is None:
                    root.left = node
                else:
                    self.insert(node, root.left)
            else:
                if root.right is None:
                    root.right = node
                else:
                    self.insert(node, root.right)

        self.size += 1

    def find(self, node_no, node=self.root, count=0):
        if node is not None:
            self.find(node_no, node.left, count)
            if count == node_no:
                return node
            else:
                count += 1
            self.find(node_no, node.right, count)

    def get_random_node(self):
        node_no = random.rand_int(1, self.size)
        node = self.find(node_no)
        return node

    def delete(self, node):
        parent = node.parent
        if parent.left == node:
            parent.left = None
        else:
            parent.right = None

        left = node.left
        node = node.right
        self.insert(left)

#Problem 4.12
#You are given a binary tree in which each node contains an integer value
#(which might be positive or negative). Design an algorithm to count
#the number of paths that sum to a given value. The path does not need
#to start or end at the root or a leaf, but it must go downwards
#(traveling only from parent nodes to child nodes).
def paths_with_sum(root, target):
    """
    This solution is a direct python implementation of Gayle's solution
    in CtCI.
    """
    return count_paths_with_sum(root, target, 0, path_count):

def count_paths_with_sum(node, target, running_sum, path_count)
    if node is None:
        return 0

    #Count paths with sum ending at the current node.
    running_sum += node.data
    current_sum = running_sum - target
    total_paths = path_count.get(current_sum, 0)

    #If runnin_sum equals target_sum, then one additional path
    #starts at root. Add in this path.
    if running_sum == target:
        total_paths += 1

    #increment path_count, recurse, then decrement path_count.
    total_paths += count_paths_with_sum(node.left, target, running_sum, path_count)
    total_paths += count_paths_with_sum(node.right, target, running_sum, path_count)
    increment_path_count(path_count, running_sum, -1)

    return total_paths

def increment_path_count(path_count, key, delta):
    new_count = path_count.get(key, 0) + delta
    if new_count == 0:
        #Remove when zero to reduce space usage.
        _ = path_count.pop(key, None)
    else:
        path_count[key] = new_count
