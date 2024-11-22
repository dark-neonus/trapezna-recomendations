""" Module that contain all tools to work Matrix """
from typing import NewType

# Just create new type shortcut called "Matrix"
# So when you use "Matrix", python understand it as "list[list[str]]"
Matrix = NewType("Matrix", list[list[str]])
# We would use matrix to store screen or images buffers
#
# Example of matrix:
# .....
# .egg.
# .....
#
# We will save it in Matrix as [
# [".", ".", ".", ".", "."],
# [".", "e", "g", "g", "."],
# [".", ".", ".", ".", "."]
# ]

def create_matrix(width: int, height: int, fill_symbol=" ") -> Matrix:
    """ Create matrix of size `width`x`height`

    Args:
        width (int): width of matrix (number of columns)
        height (int): height of matrix (number of rows)
        fill_symbol (str, optional): Symbol to fill matrix. Defaults to " ".

    Returns:
        Matrix: matrix of size `width`x`height` with all tile set to `fill_symbol`
    
    Examples:
    >>> create_matrix(3, 2, '*')
    [['*', '*', '*'], ['*', '*', '*']]
    """
    result = []
    for _y in range(height):
        result.append([])
        for _x in range(width):
            result[-1].append(fill_symbol)
    return result

def get_matrix_width(matrix: Matrix) -> int:
    """ return matrix width

    Args:
        matrix (Matrix): source matrix

    Returns:
        int: width of given matrix
    """
    return len(matrix[0])

def get_matrix_height(matrix: Matrix) -> int:
    """ return matrix height

    Args:
        matrix (Matrix): source matrix

    Returns:
        int: height of given matrix
    """
    return len(matrix)

def matrix_get_at(x: int, y: int, matrix: Matrix, silent_erros: bool=False) -> str | None:
    """ Return value of tile at (y, x) in matrix

    Args:
        x (int): column of tile to get
        y (int): row of tile to get
        matrix (Matrix): source matrix
        silent_erros (bool): indicate if exception should be ignored if
            coordinates out of matrix boundaries. Default to False.

    Returns:
        str | None: symbol at (y, x) from matrix. If indexes out of matrix boundaries
            return None if `silent_errors`, otherwise raise exception
    >>> matrix_get_at(1, 1, [['1', '2', '3'], ['a', 'b', 'c']])
    'b'
    >>> matrix_get_at(0, 4, [['1', '2', '3'], ['a', 'b', 'c']], True) is None
    True
    >>> matrix_get_at(0, 4, [['1', '2', '3'], ['a', 'b', 'c']])
    Traceback (most recent call last):
        ...
    ValueError: Coordinates (x:0, y:4) are out of matrix size (w: 3, h: 2)
    """
    if (x < 0 or x >= get_matrix_width(matrix)) or (y < 0 or y >= get_matrix_height(matrix)):
        if silent_erros:
            return None
        raise ValueError(f"Coordinates (x:{x}, y:{y}) are out of matrix size \
(w: {get_matrix_width(matrix)}, h: {get_matrix_height(matrix)})")
    return matrix[y][x]

def matrix_set_at(x: int, y: int, value: str, matrix: Matrix, silent_erros: bool=False):
    """ Set tile at (y, x) in matrix to `value`

    Args:
        x (int): column of tile to get
        y (int): row of tile to get
        value (str): new value of tile at (y, x)
        matrix (Matrix): matrix to change
        silent_erros (bool): indicate if exception should be ignored if
            coordinates out of matrix boundaries. Default to False.

    >>> matrix = [['1', '2', '3'], ['a', 'b', 'c']]
    >>> matrix_set_at(0, 0, '*', matrix)
    >>> matrix
    [['*', '2', '3'], ['a', 'b', 'c']]
    >>> matrix_set_at(1, 6, '*', matrix, True)
    >>> matrix
    [['*', '2', '3'], ['a', 'b', 'c']]
    >>> matrix_set_at(1, 6, '*', matrix)
    Traceback (most recent call last):
        ...
    ValueError: Coordinates (x:1, y:6) are out of matrix size (w: 3, h: 2)
    >>> matrix_set_at(0, 0, 'abc', matrix)
    Traceback (most recent call last):
        ...
    ValueError: Invalid string format \"abc\". Must be string with length of 1
    """
    if (x < 0 or x >= get_matrix_width(matrix)) or (y < 0 or y >= get_matrix_height(matrix)):
        if silent_erros:
            return
        raise ValueError(f"Coordinates (x:{x}, y:{y}) are out of matrix size \
(w: {get_matrix_width(matrix)}, h: {get_matrix_height(matrix)})")
    elif not isinstance(value, str) or len(value) != 1:
        if silent_erros:
            return
        raise ValueError(f"Invalid string format \"{value}\". Must be string with length of 1")
    matrix[y][x] = value

def draw_matrix_on_matrix(source_matrix: Matrix, destination_matrix: Matrix,
                          d_x: int, d_y: int, silent_erros: bool=False):
    """ Draw `source_matrix` on `ddestination_matrix` biased by (`d_y`, `d_x`)

    Args:
        source_matrix (Matrix): source of new tiles
        destination_matrix (Matrix): source of base tiles
        d_x (int): delta x position of `source_matrix`
        d_y (int): delta y position of `source_matrix`
        silent_erros (bool, optional): indicate if exception should be ignored if
            coordinates out of matrix boundaries. Default to False.
    
    Examples:
    >>> source_matrix = [['1', '2', '3'], ['a', 'b', 'c']]
    >>> draw_matrix_on_matrix([['>'], ['<']], source_matrix, 1, 0)
    >>> source_matrix
    [['1', '>', '3'], ['a', '<', 'c']]
    >>> draw_matrix_on_matrix([['A'], ['B'], ['C'], ['D']], source_matrix, 0, -1, True)
    >>> source_matrix
    [['B', '>', '3'], ['C', '<', 'c']]
    >>> draw_matrix_on_matrix([['A'], ['B'], ['C'], ['D']], source_matrix, 0, -1)
    Traceback (most recent call last):
        ...
    ValueError: Coordinates (x:0, y:-1) are out of matrix size (w: 3, h: 2)
    """
    for source_y in range(get_matrix_height(source_matrix)):
        for source_x in range(get_matrix_width(source_matrix)):
            matrix_set_at(
                x = source_x + d_x,
                y = source_y + d_y,
                value = matrix_get_at(source_x, source_y, source_matrix, silent_erros),
                matrix = destination_matrix,
                silent_erros = silent_erros
                )

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
