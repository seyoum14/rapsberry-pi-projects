# led_hello.py - light a LED using Raspberry Pi GPIO
# Yophtahe Seyoum - January 14, 2016

import time
import os 

def writeFile(filename, contents):
	with open(filename, 'w') as f:
		f.write(contents)


# main

print "Blinking LED on GPIO 27 once..." 

if not os.path.isfile("/sys/class/gpio/gpio27/direction"):
	wrtieFile("/sys/class/gpio/export", "27")

time.sleep(0.1)
writeFile("/sys/class/gpio/gpio27/direction", "out")

writeFile("/sys/class/gpio/gpio27/value", "1")
time.sleep(2) #secs
writeFile("/sys/class/gpio/gpio27/value", "0")

