#!/usr/bin/python3


import pandas as pd
import numpy as np
#only neededif you want to use xslx or xls files, also will need to add sheet name
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import json

def main():


	df = pd.read_csv('filename.csv')
	data = df.to_json('filename.json')
	

if __name__ == '__main__':
	main()

