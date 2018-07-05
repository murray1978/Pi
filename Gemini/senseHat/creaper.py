from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

g = (0,255,0)
b = (0,0,0)

creaper_pixels = [
	g,g,g,g,g,g,g,g,
	g,g,g,g,g,g,g,g,
	g,b,b,g,g,b,b,g,
	g,b,b,g,g,b,b,g,
	g,g,g,b,b,g,g,g,
	g,g,b,b,b,b,g,g,
	g,g,b,b,b,b,g,g,
	g,g,b,g,g,b,g,g
]

#sense.set_pixels(creaper_pixels)

#while True:
#	sleep(1)
#	sense.flip_h()

sense.clear()
