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
	print("Output: ", tc.dt.us_month(string_2))

	print("Input: ", string_3)
	print("Output: ", tc.dt.us_year(string_3))

	print("Input: ", string_3)
	print("Output: ", tc.dt.us_date(string_3))

	# Test the CurrencyToken() class:
	string_4 = 'the price of a Big Mac was $3.57 in the United States '
	string_5 = 'the price of a Big Mac was £2.29 in the United Kingdom'
	string_6 = 'the price of a Big Mac was ¥670.00 in the Japan'
	string_7 = 'the price of a Big Mac was €7,00 in the Germany'

	print("Input: ", string_4)
	print("Output: ", tc.fx.dollar(string_4))

	print("Input: ", string_5)
	print("Output: ", tc.fx.pound(string_5))

	print("Input: ", string_6)
	print("Output: ", tc.fx.yen(string_6))

	print("Input: ", string_7)
	print("Output: ", tc.fx.euro(string_7))

	# Test the NumberToken() class:
	string_8 = 'The number 12.345,789.01 is my lucky number'

	print("Input: ", string_8)
	print("Output: ", tc.nmbr.number(string_8))

	# Test the Tokenize() class
	string_9 = 'On April 15th, 1985 Michael Jordan paid $2.12 for each of his 10 big macs'

	print("Input: ", string_9)
	print("Output: ", tc.tkn.tokenize(string_9))


