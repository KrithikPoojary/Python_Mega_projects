import curses
from curses import wrapper

def start_screen(stdscr):    #Standard screen
    stdscr.clear()
    stdscr.addstr("Welcome to speed typing test!")
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh()
    stdscr.getkey()
    
def display_test(stdscr , target, current , wpm=0):
    stdscr.addstr(Target_test)
    for  i , char in  enumerate(current_test):
        stdscr.addstr(char , curses.color_pair(1))




def wpm_work(stdscr):
    Target_test = "Hello world we are testing our logic.."
    current_test = []
    

    while True:
        stdscr.clear()   #Must needed because it might loop the char again and again....

        stdscr.refresh()
        key = stdscr.getkey()

        if ord(key) == 27:  #This number is our keyboard number each and every key has that unique number
            break

        if key in ("KEY_BACKSPACE" , "\b" , "\x7f"):  #This is basically our 'backspace' key value in our OS
            if len(current_test) > 0:
                current_test.pop()
        else:
            current_test.append(key)


def main(stdscr):
    curses.init_pair(1 , curses.COLOR_GREEN , curses.COLOR_BLACK)
    curses.init_pair(2 , curses.COLOR_RED , curses.COLOR_BLACK)
    curses.init_pair(3 , curses.COLOR_WHITE , curses.COLOR_BLACK)
    # key = stdscr.getkey()
    # print(key)
    start_screen(stdscr)
    wpm_work(stdscr)


wrapper(main)

