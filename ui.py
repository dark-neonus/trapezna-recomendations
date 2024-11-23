""" UI module with main program loop """

import curses

from ui_tools.matrix import (Matrix, create_matrix, fill_matrix,
                             draw_matrix_on_screen, draw_matrix_on_matrix)
from ui_tools.ui_toolbox import create_text_field
from graph_logic import divide_dishes_by_type

UI_WIDTH = 60
UI_HEIGHT = 30

# Food data for testing
TESTING_FOOD_DATA = (
    ["борщ", "гороховий суп"],
    ["картопля фрі", "рис", "каша пшенична з сиром фета", "булгур", "омлет", "вівсяка", "котлета"],
    ["компот", "сік апельсиновий", "сік яблучний"]
    )

def handle_terminal_size(stdscr: curses.window) -> bool:
    """ Check if terminal is big enough. If it isnt, ask user to resize it """
    # Dont start app until terminal big enough
    while True:
        height, width = stdscr.getmaxyx()

        if width < UI_WIDTH or height < UI_HEIGHT:
            # Display a warning and ask the user to resize
            stdscr.clear()
            stdscr.addstr(0, 0, "Terminal is too small!")
            stdscr.addstr(1, 0, f"Minimum size: {UI_WIDTH}x{UI_HEIGHT}")
            stdscr.addstr(2, 0, f"Current size: {width}x{height}")
            stdscr.addstr(3, 0, "Resize the terminal.")
            stdscr.refresh()

            key = stdscr.getch()
            # ESC key code - 27
            if key in [ord("q"), ord("Q"), 27]:
                # Return ui_runs = False if q is pressed
                return False
        else:
            break  # Terminal is large enough

    return True

def init_curses() -> curses.window:
    """ Init curses library and check if terminal is big enogh

    Returns:
        curses.window: object of curses output window
    """
    # Object of curses librart window(canvas)
    # on which all output will be drawn
    stdscr = curses.initscr()

    # Make terminal cursor invinsible
    curses.curs_set(0)

    # Set waiting time for "stdscr.getch()" to 100ms
    # So "key = stdscr.getch()" wont stop program like input(), but wil wait for 100ms
    stdscr.timeout(500)

    # Check if terminal size is okay for start
    handle_terminal_size(stdscr)

    return stdscr

def main_loop(testing_mode: bool=False):
    """ Main loop of UI program """
    stdscr = init_curses()

    # Flag that indicate if program should still run
    ui_runs = True
    # Terminal screen matrix
    screen_matrix = create_matrix(UI_WIDTH, UI_HEIGHT)
    # Variable to hold food values for each food row
    typed_food = ([], [], [])

    while ui_runs:
        if testing_mode:
            typed_food = TESTING_FOOD_DATA
        else:
            raise NotImplementedError()
        build_ui(screen_matrix, typed_food)
        draw_matrix_on_screen(stdscr, screen_matrix)
        ui_runs = handle_keys_input(stdscr, ui_runs) and handle_terminal_size(stdscr)

def handle_keys_input(stdscr: curses.window, ui_runs: bool) -> bool:
    """ Handle keys input"""
    key = stdscr.getch()
    # ESC key code - 27
    if key in [ord("q"), ord("Q"), 27]:
        ui_runs = False

    return ui_runs

def build_ui(screen_matrix: Matrix, typed_food: tuple[list[str], list[str], list[str]]
             ) -> Matrix:
    """ Build UI screen matrix """
    fill_matrix(screen_matrix, " ")
    for row in range(3):
        for column in range(min(3, len(typed_food[row]))):
            dish_frame = create_text_field(typed_food[row][column], 17, 7)
            draw_matrix_on_matrix(dish_frame, screen_matrix, column*20, row*8)


if __name__ == "__main__":
    main_loop(testing_mode=True)
