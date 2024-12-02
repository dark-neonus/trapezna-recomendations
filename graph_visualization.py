""" Module to make graph visualization """

import doctest
import doctest
from graph_logic import Graph
from graphviz import Digraph


def organise_graph(graph: Graph):
    '''
    Converts Graph type (dict[str, list[str]]) to list(tuple)

    Args:
        graph (dict[str, list[str]]): graph to vizualize
    Returns:
        edge_list (list(tuple)): a list of graph edges
    Examples:
    >>> organise_graph({"session_1" : ["product_1", "product_2", "product_3", "product_1"],\
    "session_2" : ["product_7", "product_9"]})
    [('session_1', 'product_1'), ('session_1', 'product_2'), ('session_1', 'product_3'), ('session_1', 'product_1'), ('session_2', 'product_7'), ('session_2', 'product_9')]
    '''
    edge_list = []
    for key, values in graph.items():
        for value in values:
            edge_list.append((key, value))
    return edge_list


def generate_graph_png(edge_list, output_file="graph.png"):
    """
    Creates a PNG-image of graph using a list of edges

    Args:
        edge_list (list[tuple]): list of edges
        output_file (str): pathway
    Returns:
        None
    Example:
    """
    dot = Digraph(format='png')
    for edge in edge_list:
        dot.edge(edge[0], edge[1])

    dot.render(output_file, cleanup=True)

def test_visualization():
    """
    Function with predefined graph to test visualization
    """
    test_graph = {
        "session_1": ["product_1", "product_2", "product_6"],
        "session_2": ["product_7", "product_9"],
    }

    edges = organise_graph(test_graph)
    print(f"A list of edges:{edges}")
    generate_graph_png(edges, output_file="test_graph")

if __name__ == "__main__":
    doctest.testmod()
    doctest.testmod()
    test_visualization()