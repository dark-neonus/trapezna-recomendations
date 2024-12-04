from manim import *

def organise_graph(graph_data):
    """
    Converts a graph from a dictionary of nodes and their neighbors to an edge list.

    Args:
        graph_data (dict): A dictionary where keys are nodes (e.g., session names) and values are lists of neighbors (e.g., products related to the session).

    Returns:
        list: A list of tuples, each representing an edge between two nodes (source, destination).

    Example:
        Input:
        {
            "session_1": ["product_1", "product_2", "product_6"],
            "session_2": ["product_7", "product_9"]
        }

        Output:
        [
            ("session_1", "product_1"),
            ("session_1", "product_2"),
            ("session_1", "product_6"),
            ("session_2", "product_7"),
            ("session_2", "product_9")
        ]
    """
    edge_list = []
    for key, values in graph_data.items():
        # For each neighbor in the list of neighbors, create an edge
        for value in values:
            edge_list.append((key, value))  # Add the edge (key, value) to the edge_list
    return edge_list


def create_scene(graph_data):
    """
    Creates and renders a scene with a graph visualization.

    The function sets up a simple graph with nodes (sessions and products) and edges
    that represent relationships between them. It uses Manim's Graph class to visualize
    the graph and plays the animation.
    Args:
        graph_data(dict): a dict with sessions
    Returns:
        Scene: The scene object with the graph animation.
    Example:
        graph_data = {
        "session_1": ["product_1", "product_2", "product_6"],
        "session_2": ["product_7", "product_9"],
    }
    """
    scene = Scene()  # Create a new scene object

    edge_list = organise_graph(graph_data)

    # Find unique nodes (both sessions and products) from the edge list
    vertices = {node for edge in edge_list for node in edge}

    # Create the graph using the edge list and the list of vertices
    graph = Graph(vertices, edge_list, layout="spring", vertex_config={"color": BLUE}, edge_config={"color": WHITE})
    scene.play(Create(graph)) # Play the scene
    scene.wait(2)  # Wait 2 seconds after the animation

    return scene

# Example graph data (sessions and associated products)
graph_data = {
    "session_1": ["product_1", "product_2", "product_6"],
    "session_2": ["product_7", "product_9"],
}
# Create the scene and render it
if __name__ == '__main__':
    scene = create_scene(graph_data)
    scene.render(True)
