""" UI module with main program loop """

from graph_logic import divide_dishes_by_type 
import curses

UI_WIDTH = 40
UI_HEIGHT = 20

# Food data for testing
TESTING_FOOD_DATA = (
    ["борщ", "гороховий суп"],
    ["картопля фрі", "рис", "каша пшенична з сиром фета", "булгур", "омлет", "вівсяка", "котлета"],
    ["компот", "сік апельсиновий", "сік яблучний"]
    )

def handle_terminal_size(stdscr: curses.window):
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

            # Wait a little bit before rechecking size
            stdscr.getch()
        else:
            break  # Terminal is large enough

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

    return stdscr

def main_loop(testing_mode: bool=False):
    """ Main loop of UI program """
    stdscr = init_curses()

    # Flag that indicate if program should still run
    ui_runs = True
    # Variable to hold food values for each food row
    typed_food = ([], [], [])

    while ui_runs:
        handle_terminal_size(stdscr)
        if testing_mode:
            typed_food = TESTING_FOOD_DATA
        else:
            raise NotImplementedError()
        draw_ui(stdscr, typed_food)
        ui_runs = handle_keys_input(stdscr, ui_runs)

def handle_keys_input(stdscr: curses.window, ui_runs: bool) -> bool:
    """ Handle keys input"""
    key = stdscr.getch()
    # ESC key code - 27
    if key in [ord("q"), ord("Q"), 27]:
        ui_runs = False

    return ui_runs

def draw_ui(stdscr: curses.window, typed_food: tuple[list[str], list[str], list[str]]):
    """ Draw UI """
    height, width = stdscr.getmaxyx()
    stdscr.clear()
    stdscr.addstr(2, 0, f"Current size: {width}x{height}")
    stdscr.addstr(3, 0, ", ".join(typed_food[0]))
    stdscr.addstr(4, 0, ", ".join(typed_food[1]))
    stdscr.addstr(5, 0, ", ".join(typed_food[2]))
    stdscr.refresh()

if __name__ == "__main__":
    main_loop(testing_mode=True)
