import os
import re
import sys


class CurrencyToken():

	def __init__(self):

		print('CurrencyToken() package has been installed')

	def dollar(self, string):
		'''
		This function takes a string input and replaces all instances 
		of dollars signs and trailing numerica values to the '<dollar>'
		tag

		param string
		return string
		'''
		# Declare re.compile syntax
		monetary_unit = re.compile(r'[$][0-9,.]+', re.IGNORECASE)

		# Use the re.compile regex to subsitute string values
		return_string = monetary_unit.sub(' <dollar> ', string)

		# Return the string in lower case
		return return_string.lower()

	def euro(self, string):
		'''
		This function takes a string input and replaces all instances 
		of dollars signs and trailing numerica values to the '<euro>'
		tag

		param string
		return string
		'''
		# Declare re.compile syntax
		monetary_unit = re.compile(r'[€][0-9,.]+', re.IGNORECASE)

		# Use the re.compile regex to subsitute string values
		return_string = monetary_unit.sub(' <euro> ', string)

		# Return the string in lower case
		return return_string.lower()

	def yen(self, string):
		'''
		This function takes a string input and replaces all instances 
		of dollars signs and trailing numerica values to the '<yen>'
		tag

		param string
		return string
		'''
		# Declare re.compile syntax
		monetary_unit = re.compile(r'[¥][0-9,.]+', re.IGNORECASE)

		# Use the re.compile regex to subsitute string values
		return_string = monetary_unit.sub(' <yen> ', string)

		# Return the string in lower case
		return return_string.lower()

	def pound(self, string):
		'''
		This function takes a string input and replaces all instances 
		of dollars signs and trailing numerica values to the '<pound>'
		tag

		param string
		return string
		'''
		# Declare re.compile syntax
		monetary_unit = re.compile(r'[£][0-9,.]+', re.IGNORECASE)

		# Use the re.compile regex to subsitute string values
		return_string = monetary_unit.sub(' <pound> ', string)

		# Return the string in lower case
		return return_string.lower()

	def money(self, string):
		'''
		This function takes a string input and replaces all instances 
		of dollars signs and trailing numerica values to the '<money>'
		tag

		param string
		return string
		'''
		# Declare re.compile syntax
		monetary_unit = re.compile(r'[€$¥£][0-9,.]+', re.IGNORECASE)

		# Use the re.compile regex to subsitute string values
		return_string = monetary_unit.sub(' <money> ', string)

		# Return the string in lower case
		return return_string.lower()

if __name__=='__main__':
	print('CurrencyToken() package has been run')