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

def bst_insert(root, node):
    if root is None:
        root = None
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

def inorder_traversal(node, visit):
    if node is not None:
        inorder_traversal(node.left, foo)
        visit(node)
        inorder_traversal(node.right, foo)

def preorder_traversal(node, foo):
    if node is not None:
        visit(node)
        preorder_traversal(node.left, foo)
        preorder_traversal(node.right, foo)

def postorder_traversal(node, foo):
    if node is not None:
        postorder_traversal(node.left, foo)
        postorder_traversal(node.right, foo)
        visit(node)
