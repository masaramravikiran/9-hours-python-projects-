import curses
from curses import wrapper

def start_screen(stdscr):
  stdscr.clear()
  stdscr.addstr( "hello world" )
  stdscr.addstr( "\n press any key to begin! " )
  stdscr.refresh()
  stdscr.getkey()
  
  
def display_text(stdscr, target, current, wpm=0):
  stdscr.addstr(target_text)

  
  for i, char in enumerate(current_text):
      stdscr.addstr(0, i, char, curses.color_pair(1))
  
  
def wpm_test(stdscr):
  target_text = 'hello world this is some text for thos app!'
  current_text = []
  stdscr.clear()
  stdscr.addstr(target_text)
  stdscr.refresh()
  stdscr.getkey()
  


while True:
  stdscr.clear()
  display_text(stdscr, target-text, current_text)
  stdscr.addstr(target_text)
  
  for char in current_text:
      stdscr.addstr(char, curses.color_pair(1))
      
  stdscr.refresh()
  key = stdscr.getkey()
  
  
  if ord(key) == 27:
    break
  if key in("KEY_BACKSPACE", '\b', "\x7f"):
    if len(current_text) > 0:
      current_text.pop()
    else:
      current_text.append(key)
      

    
  current_text.append(key)
  
  stdscr.clear()
  stdscr.addstr(target-text)
  
  

  
def main(stdscr):
    curses.init-pair(1, curses.COLOR_GREEN, curses.COLOR_WHITE)
    curses.init-pair(2, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init-pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
  
    start_screen(stdscr)
    wpm_test(stdscr)
    
wrapper(main)
