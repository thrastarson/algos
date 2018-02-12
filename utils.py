import random
from graphs import Graph, GraphNode

def sort_string(w):
    return ''.join(sorted(w))

def get_random_list(size=10):
    return [random.randint(0, 100) for i in range(size)]

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

def is_sorted(a):
    return a == sorted(a)

def swap(a, i, j):
    a[i], a[j] = a[j], a[i]

def test_sorting(sort_foo, returns_sorted=True):
    a = [5, 4, 7, 1, 3, 2, 8, 6, 9]
    b = []
    c = [14]
    d = [5, 6, 7, 8]
    cases = [a, b, c, d]

    if returns_sorted:
        for _list in cases:
            sorted_list = sort_foo(_list)
            print(is_sorted(sorted_list), sorted_list)
    else:
        for _list in cases:
            sort_foo(_list)
            print(is_sorted(_list), _list)

def build_string(list_of_strings):
    """
    In some languages it can be handy to build a class,
    commonly called StringBuilder, to mitigate the time
    complexity of concatenating multiple strings.
    In many languages, including python, a str3 = str1 + str2
    operation copies str1 and str2 into a new string str3.
    This can quickly become expansive if done with little though.
    A workaround in Python is so elegant that a whole
    StringBuilder class is pretty unnecessary.
    It is implemented here as an exercise.
    """
    return ''.join(list_of_strings)
