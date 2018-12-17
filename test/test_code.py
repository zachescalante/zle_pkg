import os
import re
import sys
import numpy as np
import pandas as pd


class NLPFormatting():

	def __init__(self):

		print('StringFormatting() package has been installed')

	def dollar(self, string):
		'''
		This function takes a string input and replaces all instances 
		of dollars signs and trailing numerica values to the '<dollar>'
		tag

		param string
		return string
		'''
		# Declare re.compile syntax
		monetary_unit = re.compile(r'[$][(0-9).,]+', re.IGNORECASE)

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
		monetary_unit = re.compile(r'[€][(0-9).,]+', re.IGNORECASE)

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
		monetary_unit = re.compile(r'[¥][(0-9).,]+', re.IGNORECASE)

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
		monetary_unit = re.compile(r'[¥][(0-9).,]+', re.IGNORECASE)

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
		monetary_unit = re.compile(r'[€$¥£][(0-9).,]+', re.IGNORECASE)

		# Use the re.compile regex to subsitute string values
		return_string = monetary_unit.sub(' <money> ', string)

		# Return the string in lower case
		return return_string.lower()

if __name__=='__main__':

	nlpf = NLPFormatting()

	# Two money strings, one with commas and one without
	string_1 = '$12345 see if this works $123,456,789'
	print("Input: ", string_1)
	print("Output: ", nlpf.dollar(string_1))

	# Two euro strings, one with periods and one with commas
	string_2 = '€12345.76 see if this works €123,456,789'
	print("Input: ", string_2)
	print("Output: ", nlpf.euro(string_2))

	# Two yen strings, one with periods and one with commas
	string_3 = 'Common stock, ¥0.60 par value, 3,000,000 shares authorized'
	print("Input: ", string_3)
	print("Output: ", nlpf.yen(string_3))

	# Testing British Pound money strings
	string_4 = 'Common stock, £0.60 par value, 3,000,000 shares authorized'
	print("Input: ", string_4)
	print("Output: ", nlpf.pound(string_4))

	# Testing the money function
	string_5 = 'dollar $123,456,789.23 pound £123,456,789 yen ¥123,456,789.98 euro €123,456,789.54'
	print("Input: ", string_5)
	print("Output: ", nlpf.money(string_5))
