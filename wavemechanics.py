#Coastal Engineering Design Package
#Title: Wave Mechanics
#Author: Francisco Chaves
#Version 0.00
#First Created: 14.12.2015
#Latest Edit: 17.12.2015
#Description:  Calculates wave mechanics based on Linear Wave Theory

import os
os.system("clear")
print "Wave Mechanics - Linear Wave Theory\n"

#User input request - Water depth!
while True:
	try:
		d = float(raw_input("d:\tWater Depth (m) >> "))
		if d<0: 
			raise ValueError
	except ValueError:
		print "\n>Please provide a valid input!"
		
#User input request - Wave Period!
while True:
	try:
		T = float(raw_input("T:\tWave Period >> "))
		if T<0:
			raise ValueError
	except ValueError:
		print "\n>Please provide a valid input!" 

