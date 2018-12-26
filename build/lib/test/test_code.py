from zle_pkg.date import DateToken
from zle_pkg.numbers import NumberToken
from zle_pkg.currency import CurrencyToken
from zle_pkg.tokenize import Tokenize


class TestCode():

	def __init__(self):

		self.dt = DateToken()
		self.nmbr = NumberToken()
		self.fx = CurrencyToken()
		self.tkn = Tokenize()

if __name__=='__main__':

	tc = TestCode()

	# Test the DateToken() class:
	string_1 = 'On July 4th, 1776 we celebrate Independance Day'
	string_2 = 'On 07/04/1776 we celebrate Independance Day'
	string_3 = 'On 7-04-1776 we celebrate Independance Day'
	print("Input: ", string_1)
	print("Output: ", tc.dt.us_day(string_1))

	print("Input: ", string_2)
	print("Output: ", tc.dt.us_month(string_1))

	print("Input: ", string_3)
	print("Output: ", tc.dt.us_year(string_1))
'''
	# Two euro strings, one with periods and one with commas
	string_2 = '€12345.76 see if this works €123,456,789'
	print("Input: ", string_2)
	print("Output: ", nlpf.euro(string_2))

	# Two yen strings, one with periods and one with commas
	string_3 = 'Common stock, ¥0.60 par value, 3,000,000 shares authorized'
	print("Input: ", string_3)
	print("Output: ", nlpf.yen(string_3))

	# Testing British Pound money strings
	string_4 = 'Common stock, £0.60.00,00 par value, 3,000,000 shares authorized'
	print("Input: ", string_4)
	print("Output: ", nlpf.pound(string_4))

	# Testing the money function
	string_5 = 'dollar $123,456,789.23 pound £123,456,789 yen ¥123,456,789.98 euro €123,456,789.54'
	print("Input: ", string_5)
	print("Output: ", nlpf.money(string_5))
'''
