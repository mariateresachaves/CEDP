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

#Change current folder to /scripts
os.chdir("scripts")

#Runs setup.py which will check the need for package installation or updates
os.system("python setup.py")

#Launch main menu
os.system("python mainmenu.py")


