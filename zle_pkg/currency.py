import os
import re
import sys


class CurrencyToken():

	'''
	def __init__(self):

		print('CurrencyToken() package has been installed')
	'''

	@classmethod
	def dollar(cls, string):
		"""
		This function takes a string input and replaces all instances 
		of dollars signs and trailing numerica values to the '<dollar>'
		tag

		param string
		return string (<dollar>)
		"""
		# Declare re.compile syntax
		monetary_unit = re.compile(r'[$][0-9,.]+', re.IGNORECASE)

		# Use the re.compile regex to subsitute string values
		return_string = monetary_unit.sub(' <dollar> ', string)

		# Return the string in lower case
		return return_string.lower()

	@classmethod
	def euro(cls, string):
		"""
		This function takes a string input and replaces all instances 
		of euro signs and trailing numeric values to the '<euro>'
		tag

		param string
		return string (<euro>)
		"""
		# Declare re.compile syntax
		monetary_unit = re.compile(r'[€][0-9,.]+', re.IGNORECASE)

		# Use the re.compile regex to subsitute string values
		return_string = monetary_unit.sub(' <euro> ', string)

		# Return the string in lower case
		return return_string.lower()
	@classmethod
	def yen(cls, string):
		'''
		This function takes a string input and replaces all instances 
		of yen signs and trailing numerica values to the '<yen>'
		tag

		param string
		return string (<yen>)
		'''
		# Declare re.compile syntax
		monetary_unit = re.compile(r'[¥][0-9,.]+', re.IGNORECASE)

		# Use the re.compile regex to subsitute string values
		return_string = monetary_unit.sub(' <yen> ', string)

		# Return the string in lower case
		return return_string.lower()

	@classmethod
	def pound(cls, string):
		"""
		This function takes a string input and replaces all instances 
		of pound signs and trailing numerica values to the '<pound>'
		tag

		param string
		return string (<pound>)
		"""
		# Declare re.compile syntax
		monetary_unit = re.compile(r'[£][0-9,.]+', re.IGNORECASE)

		# Use the re.compile regex to subsitute string values
		return_string = monetary_unit.sub(' <pound> ', string)

		# Return the string in lower case
		return return_string.lower()

	@classmethod
	def money(cls, string):
		"""
		This function takes a string input and replaces all instances 
		of dollar/pound/yen/euro signs and trailing numerica values to the '<money>'
		tag

		param string
		return string (<money>)
		"""
		# Declare re.compile syntax
		monetary_unit = re.compile(r'[€$¥£][0-9,.]+', re.IGNORECASE)

		# Use the re.compile regex to subsitute string values
		return_string = monetary_unit.sub(' <money> ', string)

		# Return the string in lower case
		return return_string.lower()

if __name__=='__main__':

	'''
	Run this code to make sure the package has been installed

	print('CurrencyToken() package has been installed')
	'''