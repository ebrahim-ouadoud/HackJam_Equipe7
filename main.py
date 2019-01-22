# import both libs
import neopixel
from machine import Pin

# define which pin to use and a neopixel object
pin0 = Pin(0)
np = neopixel.NeoPixel(pin0)

# [0] for the first LED, [1] for the 2nd etc
# value in RGB from 0 to 255
np[0] = (255, 0, 0)
# write the modification to switch on the first led in bright red
np.write()

# 2nd exemple with different leds with different values :

BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)

COL_LIST = [BLUE, GREEN, PURPLE, RED]

for i in range(0, 3, 1):
    np[i] = COL_LIST[i]
np.write()
