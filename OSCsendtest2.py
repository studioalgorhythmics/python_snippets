import OSC
import time, sys
import time, random

c = OSC.OSCClient()
c.connect( ( '127.0.0.1', 57110 ))

arraywidth = 10
panval = 1.0
ppan = 1.0
i = 0
j= 0
while (i < arraywidth):
    msg = OSC.OSCMessage()
    msg.setAddress("s_new")
    msg.append("grain")
    msg.append(-1)
    msg.append(0)
    msg.append(1)
    msg.append("freq")
    msg.append(20)
    msg.append("sustain")
    msg.append(0.001)
    msg.append("pan")
    msg.append(0.0)
    c.send(msg)
    time.sleep(0.5)
    i = i + 1
