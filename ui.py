""" UI module with main program loop """

import curses

from ui_tools.matrix import (Matrix, create_matrix, fill_matrix,
                             draw_matrix_on_screen, draw_matrix_on_matrix)
from ui_tools.ui_toolbox import create_text_field
from graph_logic import divide_dishes_by_type

UI_WIDTH = 90
UI_HEIGHT = 30

DISH_PER_DISPLAY = 5
DISH_BLOCK_WIDTH = UI_WIDTH // DISH_PER_DISPLAY - 2

# Food data for testing
TESTING_FOOD_DATA = [
    ["борщ", "гороховий суп"],
    ["картопля фрі", "рис", "каша пшенична з сиром фета", "булгур", "омлет", "вівсяка", "котлета"],
    ["компот", "сік апельсиновий", "сік яблучний"]
]

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

    # Enable keyhandling by curses
    stdscr.keypad(True)

    # Set waiting time for "stdscr.getch()" to 100ms
    # So "key = stdscr.getch()" wont stop program like input(), but wil wait for 100ms
    # stdscr.timeout(500)

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
    typed_food = [[], [], [], []]
    dishes_dx = [0 for _ in range(len(typed_food))]
    cursor_position = (0, 0)
    selected_dishes = []

    if testing_mode:
        typed_food = TESTING_FOOD_DATA
    else:
        raise NotImplementedError()
    typed_food = typed_food + [["Купити"]]

    while ui_runs:
        
        build_ui(screen_matrix, typed_food,
                cursor_position, selected_dishes,
                dishes_dx
                )
        draw_matrix_on_screen(stdscr, screen_matrix)
        # ui_runs = handle_keys_input(stdscr, ui_runs) and handle_terminal_size(stdscr)

        # Handle key input
        key = stdscr.getch()
        # ESC key code - 27
        if key in [ord("q"), ord("Q"), 27]:
            ui_runs = False
        elif key in [ord("d"), ord("D"), curses.KEY_RIGHT]:
            cursor_position = (
                cursor_position[0] + 1,
                cursor_position[1]
                )
        elif key in [ord("a"), ord("A"), curses.KEY_LEFT]:
            cursor_position = (
                max(cursor_position[0] - 1, 0),
                cursor_position[1]
                )
        elif key in [ord("w"), ord("W"), curses.KEY_UP]:
            cursor_position = (
                cursor_position[0],
                max(cursor_position[1] - 1, 0)
                )
        elif key in [ord("s"), ord("S"), curses.KEY_DOWN]:
            cursor_position = (
                cursor_position[0],
                min(cursor_position[1] + 1, len(typed_food) - 1)
                )
        elif key in [curses.KEY_ENTER, ord("\n"), ord(" ")]:
            if cursor_position == [0, 3]:
                ...

            if cursor_position in selected_dishes:
                selected_dishes.remove(cursor_position)
            else:
                selected_dishes.append(cursor_position[:])

        cursor_position = (
                min(cursor_position[0], len(typed_food[cursor_position[1]]) - 1),
                cursor_position[1]
                )
        dishes_dx[cursor_position[1]] = min(
                            max(0, cursor_position[0] - 2),
                            max(len(typed_food[cursor_position[1]]) - DISH_PER_DISPLAY, 0)
                            )



def build_ui(screen_matrix: Matrix, typed_food: tuple[list[str], list[str], list[str]],
             cursor_position: tuple[int, int], selected_dishes: list[tuple[int, int]],
             dishes_dx: list[int]
             ) -> Matrix:
    """ Build UI screen matrix """
    fill_matrix(screen_matrix, " ")
    for row in range(len(typed_food)):
        for column in range(min(DISH_PER_DISPLAY, len(typed_food[row]))):
            frame_symbol = None
            if (column + dishes_dx[row], row) == cursor_position:
                frame_symbol = "█"
            elif (column + dishes_dx[row], row) in selected_dishes:
                frame_symbol = "░"
            dish_frame = create_text_field(
                f"{column + dishes_dx[row]}) {typed_food[row][column + dishes_dx[row]]}",
                DISH_BLOCK_WIDTH, [3, 5, 7, 5, 3][column], frame_symbol
                )
            draw_matrix_on_matrix(dish_frame, screen_matrix, column*(DISH_BLOCK_WIDTH+2), row*8)

def buy_button_pressed(selected_dishes: list[str],
               typed_dishes: list[list[str], list[str], list[str]]
               ) -> list[list[str], list[str], list[str]]:
    ...

if __name__ == "__main__":
    main_loop(testing_mode=True)
