#Python Script for Temperature Sensing Project using Raspberry Pi

import RPi.GPIO as GPIO
import sys
import time

#Setup numbering mode to use for channel
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#Setup which GPIO channel to use
GPIO.setup(26,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)

Timestep = input("Time Stamp size in seconds? ")
CapIter = input("How many captures? ")
tfile = open("/sys/bus/w1/devices/28-031572f527ff/w1_slave")

for i in range(int(CapIter)):

	tfile = open("/sys/bus/w1/devices/28-031572f527ff/w1_slave")
	text = tfile.read()

	# Close the file now that the text has been read. 
	tfile.close() 

	temperaturedata = text.split()[-1] #[-1] = last array index, [-2] = second index counted from the last
	print("Current Room Temperature is", float(temperaturedata[2:])/1000 , "Celcius")
	#print(i)
	time.sleep(float(Timestep))

tfile.close() 


