#Python Script for Temperature Sensing Project using Raspberry Pi

tfile = open("/sys/bus/w1/devices/28-031572f527ff/w1_slave")
text = tfile.read()

# Close the file now that the text has been read. 
tfile.close() 

# Split	 the text with new lines (\n) and select the second line. 
#secondline = text.split("\n")[1] 
#print(secondline)

# Split the line into words, referring to the spaces, and select the 10th word (counting from 0). 
#temperaturedata = secondline.split(" ")[9] 
#print(temperaturedata)

#temperaturedata = text.split("\n")[1].split(" ")[9]
#temperaturedata = text.split() #.split() by default split string by whitespace
#print(temperaturedata)

temperaturedata = text.split()[-1] #[-1] = last array index, [-2] = second index counted from the last
#print(temperaturedata)

# The first two characters are "t=", so get rid of those and convert the temperature from a string to a number. 
#temperature = float(temperaturedata[2:]) 

# Put the decimal point in the right place and display it. 
#temperature = temperature / 1000 
print("Current Room Temperature is", float(temperaturedata[2:])/1000 , "Celcius")




