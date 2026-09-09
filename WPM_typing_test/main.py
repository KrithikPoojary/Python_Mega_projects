import curses
from curses import wrapper

def main(stdscr):
    curses.init_pair(1 , curses.COLOR_RED , curses.COLOR_WHITEl)
    stdscr.clear()
    stdscr.addstr("Hello world")
    stdscr.refresh()
    stdscr.getkey()

wrapper(main)

