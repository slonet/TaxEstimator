import csv
from datetime import datetime

"""
Prompts the user for the paths to each Solium stock certificate file.
Multiple files can be specified.
A file object is returned for each that can be opened.
Errors are printed to the terminal for any that cannot be opened.
"""
def open_stock_cert_files():
	print("Enter the relative paths to each Solium stock certificate file to be parsed")
	print("Separate the paths with \", \"")
	file_string = input("\n> ")

	file_paths = file_string.split(", ")
	files = []

	for file_path in file_paths:
		try:
			file = open(file_path, 'r')
			files.append(file)

		except:
			print(f"\nCould not open the file with path \"{file_path}\"")

	return files


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
def parse_grant_csv_row(row):

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
def parse_grant_csv(file_obj):

	grants = []

	with file_obj:
		csv_reader = csv.reader(file_obj, delimiter=',')

		for row in csv_reader:
			for item in row:
				if item.count("$"): # found a row with a grant					
					grants += parse_grant_csv_row(row)

	return grants


def get_stock_grants():

	csv_files = open_stock_cert_files()

	grants = []

	# iterate through each grant file provided and merge the grant data into one dictionary
	for file_obj in csv_files:
		grants += parse_grant_csv(file_obj)

	return grants


def parse_config_file(config_file):
	return config

grants = get_stock_grants()

for grant in grants:
	print(grant)