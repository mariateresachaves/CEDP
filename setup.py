#Coastal Engineering Design Package
#Title: Setup
#Author: Francisco Chaves
#Version 0.00
#First Created: 14.12.2015
#Latest Edit: 14.12.2015
#Description: Installs all the required Packages for Coastal_Design

import os

#install tabulate
os.system('sudo apt-get install python-pip')
os.system('sudo pip install tabulate')
os.system('sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose')

#clear screen
os.system('clear')
print "C.E.D.P. successfully installed all the required packages!\n"
