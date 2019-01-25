import os
import re


class NumberToken():

	'''
	def __init__(self):

		print('NumberToken() package has been installed')
	'''

	@classmethod
	def number(cls, string):
		'''
		This function takes a string input and replaces all instances 
		of numeric data and trailing numeric values to the '<numeric>'
		tag

		param string
		return string (<numeric>)
		'''
		# Declare re.compile syntax
		monetary_unit = re.compile(r'[0-9,.]+', re.IGNORECASE)

		# Use the re.compile regex to subsitute string values
		return_string = monetary_unit.sub(' <number> ', string)

		# Return the string in lower case
		return return_string.lower()

if __name__=='__main__':

	'''
	Run this to make sure the NumberToken() package has been installed

	print('NumberToken() package has been installed')
	'''