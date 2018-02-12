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
        return '%3s -> %s' % (str(self.val), self.adjacent)

class Graph:
    #Implements a graph using adjacency lists.
    def __init__(self):
        self.nodes = []

    def add(self, node):
        self.nodes.append(node)

    def get_nodes(self):
        return self.nodes

    def get_root(self):
        if self.size() > 0:
            return self.nodes[0]
        else:
            return None

    def get_random_node(self):
        if len(self.nodes) > 1:
            return random.choice(self.nodes[1:])
        else:
            return None

    def reset_marked(self):
        for node in self.nodes:
            node.marked = False

    def size(self):
        return len(self.nodes)

    def __repr__(self):
        return 'Graph(%3s)' % self.nodes

def df_search(root, visit):
    visit(root)
    root.marked = True
    for node in root.adjacent:
        if node.marked is False:
            df_search(node, visit)

def bf_search(root, visit):
    q = MyQueue()
    root.marked = True
    q.add(root)
    
    while not q.is_empty():
        node = q.remove().data
        visit(node)
        for adjacent_node in node.adjacent:
            if adjacent_node.marked is False:
                adjacent_node.marked = True
                q.add(adjacent_node)

def get_sample_graph(size=10):
    a = get_random_list(size)
    g = Graph()
    for x in a:
        node = GraphNode(val=x)
        g.add(node)

    nodes = g.get_nodes()
    for i, node in enumerate(nodes):
        #Add two random directed edges for each node.
        index_range = [x for x in range(len(nodes)) if x != i]
        first_index = random.choice(index_range)
        node.add_edge(nodes[first_index])

        index_range = [x for x in range(len(nodes)) if x != i and x != first_index]
        second_index = random.choice(index_range)
        node.add_edge(nodes[second_index])

    return g

class MatrixGraph:
    #Implements a graph using an adjacency matrix.
    def __init__(self, size=10):
        self.size = size
        self.matrix = [[False for x in range(n)] for y in range(n)]

def main():
    g = get_sample_graph()
    
    for node in g.get_nodes():
        print(node)

    root = g.get_root()
    print('Depth First Search:')
    df_search(root, print)
    
    g.reset_marked()
    
    print('Breadth First Search:')
    bf_search(root, print)

if __name__ == '__main__':
    main()
