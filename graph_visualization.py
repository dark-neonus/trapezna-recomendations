""" Module to make graph visualization """

from graph_logic import Graph


def organise_graph(graph: Graph):
    '''
    {
    "session_1" : ["product_1", "product_2", "product_3", "product_1"],
    "session_2" : ["product_7", "product_9"],
    }
    '''
    edge_list = []
    for key, values in graph.items():
        for value in values:
            edge_list.append((key, value))
    return edge_list


def graph_visualization(edge_list):
    """ Function that make graph visualization.

    Graph format: `dict[str, list[str]]`

    Args:
        graph (Graph): graph to visualize
    """

    dot_content = "digraph {\n"
    for tple in edge_list:
        dot_content += f"{tple[0]} -> {tple[1]}\n"
    dot_content += "}"
    return dot_content

print(graph_visualization([('session_1', 'product_1'), ('session_1', 'product_2'), ('session_1', 'product_3'), ('session_1', 'product_1'), ('session_2', 'product_7'), ('session_2', 'product_9')]))

def test_visualization():
    """ Function with predefined graph to test visualization """
    # Here you need to create small graph and cal visualization
    # Just to test if graph visualization works as expected
    # Also print graph before visualization
    pass


if __name__ == "__main__":
    test_visualization()
