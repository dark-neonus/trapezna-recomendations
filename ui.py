""" UI module with main program loop """

import graph_logic
import curses

def init_curses() -> curses.window:
    """ Init curses library

    Returns:
        curses.window: object of curses output window
    """
    # Object of curses librart window(canvas)
    # on which all output will be drawn
    stdscr = curses.initscr()
    curses.curs_set(0)

    return stdscr

def main_loop():
    """ Main loop of UI program """
    stdscr = init_curses()

    def handle_keys_input():
        """ Handle keys input"""
        pass

    # Flag that indicate if program should still run
    ui_runs = True

    while ui_runs:
        draw_ui(stdscr)
        handle_keys_input()

def draw_ui(stdscr: curses.window):
    """ Draw UI """
    pass
