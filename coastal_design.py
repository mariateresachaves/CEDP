#Coastal Engineering Design Package
#Title: Main
#Author: Francisco Chaves
#Version 0.00
#First Created: 14.12.2015
#Latest Edit: 14.12.2015
#Description: Main script of the Coastal Design Package. Will be used as the main menu of the program and will contain a
#			  list of all available packages.

import os
from tabulate import tabulate

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

#List of C.E.D.P packages
packagelist=[
["1","wavemechanics.py"],
["2","waveovertopping.py"],
["3","armourrockvandermeer.py"],
["4","toestability.py"],
["5","rearsidestability.py"],
]

#Display available C.E.D.P. 

contents=[
['1','Wave Mechanics','Under Development','WAM',],
['>>>','Rubble Mound Structures','Under Development', 'RBS'],
['2','Wave Overtopping','Under Development','WOG'],
['3','Armour Rock (Van der Meer)','Under Development','ARK'],
['4','Toe Stability (Van der Meer)','Under Development','TSY'],
['5','Rear Side Stability','Under Development','RSS']
]
#Generate a beautiful selection table
print "\n",tabulate(contents, headers=['No','Name', 'Availability', 'Code']),"\n"

#Package selection, error handling and run package.
while True:
	try:
		pselect=int(raw_input("Select a Package No.:\n>"))
		# Reduce selected number by 1 because lists index start as zero (0)
		pselect = pselect -1
		break
	except ValueError:
		print "\nERROR: Please select a valid package number!\n"	

os.system("python %s" % packagelist[pselect][1])