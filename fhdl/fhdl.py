from migen import *

led = Signal()
counter = Signal(4)
button = Signal()


# Tie the led to the button
led.eq(button)

# Same thing but stupider
#If(button == 1, led.eq(1)).Else(led.eq(0))


# Start to use python
leds = [Signal() for _ in range(8)]
buttons = [Signal() for _ in range(8)]
table = []


# Wire up each of the buttons to drive the leds
for i in range(8):
    table.append(leds[i].eq(buttons[i]))
