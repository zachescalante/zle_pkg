import os
import regex
import numpy as np
import pandas as pd


class StringFormatting():

	def __init__(self):

		print('StringFormatting() package has been installed')

	def lower_case(word):
		return word.lower()

if __name__=='__main__':
	print(StringFormatting.lower_case('ABCD'))
