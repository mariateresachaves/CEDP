#Coastal Engineering Design Package
#Title: Wave Mechanics
#Author: Francisco Chaves
#Version 0.00
#First Created: 21.12.2015
#Latest Edit: 21.12.2015
#Description:  

import datetime

# By default, MyTime is set to today's date, but it can be set to any other date.
class MyTime():
	def __init__(self):
		self.year = datetime.date.today().year
		self.month = datetime.date.today().month
		self.day = datetime.date.today().day
		self.days = self.day + self.month*31+self.year*365

	#sets MyTime to a given date.
	def setDate(self,y,m,d):
		self.year = y
		self.month = m
		self.day = d

	#calculates the difference between a date and MyTime's current date
	def diffDate(self,d8):
		difDay = self.days - d8.days
		return difDay

dateNow = MyTime()
d8 = MyTime()








