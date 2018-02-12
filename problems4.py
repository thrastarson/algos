from graphs import bf_search, get_sample_graph

#Problem 4.1
#Given a directed graph, design an algorithm to find out whether there is
#a route between two nodes.
def route_between_two_nodes(s, t):
    """
    This solution runs a BFS starting at node s.
    For each node visited it checks to see if
    the visited node is t.
    """
    is_same_node = lambda x: if x is t: print('found!')
    bf_search(s, is_same_node)

def test_route():
    g = get_sample_graph()
    print('Graph:')
    for node in g.get_nodes():
        print(node)

    s = g.get_root()
    t = g.get_random_node()
    print('---')
    print('s: %s' % s)
    print('t: %s' % t)
    route_between_two_nodes(s, t)
