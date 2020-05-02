#!/usr/bin/python3


import pandas as pd
import numpy as np
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import json

name = input("give me the name of the file: ")

def main():


	df = pd.read_csv(name + '.csv')
	data = df.to_json(name + '.json')
	

if __name__ == '__main__':
	main()

