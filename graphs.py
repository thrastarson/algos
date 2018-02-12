from queues import MyQueue

class Graph:
    #Implements a graph using adjacency lists.
    class GraphNode:
        def __init__(self, name=None, adjacent=None):
            self.name = name
            if adjacent is None:
                self.adjacent = []
            else:
                self.adjacent = adjacent
            self.marked = False

    def __init__(self):
        self.nodes = []

def df_search(root, visit):
    visit(root)
    root.marked = True
    for node in root.adjacent:
        if node.marked is False:
            df_search(node, visit)

def bf_search(root, visit):
    q = MyQueue()
    q.add(root)
    
    while not q.is_empty():
        node = q.remove()
        node.marked = True
        visit(node)
        
        for adjacent_node in node.adjacent:
            if adjacent_node.marked is False:
                adjacent_node.marked = True
                q.add(adjacent_node)


class MatrixGraph:
    #Implements a graph using an adjacency matrix.
    def __init__(self, size=10):
        self.size = size
        self.matrix = [[False for x in range(n)] for y in range(n)]
        
