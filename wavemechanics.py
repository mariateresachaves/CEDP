#Coastal Engineering Design Package
#Title: Wave Mechanics
#Author: Francisco Chaves
#Version 0.00
#First Created: 14.12.2015
#Latest Edit: 17.12.2015
#Description:  Calculates wave mechanics based on Linear Wave Theory

import os
import math
os.system("clear")
print "Wave Mechanics - Linear Wave Theory\n"

#User input request - Water depth!
while True:
	try:
		d = float(raw_input("d:\tWater Depth (m) >> "))
		if d<0: 
			raise ValueError
		break
	except ValueError:
		print "\n>Please provide a valid input!"
		
#User input request - Wave Period!
while True:
	try:
		T = float(raw_input("T:\tWave Period >> "))
		if T<0:
			raise ValueError
		break
	except ValueError:
		print "\n>Please provide a valid input!" 

# Output Header Print:
print ("\n"+20*"="+"OUTPUT"+20*"=")

# Calculate wave length
def wavelength(T,d):
	g = 9.81 # Set gravitational acceleration
	L0 = g*pow(T,2)/(2*math.pi) #deep water wave length, starting point for iteration
	L = 0 #initialize L
	while abs(L-L0) > 0.0001:
		if L == 0:
			L = L0
		L = g*pow(T,2)/(2*math.pi)*((2*math.pi*d)/L)
	return L

L = wavelength(T,d)
print "Wave Length > L = %.2fm" % L

# Determine relative water depth

def relativedepth(d,L):
	if d/L < 1/20:
		relativedepth = "Shallow Water"
	elif d/L > 1/2:
		relativedepth = "Deep Water"
	else:
		relativedepth = "Transitional Water"
	return relativedepth

relativedepth = relativedepth(d,L)
print "Relative water depth > %s" % relativedepth

