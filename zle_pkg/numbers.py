import os
import re


class NumberToken():

	def __init__(self):

		print('NumberToken() package has been installed')

	def number(self, string):
		'''
		This function takes a string input and replaces all instances 
		of dollars signs and trailing numerica values to the '<dollar>'
		tag

		param string
		return string
		'''
		# Declare re.compile syntax
		monetary_unit = re.compile(r'[0-9,.]+', re.IGNORECASE)

		# Use the re.compile regex to subsitute string values
		return_string = monetary_unit.sub(' <number> ', string)

		# Return the string in lower case
		return return_string.lower()

if __name__=='__main__':
	main()