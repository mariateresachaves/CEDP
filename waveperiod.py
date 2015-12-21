#Coastal Engineering Design Package
#Title: Wave Mechanics
#Author: Francisco Chaves
#Version 0.00
#First Created: 21.12.2015
#Latest Edit: 21.12.2015
#Description:  Calculates Tp, Tm and Tm-1,0, based on input wave period

import os
import math
from tabulate import tabulate
#Ask user which wave period he intends to input.

waveperiodtype = [
["1","Tp (s) Peak Wave Period"],
["2","Tm (s) Mean Wave Period"],
["3","Tm-1,0 (s) Mean Energy Wave Period"]
]

print "\n",tabulate(waveperiodtype,headers=["No.","Input Wave Period"]),"\n"

while True:
	try:
		selection = int(raw_input("Please select input wave period -> "))
		if selection>len(waveperiodtype) or selection<0:
			raise ValueError
		break
	except ValueError:
		print "Please provide a valid input!"

Tselected = raw_input("\n%s" % waveperiodtype[selection-1][1])

#if selection == 1:
#	Tm = Tp

