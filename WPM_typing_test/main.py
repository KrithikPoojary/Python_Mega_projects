import curses
from curses import wrapper

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Hello world")
    stdscr.addstr("Hello world")
    stdscr.refresh()
    key = stdscr.getkey()
    print(key)


def main(stdscr):
    curses.init_pair(1 , curses.COLOR_GREEN , curses.COLOR_BLACK)
    curses.init_pair(2 , curses.COLOR_RED , curses.COLOR_BLACK)
    curses.init_pair(3 , curses.COLOR_WHITE , curses.COLOR_BLACK)


wrapper(main)

