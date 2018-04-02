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
