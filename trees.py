class TrieNode:
    def __init__(self, label=None, alphabet='abcdefghijklmnopqrstuvwxyz'):
        self.label = label
        self.children = {x: None for x in alphabet}
        self.terminating = True

class BinaryTreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)

    def __str__(self):
        return str(self.data)

def bst_insert(root, node):
    if root is None:
        root = node
    else:
        if node.data <= root.data:
            if root.left is None:
                root.left = node
            else:
                return bst_insert(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                return bst_insert(root.right, node)

def search(root, node):
    if root is None:
        return False

    if root == node:
        return True

    return search(root.left) or search(root.right)

def inorder_traversal(node, visit):
    if node is not None:
        inorder_traversal(node.left, visit)
        visit(node)
        inorder_traversal(node.right, visit)

def preorder_traversal(node, visit):
    if node is not None:
        visit(node)
        preorder_traversal(node.left, visit)
        preorder_traversal(node.right, visit)

def postorder_traversal(node, foo):
    if node is not None:
        postorder_traversal(node.left, visit)
        postorder_traversal(node.right, visit)
        visit(node)

def max_depth(node):
    """
    Max depth of a binary tree is the longest root-to-leaf path. 
    Given a binary tree, find its max depth.
    Here, we define the length of the path to be the number of edges on that path, not the number of nodes.
    """
    def dfs(node):
        """
        Use DFS to calculate the number of nodes on the longest path from root to leaf.
        """
        if node is None:
            return 0
        return 1 + max(dfs(node.left), dfs(node.right))
    
    return dfs(node) - 1 if node else 0

def visible_tree_node(root: BinaryTreeNode) -> int:
    """
    In a binary tree, a node is labeled as "visible" if, 
    on the path from the root to that node, 
    there isn't any node with a value higher than this node's value.
    The root is always "visible" since there are no other nodes 
    between the root and itself. 
    Given a binary tree, count the number of "visible" nodes.
    """
    def dfs(root: BinaryTreeNode, max_element: int) -> int:
        if root is None:
            return 0
    
        total = 0
        if root.val >= max_element:
            total += 1

        total += dfs(root.left, max(root.val, max_element))
        total += dfs(root.right, max(root.val, max_element))
        
        return total
    
    return dfs(root, root.val) if root else 0

def is_balanced(tree: BinaryTreeNode) -> bool:
    def tree_height(tree: BinaryTreeNode) -> int:
        if tree is None:
            return 0
        
        left_height = tree_height(tree.left)
        right_height = tree_height(tree.right)
        if left_height == -1 or right_height == -1:
            return -1
        elif abs(left_height - right_height) > 1:
            return -1
        else:
            return 1 + max(left_height, right_height)
    
    return tree_height(tree) != -1
