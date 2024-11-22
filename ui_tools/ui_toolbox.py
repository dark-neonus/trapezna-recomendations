""" Module that contain all thing needed for creating ui """
from ui_tools.matrix import (
    Matrix, get_matrix_width, get_matrix_height, matrix_set_at,
    create_matrix
)

def add_frame_to_matrix(matrix: Matrix, frame_symbol: str | None=None):
    """ Draw frame on matrix
    
    Exampele of frame:
        original:
        ......
        .egg..
        ......
        ......
        framed:
        ┌────┐
        │egg.│
        │....│
        └────┘

    Args:
        matrix (Matrix): matrix to draw frame on
        frame_symbol (str | None, optional): Symbol of frame.
            If set to None, normal frame will apper, otherwise
            frame will be made from `frame_symbol`. Defaults to None.
    """
    matrix_w = get_matrix_width(matrix)
    matrix_h = get_matrix_height(matrix)

    matrix_set_at(0, 0, frame_symbol or "┌", matrix)
    matrix_set_at(matrix_w - 1, 0, frame_symbol or "┐", matrix)
    matrix_set_at(0, matrix_h - 1, frame_symbol or "└", matrix)
    matrix_set_at(matrix_w - 1, matrix_h - 1, frame_symbol or "┘", matrix)

    for x in range(1, matrix_w - 1):
        matrix_set_at(x, 0, frame_symbol or "─", matrix)
        matrix_set_at(x, matrix_h - 1, frame_symbol or "─", matrix)

    for y in range(1, matrix_h - 1):
        matrix_set_at(0, y, frame_symbol or "│", matrix)
        matrix_set_at(matrix_w - 1, y, frame_symbol or "│", matrix)

def create_text_field(text: str, width: int, height: int, frame_symbol: str | None=None) -> Matrix:
    """ Create text field in format
    ┌───────────┐
    │   Meow    │
    └───────────┘

    Args:
        text (str): text to put in the frame
        width (int): width of frame
        height (int): height of frame_
        frame_symbol (str | None, optional): Symbol of frame.
            If set to None, normal frame will apper, otherwise
            frame will be made from `frame_symbol`. Defaults to None.

    Returns:
        Matrix: matrix for frame with given parameters
    """
    field_matrix = create_matrix(width, height)
    add_frame_to_matrix(field_matrix, frame_symbol)

    # Here will be logic to divide text to multyline when it too big
    text = text[:min(width - 2, len(text))]

    # Center text
    delta_x = (width - 2 - len(text)) // 2

    # Draw text on field_matrix
    center_y = height // 2
    for i, char in enumerate(text):
        matrix_set_at(1 + delta_x + i, center_y, char, field_matrix)

    return field_matrix
