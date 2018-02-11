class Graph:
    #Implements a graph using adjacency lists.
    class GraphNode:
        def __init__(self, name=None, children=None):
            self.name = name
            if children is None:
                self.children = []
            else:
                self.children = children

    def __init__(self):
        self.nodes = []

class MatrixGraph:
    #Implements a graph using an adjacency matrix.
    def __init__(self, size=10):
        self.size = size
        self.matrix = [[False for x in range(n)] for y in range(n)]
        
