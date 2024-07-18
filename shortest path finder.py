import curses
from curses import wrapper
import queue
import time


def print-maze(maze, stdscr, path=[]):
  BLUE =  curses.color_pair(1)
  RED = curses.color_pair(2)
  
  for i, row in enumerate(maze):
    for j, column in enumerate(row):
      if value == start:
        return i ,j
  return None

def find-path(maze,stdscr):
  start = "0"
  end = "X"
  start_pos = find_start(maze, start)
  
  q = queue.Queue()
  q.put(start_pos, [start_pos])
  visited = set()
  
  while not q.empty():
    current_pos = q.get()
    row,col = current_pos
    
    if maze[row][col] == end:
      return path

def main(stdscr):
  
  curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
  curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BROWN)
  blue_and_black = curses.color_pair(1)
  
  print_maze(maze, stdscr)
  stdscr.clear()
  stdscr.addstr(5, 5, "Hello World!")
  stdscr.refresh()
  stdscr.getch()
  
wrapper(main)