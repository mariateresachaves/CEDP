#Coastal Engineering Design Package
#Title: Setup
#Author: Francisco Chaves
#Version 0.00
#First Created: 14.12.2015
#Latest Edit: 14.12.2015
#Description: Installs all the required Packages for Coastal_Design

import os
import datetime
import dateclass

today = dateclass.MyTime()

#acess installation registration file and read the date it was last update. If the file doesn't exists create one and run the full setup


#Checks if installation of packages is required.
while True:
	try:
		install_reg=open("install_reg.py","r+")
		install_data= int(install_reg.read())
		fileExists = True
		if abs(install_data - today.days) > 30:
			raise IOError
		choice = False
		break
	except IOError:
		fileexists = False
		print"CEDP.py installation updates are required. Installation might take several minutes. Do you want to continue? [y/n]"
		while True:
			try:
				choice = raw_input("-> ").upper()
				if choice == "Y" or "N":
					break
				else:
					raise ValueError 
			except ValueError:
				print "Please provide a valid answer!"
		break

if choice == "Y":
	#install tabulate
	os.system('sudo apt-get install python-pip')
	#install pip
	os.system('sudo pip install tabulate')
	#install packages
	os.system('sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose')
	#generate/overwrite text file recording installation date
	install_reg = open("install_reg.py","w")
	install_reg.write(str("%d"%today.days))
	#clear screen
	os.system('clear')
	print "C.E.D.P. successfully installed all the required packages!\n"

