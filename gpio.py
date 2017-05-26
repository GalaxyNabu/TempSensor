#Configure GPIO

import RPi.GPIO as GPIO
import sys

#use the pin number on the breadboard
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)
#Setup which GPIO channel to use
GPIO.setup(26,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)


while True: 

	Ans = input("LED On / Off or Exit? ")

	if Ans[1] == "n" or Ans[1] == "N": 
		Ans = "On"
	elif Ans[1] == "f" or Ans[1] == "F":
		 Ans = "Off"
	else:
		GPIO.output(26,GPIO.LOW)
		GPIO.output(16,GPIO.LOW)
		sys.exit("Fun! Thank You Come Again")

	if Ans == "On":
		#Turn on GPIO output and light LED
		GPIO.output(26,GPIO.HIGH)
		GPIO.output(16,GPIO.HIGH)
 
	#Turn on GPIO output and light LED
	else:
 		GPIO.output(26,GPIO.LOW)
 		GPIO.output(16,GPIO.LOW)

