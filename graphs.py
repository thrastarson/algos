import random
from queues import MyQueue
from utils import get_random_list

class GraphNode:
    #Implements a graph node with an adjacency list.
    def __init__(self, val=None, adjacent=None):
        self.val = val
        if adjacent is None:
            self.adjacent = []
        else:
            self.adjacent = adjacent
        self.marked = False

    def add_edge(self, node):
        self.adjacent.append(node)

    def __repr__(self):
        return 'GraphNode(%s)' % self.val

    def __str__(self):
        return str(self.val)

class Graph:
    #Implements a graph using adjacency lists.
    def __init__(self):
        self.nodes = []

    def add(self, node):
        self.nodes.append(node)

    def get_nodes(self):
        return self.nodes

    def size(self):
        return len(self.nodes)

    def __repr__(self):
        return 'Graph(%s)' % [str(node) for node in self.nodes]

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

def main():
    a = get_random_list()
    
    g = Graph()
    for x in a:
        node = GraphNode(val=x)
        g.add(node)

    nodes = g.get_nodes()
    for node in nodes:
        #Add two random directed edges for each node.
        node.add_edge(random.choice(nodes))
        node.add_edge(random.choice(nodes))
    print(g)

if __name__ == '__main__':
    main()
