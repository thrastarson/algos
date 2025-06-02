class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find(tree, val):
    if tree is None:
        return False
    
    if tree.val == val:
        return tree
    elif tree.val < val:
        return find(tree.right, val)
    else:
        return find(tree.left, val)

def insert(tree, val):
    if tree is None:
        return Node(val)
    
    if tree.val < val:
        tree.right = insert(tree.right, val)
    elif tree.val > val:
        tree.left = insert(tree.left, val)
    
    return tree

def is_valid_bst(root: Node) -> bool:
    """
    Given a binary tree, determine whether it is a binary search tree.
    """
    def dfs(root: Node, min_val: int, max_val: int) -> bool:
        if not root:
            return True
        
        if not (min_val < root.val < max_val):
            return False
        
        left_valid = dfs(root.left, min_val, root.val)
        right_valid = dfs(root.right, root.val, max_val)
    
        return left_valid and right_valid
    
    return dfs(root, float('-inf'), float('inf'))
    
def lca(bst: Node, p: int, q: int) -> int:
    """
    Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
    The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).
    """
    if not bst:
        return None
    
    if p < bst.val and q < bst.val:
        return lca(bst.left, p, q)
    
    if p > bst.val and q > bst.val:
        return lca(bst.right, p, q)
    
    return bst.val
