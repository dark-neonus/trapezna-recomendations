""" Module with main graph and recommendation logic """

import json
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
FOOD_DATABASE_FILE = 'menu.json'

# WARNING: We have no separate list of products.
#   To add new product we need to add it to some dish

# Iia
def structure_menu(menu: dict[dict[str]]) -> dict[str]:
    """ Auxiliary function for transforming dictionary of dictionaries,
    which is a menu, into simple dictionary. Turns structure
    { type:
        dish: [products],
        dish: [products]
    }
    into
    {   dish: (type, [products]),
        dish: (type, [products])
    }
    
    This simplifies working with menu data by flattening it while 
    preserving the association between dishes, their types, and products.

    Args:
        menu (dict): a menu which has to be restructurised

    Returns:
        dict: a menu with valid structure
    """
    new_menu = {}
    for dish_type in menu:
        for dish in menu[dish_type]:
            new_menu[dish] = (dish_type, menu[dish_type][dish])
    return new_menu

def dishes_to_products(dishes: list[str]) -> list[str]:
    """ Return all productes presented in given `dishes`
    based on information in `FOOD_DATABASE_FILE`.
    Products can repeat.

    Args:
        dishes (list[str]): dishes selected by user

    Returns:
        list[str]: products presented in `dishes`
    
    Examples:
    >>> dishes_to_products(['Крем суп з броколі','Макарони з сиром','Компот'])
    ['Броколі', 'Тісто', 'Сир', 'Ягоди']
    """
    with open(FOOD_DATABASE_FILE, 'r', encoding="utf-8") as file:
        menu = json.load(file)
    menu = structure_menu(menu)
    product_query = []
    for dish in dishes:
        product_query.extend(menu[dish][-1])
    return product_query


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
    >>> query = calculate_dishes_power({"Броколі":1, "Картопля":10, "Буряк":3})
    >>> list(query.items())[:3]
    [('Крем суп з броколі', 1), ('Борщ з мʼясом', 13), ('Суп грибний', 10)]
    """
    with open(FOOD_DATABASE_FILE, 'r', encoding="utf-8") as file:
        menu = json.load(file)
    menu = structure_menu(menu)
    query = {}
    for dish, dish_info in menu.items():
        power = 0
        for product, product_p in products_power.items():
            power += product_p if product in dish_info[-1] else 0
        query[dish] = power
    return query



def divide_dishes_by_type(dishes: list[str]) -> tuple[list[str], list[str], list[str]]:
    """ Divide list of sorted dishes into three lists
    by dish type. Info from `FOOD_DATABASE_FILE`

    Args:
        dishes (list[str]): list of sorted dishes

    Returns:
        tuple[list[str], list[str], list[str]]: three lists of sorted dishes
            divided by their type

    Example:
    >>> divide_dishes_by_type(['Борщ з мʼясом', 'Суп грибний', 'Крем суп з броколі', \
        'Піца', 'Кава'])
    (['Борщ з мʼясом', 'Суп грибний', 'Крем суп з броколі'], ['Піца'], ['Кава'])
    """
    with open(FOOD_DATABASE_FILE, 'r', encoding="utf-8") as file:
        menu = json.load(file)
    menu = list(menu.items())
    query = [[dish for dish in dishes if dish in section[1]] for section in menu]
    return tuple(query)


# Oleksii
def calculate_products_power(graph: Graph) -> dict[str, int]:
    """ Calculate power of all product based on their
        connections in `graph`.

    Args:
        graph (Graph): graph with sessions and products connections

    Returns:
        dict[str, int]: dictionary where key is name of product
            and value is power of product
    
    Example:
    ... 
    """
    pass


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
