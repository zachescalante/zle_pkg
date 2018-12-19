import os
import re
from date import DateToken
from numbers import NumberToken
from currency import CurrencyToken


class Tokenize():

	def __init__(self):

		print('Tokenize() package has been installed')

	def tokenize(self, string):
		'''
		This function takes a string input and executes three functions:

		1. CurrencyToken.money(): if we see any currency symbols, then we convert
		   those numbers following that symbol to the <currency> token
		2. DateToken.us_date(): if we see any dates (numbers/strings with date
		   naming convension) then we convert these to the <date> token
		3. NumberToken.number(): convert all remaining numbers to the <number> token  

		param string
		return string
		'''

		# 1. exchange all currency symbols for the <money> token
		currency_symbols = re.compile(r'[€$¥£]')
		if currency_symbols.findall(string):
			string = CurrencyToken().money(string)

		# 2. exchange all date values for the <date> token
		string = DateToken().us_date(string)

		#3. exchange all number values for the <number> token
		string = NumberToken().number(string)

		return string

if __name__=='__main__':

	print(Tokenize().tokenize("let's try this $123,456.789 currency with this January 1st, 2014 date and these 12,34,5.8.0 numbers"))