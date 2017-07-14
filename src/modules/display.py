# ---
# display.py
# Functions that aids printing text onto the screen.
# ---

import sys

black = 30
red = 31
green = 32
yellow = 33
blue = 34
pink = 35
cyan = 36
white = 37

normal = 0
bright = 1
dim = 2
italic = 3
underline = 4

def display(string, color = white, background = black, type = 0, end = "\r\n"):
    sys.stdout.write( "\x1b[" + str(type) + ";" + str(color) + ";" + str(background + 10) + "m" + string + "\x1b[0m" + end )
