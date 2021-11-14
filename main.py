import time
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
	wpm = 0
	start_time = time.time()
	stdscr.nodelay(True)

	while True:
		time_elapsed = max(time.time() - start_time, 1)
		wpm = round((len(text) / (time_elapsed / 60)) / 5)

		stdscr.clear()
		stdscr.addstr(target_text)
		stdscr.addstr(1, 0, f'WPM : {wpm}')

		for i, char in enumerate(text):
			correct_char = target_text[i]
			color = curses.color_pair(1)
			if char != correct_char:
				color = curses.color_pair(2)
			stdscr.addstr(0, i, char, color)

		stdscr.refresh()

		if "".join(text) == target_text:
			stdscr.nodelay(False)
			break

		try:
			key = stdscr.getkey()
		except:
			continue
		

		if ord(key) == 27:
			break
		if key in ("KEY_BACKSPACE", '\b', "\x7f"):
			if len(text) > 0:
				text.pop()
		elif len(text) < len(target_text):
			text.append(key)




def main(stdscr):
	curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
	
	start_screen(stdscr)
	while True:

		txt_test(stdscr)

		stdscr.addstr(2, 0, "Well Done! Press any key to continue....")
		
		key = stdscr.getkey()
		if ord(key) == 27:
			break

wrapper(main)