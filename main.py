import curses
from curses import wrapper


def main(stdscr):
	stdscr.clear()
	stdscr.addstr("Hi U!")
	stdscr.refresh()
	stdscr.getkey()



wrapper(main)