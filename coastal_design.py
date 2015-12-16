#Coastal Engineering Design Package
#Title: Main
#Author: Francisco Chaves
#Version 0.00
#First Created: 14.12.2015
#Latest Edit: 14.12.2015
#Description: Main script of the Coastal Design Package. Will be used as the main menu of the program and will contain a
#			  list of all available packages.

import os

#Clear memory
os.system('clear')

#Setup - Checks if package installation is required
installation = ''
while (installation != 'Y' and installation != 'N'):
	installation = raw_input('First time running python? Y/N \n>')
	installation = installation.upper()
	if installation != 'Y' and installation != 'N':
		print "Please provide a valid selection"
	else:
		pass

if installation == "Y":
	print "Installation of the necessary packages for C.E.D.P. could take several minutes. Procceed?\n [Enter] to Procceed or [Ctrl+C] to quit"
	raw_input()
	os.system('python setup.py')
else:
	pass

#Import necessary packages
from tabulate import tabulate
#Display available C.E.D.P. 

contents=[['1','Wave Mechanics','Under Development','WAM'], ['2','Rubble Mound Structures','Under Development', 'RBS'],['2.1','\tWave Overtopping','Under Development','WOG'],['2.2','\tArmour Rock (Van der Meer)','Under Development','ARK'],['2.3','\tToe Stability (Van der Meer)','Under Development','TSY'],['2.4','\tRear Side Stability','Under Development','RSS']]

print "\n",tabulate(contents, headers=['No','Name', 'Availability', 'Code']),"\n"

#Package selection and launch
pselect=raw_input("Select a Package:\n>")

#DEVELOP=> launch the correct .py file based on user selection.


