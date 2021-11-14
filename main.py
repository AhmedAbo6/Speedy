import curses
from curses import wrapper

best = 0 

def start_screen(stdscr):
	stdscr.clear()
	stdscr.addstr("Welcome! I'am Speedy. The speed Typing Test!")
	stdscr.addstr(f"\nYour Personal Best is {best}")
	stdscr.addstr("\nPress and key to begin!")
	stdscr.refresh()
	stdscr.getkey()


def txt_test(stdscr):
	target_text = 'JacksEpicYoutubeChannelFullofFunTimesAndfunHiRickX'
	text = []
	stdscr.clear()
	stdscr.addstr(target_text)
	stdscr.refresh()
	stdscr.getkey()

	while True:
		key = stdscr.getkey()

		if ord(key) == 27:
			break
		


def main(stdscr):
	curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
	
	start_screen(stdscr)
	txt_test(stdscr)

wrapper(main)