import curses
from curses import wrapper

def start_screen(stdscr):    #Standard screen
    stdscr.clear()
    stdscr.addstr("Welcome to speed typing test!")
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh()
    stdscr.getkey()
    

def wpm_work(stdscr):
    Target_test = "Hello world we are testing our logic.."
    current_test = []
    

    while True:
        key = stdscr.getkey()
        current_test.append(key)

        stdscr.clear()
        stdscr.addstr(Target_test)
        for char in  current_test:
            stdscr.addstr(char , curses.color_pair(1))
        stdscr.refresh()

def main(stdscr):
    curses.init_pair(1 , curses.COLOR_GREEN , curses.COLOR_BLACK)
    curses.init_pair(2 , curses.COLOR_RED , curses.COLOR_BLACK)
    curses.init_pair(3 , curses.COLOR_WHITE , curses.COLOR_BLACK)
    # key = stdscr.getkey()
    # print(key)
    start_screen(stdscr)
    wpm_work(stdscr)


wrapper(main)

