import sys
import random
import time
import pyfirmata
from pyfirmata import ArduinoMega

# Arduino-Pyfirmata CODE

# Adjust that the port match your system, see samples below:
# On Linux: /dev/tty.usbserial-A6008rIF, /dev/ttyACM0,
# On Windows: \\.\COM1, \\.\COM2
PORT = '/dev/tty.usbmodem1451'

# Creates a new board
board = pyfirmata.ArduinoMega(PORT)


WIDTH=18               # How wide is the pattern?

w = WIDTH * [0]         # create the current generation
nw = WIDTH * [0]        # and the next generation
w[WIDTH/2] = 1          # populate with a single one

# or alternatively, you can populate it with a random
# initial configuration.  If you want to start with
# just a single one, comment the next two lines out.

# for i in range(WIDTH):
#      w[i] = random.randint(0, 1)

# How wide is the neighborhood of cells that are
# examined?  The traditional Wolfram 1D cellular
# automata uses a neighborhood of 3...

NEIGHBORHOOD=3

# rtab is space for the rule table.  It maps all
# numbers from [0, 2**NEIGHBORHOOD) to either a 0 or 1.
rtab = (2**NEIGHBORHOOD) * [0]

# The "rule" is a number which is used to populate
# rtab.  The number is in the range [0, 2**(2**NEIGHBORHOOD))
# Many rules generate uninteresting patterns, but some
# like 30 generate interesting, aperiodic patterns.

# input from commandline as simple arguments like: ca-firmata.py 30
# for rule 30
rule = int(sys.argv[1])

# This fills in the table...
for i in range(2**NEIGHBORHOOD):
    if ((2**i) & rule) != 0:
        rtab[i] = 1

def dump(r):
    pin = 18
    for x in r:
        if x == 1:
            sys.stdout.write('X')
        else:
            sys.stdout.write(' ')
        board.digital[pin].write(1 if x else 0)
	pin += 1
    sys.stdout.write('\n')

# and generates 100 lines...

for y in range(int(sys.argv[2])):
    dump(w)
    for x in range(WIDTH):
        sum = 0
        for d in range(NEIGHBORHOOD):
            sum = sum + (2**d) * w[(x+d+WIDTH - NEIGHBORHOOD/2) % WIDTH]
        nw[x] = rtab[sum]
    w, nw = nw, w
# time control
    time.sleep(float(sys.argv[3]))
