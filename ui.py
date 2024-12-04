""" UI module with main program loop """

import curses

from ui_tools.matrix import (Matrix, create_matrix, fill_matrix,
                             draw_matrix_on_screen, draw_matrix_on_matrix)
from ui_tools.ui_toolbox import create_text_field, add_frame_to_matrix
import graph_logic
from graph_visualization_png import organise_graph, generate_graph_png



DISH_PER_DISPLAY = 5
DISH_BLOCK_WIDTH = 16

UI_WIDTH = (DISH_BLOCK_WIDTH + 2) * DISH_PER_DISPLAY + 2
UI_HEIGHT = 30

GRAPH_FILE = "graph.json"

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
    typed_dishes = [[], [], [], []]
    dishes_dx = [0 for _ in range(len(typed_dishes))]
    cursor_position = (0, 0)
    selected_dishes = []

    typed_dishes = get_sorted_dishes(selected_dishes, typed_dishes, testing_mode)

    while ui_runs:
        build_ui(screen_matrix, typed_dishes,
                cursor_position, selected_dishes,
                dishes_dx
                )
        draw_matrix_on_screen(stdscr, screen_matrix)

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
                min(cursor_position[1] + 1, len(typed_dishes) - 1)
                )
        elif key in [curses.KEY_ENTER, ord("\n"), ord(" ")]:
            if cursor_position == (0, 3): # Buy button
                typed_dishes = get_sorted_dishes(selected_dishes,
                                                 typed_dishes,
                                                 testing_mode)
                selected_dishes = []
                cursor_position = (0, 0)
            elif cursor_position == (1, 3): # Visualization button
                show_visualization()
            elif cursor_position == (2, 3): # Clear graph button
                clear_graph()
            elif cursor_position in selected_dishes:
                selected_dishes.remove(cursor_position)
            else:
                selected_dishes.append(cursor_position[:])

        cursor_position = (
                min(cursor_position[0], len(typed_dishes[cursor_position[1]]) - 1),
                cursor_position[1]
                )
        dishes_dx[cursor_position[1]] = min(
                            max(0, cursor_position[0] - 2),
                            max(len(typed_dishes[cursor_position[1]]) - DISH_PER_DISPLAY, 0)
                            )



def build_ui(screen_matrix: Matrix, typed_food: tuple[list[str], list[str], list[str]],
             cursor_position: tuple[int, int], selected_dishes: list[tuple[int, int]],
             dishes_dx: list[int]
             ) -> Matrix:
    """ Build UI screen matrix """
    fill_matrix(screen_matrix, " ")
    for row, typed_food_row in enumerate(typed_food):
        for column in range(min(DISH_PER_DISPLAY, len(typed_food_row))):
            frame_symbol = None
            if (column + dishes_dx[row], row) == cursor_position:
                frame_symbol = "█"
            elif (column + dishes_dx[row], row) in selected_dishes:
                frame_symbol = "░"
            elif row == 3:
                frame_symbol = " "
            if row == 3:
                dish_frame = create_text_field(
                    f"{typed_food_row[column + dishes_dx[row]]}",
                    DISH_BLOCK_WIDTH, 3, frame_symbol
                    )
            else:
                dish_frame = create_text_field(
                    f"{column + dishes_dx[row] + 1}) {typed_food_row[column + dishes_dx[row]]}",
                    DISH_BLOCK_WIDTH, [3, 5, 7, 5, 3][column], frame_symbol
                    )
            draw_matrix_on_matrix(dish_frame, screen_matrix,
                                column*(DISH_BLOCK_WIDTH+2) + 2, row*8 +2)
    add_frame_to_matrix(screen_matrix)

def get_sorted_dishes(selected_dishes: list[str],
               typed_dishes: list[list[str], list[str], list[str]],
               testing_mode: bool = False
               ) -> list[list[str], list[str], list[str]]:
    """ Return list of sorted dishes with buttons """
    # Buttons row
    buttons_row = [["Купити", "Візуалізація", "! Обнули !"]]

    # Case when nothing was selected dont change anything
    if testing_mode:
        return TESTING_FOOD_DATA + buttons_row

    graph = graph_logic.load_graph(GRAPH_FILE)

    if len(selected_dishes) != 0:

        # Creating names of selected dishes from indexes and sorted list
        selected_dishes_names = []
        for i, dish_type_list in enumerate(typed_dishes):
            for j, dish_name in enumerate(dish_type_list):
                if (j, i) in selected_dishes:
                    selected_dishes_names.append(dish_name)

        selected_products = graph_logic.dishes_to_products(selected_dishes_names)
        graph_logic.add_session(graph, selected_products)
        graph_logic.save_graph(graph, GRAPH_FILE)

    # PageRank here
    dishes_power = graph_logic.calculate_dishes_power(
        graph_logic.calculate_products_power(graph)
    )
    new_typed_dishes = graph_logic.divide_dishes_by_type(
        graph_logic.sort_dishes(dishes_power)
    )

    return list(new_typed_dishes) + buttons_row

def show_visualization():
    """ Show visualization of current graph
    by calling visualization part of program
    """
    generate_graph_png(organise_graph(graph_logic.load_graph(GRAPH_FILE)))

def clear_graph():
    """ Clear graph with preferences
    """
    # Write mode create/overwrite file
    with open("graph.json", "w", encoding="utf-8") as file:
        # Write empty dictionary to `graph.json`
        file.write("{\n}")

if __name__ == "__main__":
    main_loop(testing_mode=True)
