""" Module with main graph and recommendation logic """

from typing import NewType

# Just create new type shortcut called "Graph"
# So when you use "Graph", python understand it as "dict[str, list[str]]"
Graph = NewType("Graph", dict[str, list[str]])


# Maria
def save_graph(graph: Graph, filename: str):
    """ Save graph to file (json)

    Args:
        graph (Graph): graph to save
        filename (str): name of destination file (json)
    
    Examples:
    ...
    """
    pass

def load_graph(filename: str) -> Graph:
    """ Read and return graph from file `filename` (json)

    Args:
        filename (str): name of file with graph (json)

    Returns:
        Graph: graph readed from file
    
    Examples:
    ...
    """
    pass

def add_session(graph: Graph, products: list[str]):
    """ Modify `graph` by adding session with `products` to it

    Session format:
    `session_x`
    where x is the number of session

    Session example:
    `"session_2" : ["product_7", "product_9"]`

    Args:
        graph (Graph): graph to modify
        products (list[str]): products from new session

    Examples:
    ...
    """
    pass


# Path to database(just json) with all dishes
# and information about each dish
FOOD_DATABASE_FILE = "path_to_food_database"

# WARNING: We have no separate list of products.
#   To add new product we need to add it to some dish

# Iia
def dishes_to_products(dishes: list[str]) -> list[str]:
    """ Return all productes presented in given `dishes`
    based on information in `FOOD_DATABASE_FILE`.
    Products can repeat.

    Args:
        dishes (list[str]): dishes selected by user

    Returns:
        list[str]: products presented in `dishes`
    
    Examples:
    ...
    """
    pass

def calculate_dishes_power(products_power: dict[str, int]
                           ) -> dict[str, int]:
    """ Calculate power of all dishes.
    List of all dishes we get from `FOOD_DATABASE_FILE`.

    Args:
        products_power (dict[str, int]): dictionary where
            key is name of product and value is its power.

    Returns:
        dict[str, int]: dictionary where key is name of dish
            and value is dishes power
    
    Example:
    ...
    """
    pass

def divide_dishes_by_type(dishes: list[str, int]) -> tuple[list[str], list[str], list[str]]:
    """ Divide list of sorted dishes into three lists
    by dish type. Info from `FOOD_DATABASE_FILE`

    Args:
        dishes (list[str, int]): list of sorted dishes

    Returns:
        tuple[list[str], list[str], list[str]]: three lists of sorted dishes
            divided by their type

    Example:
    ...
    """
    pass




# Oleksii
def calculate_products_power(graph: dict[str, list[str]]) -> dict[str, int]:
    """ Calculate power of all product based on their
        connections in `graph`.

    Args:
        graph (Graph): graph with sessions and products connections

    Returns:
        dict[str, int]: dictionary where key is name of product
            and value is power of product
    
    Example:
    >>> graph = {
    ...     "session_1" : ["product_1", "product_2", "product_3", "product_1"],
    ...     "session_2" : ["product_7", "product_9"]
    ... }
    >>> calculate_products_power(graph)
    {'product_1': 2, 'product_2': 1, 'product_3': 1, 'product_7': 1, 'product_9': 1}

    >>> graph = {
    ...     "session_1": ["product_a", "product_b", "product_c", "product_a", "product_a"],
    ...     "session_2": ["product_b", "product_c", "product_c"],
    ...     "session_3": ["product_a", "product_d", "product_b"]
    ... }
    >>> calculate_products_power(graph)
    {'product_a': 4, 'product_b': 3, 'product_c': 3, 'product_d': 1}
    
    """
    product_power = {}

    for products in graph.values():
        for product in products:
            if product in product_power:
                product_power[product] += 1
            else:
                product_power[product] = 1
    return product_power


def sort_dishes(dishes_power: dict[str, int]) -> list[str]:
    """ Sort dishes based on their power.
    Dishes with more power appear first.

    Args:
        dishes_power (dict[str, int]): dictionary where key is dish name
            and value is dish power

    Returns:
        list[str]: sorted list of dishes

    Example:
    ...
    """
    pass



if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
