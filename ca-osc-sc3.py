import sys
import random
import time
import os
import fcntl
import random
import OSC

# setup OSC client and connecting with supercollider
client = OSC.OSCClient()
client.connect( ( '127.0.0.1', 57110 ) )


WIDTH = int(sys.argv[2])              # How wide is the pattern?

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
rule = int(sys.argv[1])

# This fills in the table...
for i in range(2**NEIGHBORHOOD):
    if ((2**i) & rule) != 0:
        rtab[i] = 1

def dump(r):
    for x in r:
        if x == 1:
            sys.stdout.write('X')
        else:
            sys.stdout.write(' ')
    sys.stdout.write('\n')

# and generates 100 lines...

speed = float(sys.argv[3]) # speed = seconds for example 0.01
numlines = int(sys.argv[4]) # number of "lines" for example 200

for y in range(numlines):
    dump(w)
    for x in range(WIDTH):
        sum = 0
        for d in range(NEIGHBORHOOD):
            sum = sum + (2**d) * w[(x+d+WIDTH - NEIGHBORHOOD/2) % WIDTH]
        nw[x] = rtab[sum]
    w, nw = nw, w
# time control
    time.sleep(speed)
