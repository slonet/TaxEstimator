import csv
import json
from datetime import datetime

_config_data = {}
_grant_data = {}


#TODO: Rename methods to follow naming convention
#TODO: Set methods private / public
#TODO: Change config file to open with argument

"""
Prompts user for the path to a single config file.
A file object is returned or an error is printed to the terminal if the file cannot be opened.
"""
def open_config_file():
	
	print("Enter the relative path to the config file")
	file_path = input("\n> ")
	config_file = None

	try:
		config_file = open(file_path, 'r')

	except:
		print(f"\nCould not open the file with path \"{file_path}\"")

	return config_file


"""
Extracts the grant data from a grant CSV file row after being converted to a list
The date is represented as a datetime object so math can easily be done
"""
def load_grant_csv_row(row):

	grant = {
		"grant_id"       : row[0],
		"cost_basis"     : float(row[3].replace('$','')),
		"vesting_date"   : datetime.strptime(row[5], '%d-%b-%Y'),
		"shares_qty"     : int(row[7].replace(',','')),
		"shares_to_sell" : 0 # default value
	}

	return [grant]


"""
Accepts a file object pointing to a Solium stock stock certificate summary csv
Parses all of the available grants from the file
Returns a list containing the stock grant data
"""
def load_grant_csv(file_obj):

	grants = []

	with file_obj:
		csv_reader = csv.reader(file_obj, delimiter=',')

		for row in csv_reader:
			for item in row:
				if item.count("$"): # found a row with a grant					
					grants += load_grant_csv_row(row)

	return grants

"""
Loads a number of stock certificate summary CSV files and creates a dictionary of the grant lists
Each key is named after the grantee
"""
def load_grants():
	
	global _grant_data

	try:
		grant_files = _config_data["StockCertificateSummaryFiles"]
		
		for i, (grantee, file_path) in enumerate(grant_files.items()):
			with open(file_path, 'r') as grant_file:
				_grant_data[grantee] = load_grant_csv(grant_file)

	except:
		print("No grant info available. Is the config file loaded / are grant files specified?")


def get_grants():

	return _grant_data


def get_config_data():

	return _config_data


def load_config_file():

	global _config_data

	with open_config_file() as file_obj:

		_config_data = json.loads(file_obj.read())

	return 1


load_config_file()
load_grants()