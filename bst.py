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
    