# trapezna-recomendations

## Elements
- session
- dish
- product

## Graph structure
```python
graph: dict[str, list[str]]
{
    "session_1" : ["product_1", "product_2", "product_3", "product_1"],
    "session_2" : ["product_7", "product_9"],
    ...
}
```
> __Warning__: Products can repeat in sessions\
    example: {"session_1" : ["product_1", "product_2", "product_1"]}

## Who doing what
 - `main.py`, `ui.py` - Nazar
 - `graph_logic.py` - Iia, Oleksii, Maria
 -  `graph_visualization.py` - Daryna

    > ### Iia:
    > - `dishes_to_products()`
    > - `calculate_dishes_power()`
    > - `divide_dishes_by_type()`

    > ### Oleksii:
    > - `calculate_products_power()`
    > - `sort_dishes()`

    > ### Maria:
    > - `save_graph()`
    > - `load_graph()`
    > - `add_session()`


## Logic
`UI` mean ui and app loop

### Input
`UI` -[ list of selected dishes in session ]-> `dishes_to_products()` -[ list of selected products in session]-> `add_session()` -[ modified graph ]-> `save_graph()`

### Output (Sorting to UI)
`load_graph()` -[ graph ]-> `calculate_products_power()` -[ dict of products with their powers ]-> `calculate_dishes_power()` -[ dict of dishes with their powers ]-> `sort_dishes()` -[ list of sorted dishes by power ]-> `divide_dishes_by_type()` -[ three list of dishes according to their type, sorted ]-> `UI`

### Visualization
`UI` -[ just call function ]-> `graph_visualization()`

## Commits style
Please follow next git commits style for clarity of commits (read about it by link)
### How make commits
https://www.freecodecamp.org/news/how-to-write-better-git-commit-messages/

### Structure:
> \<type>[optional scope]: \<description>
> 
> [optional body]

### Examples:
> feat(file_with_func1.py): write logic for func1() function
> 
> Changed documentation a little

> test: write doctests for func2() function

> chore(README.md): fix typo in 3-rd section