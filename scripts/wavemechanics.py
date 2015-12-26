#Coastal Engineering Design Package
#Title: Wave Mechanics
#Author: Francisco Chaves
#Version 0.00
#First Created: 14.12.2015
#Latest Edit: 17.12.2015
#Description:  Calculates wave mechanics based on Linear Wave Theory

#
import os
import math
os.system("clear")
print "Wave Mechanics - Linear Wave Theory\n"

##WAVE PERIOD
#Run waveperiod.py which will request user input for wave period
#and calcuate Peak, Mean and Spectral wave periods.
#os.system("python waveperiod.py") The problem with this is that it doesn't pass the variables between both scripts
from waveperiod import Tp, Tm, Tm10

##WATER DEPTH
#User input request - Water depth!
while True:
	try:
		d = float(raw_input("d  (m) Water Depth (m)   -> "))
		if d<0: 
			raise ValueError
		break
	except ValueError:
		print "\n>Please provide a valid input!"

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

# Determine relative water depth

def relativedepth(d,L):
	if d/L < 1/20:
		relativedepth = "Shallow Water"
	elif d/L > 1/2:
		relativedepth = "Deep Water"
	else:
		relativedepth = "Transitional Water"
	return relativedepth

# Output Header Print:
print ("\n"+20*"="+"OUTPUT"+20*"="+"\n")

# Outputs wave length and relative water depth
L = wavelength(Tp,d)
print "Wave Length                -> L = %.2fm" % L
relativedepth = relativedepth(d,L)
print "Relative Water Depth       -> %s" % relativedepth

#Outputs wave periods
print "Tp Peak Wave Period        -> %.2fs" % Tp
print "Tm Mean Wave Period        -> %.2fs" % Tm
print "Tm-1,0 Sectral Wave Period -> %.2fs" % Tm10
