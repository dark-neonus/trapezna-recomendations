""" Module with main graph and recommendation logic """

import json
from typing import NewType
# Just create new type shortcut called "Graph"
# So when you use "Graph", python understand it as "dict[str, list[str]]"
Graph = NewType("Graph", dict[str, list[str]])


# Mariia
def save_graph(graph: Graph, filename: str):
    """ Save graph to file (json)

    Args:
        graph (Graph): graph to save
        filename (str): name of destination file (json)
    
    Examples:
    ...
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(graph, f, ensure_ascii=False, indent=4)

def load_graph(filename: str) -> Graph:
    """ Read and return graph from file `filename` (json)

    Args:
        filename (str): name of file with graph (json)

    Returns:
        Graph: graph readed from file
    
    Examples:
    ...
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("{\n}")
        return {}

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
    >>> add_session({}, ["product_1", "product_4", "product_3", "product_2", "product_9"])
    {'session_1': ['product_1', 'product_4', 'product_3', 'product_2', 'product_9']}
    >>> add_session({'session_1': ['product_1', 'product_4', 'product_3', 'product_2', \
'product_9']},\
 ["product_10", "product_45", "product_33", "product_26", "product_9"])
    {'session_1': ['product_1', 'product_4', 'product_3', 'product_2', 'product_9'], 'session_2':\
 ['product_10', 'product_45', 'product_33', 'product_26', 'product_9']}
    """
    num_of_sess = len(graph)
    graph[f'session_{num_of_sess+1}'] = products
    return graph

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
    >>> dishes_power = {'product_a': 4, 'product_b': 3, 'product_c': 3, 'product_d': 1}
    >>> sort_dishes(dishes_power)
    ['product_a', 'product_b', 'product_c', 'product_d']
    >>> dishes_power = {'product_a': 1, 'product_b': 3, 'product_c': 3, 'product_d': 15}
    >>> sort_dishes(dishes_power)
    ['product_d', 'product_b', 'product_c', 'product_a']
    """
    dish_and_power = sorted(list(dishes_power.items()), key = lambda x: x[1], reverse = True)
    return [dish[0] for dish in dish_and_power]


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
