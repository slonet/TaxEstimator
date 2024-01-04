import csv

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
row 0 = grant_id
row 3 = cost_basis
row 5 = vesting_date
row 7 = shares_qty
"""
def parse_grant_csv_row(row):

	grant = {
		"grant_id"     : row[0],
		"cost_basis"   : float(row[3].replace('$','')),
		"vesting_date" : row[5],
		"shares_qty"   : int(row[7].replace(',',''))
	}

	return grant


"""
Accepts a file object pointing to a Solium stock stock certificate summary csv
Parses all of the available grants from the file
Returns a dictionary containing the stock grant data
"""
def parse_grant_csv(grant_csv):

	grants = {}

	with grant_csv:
		csv_reader = csv.reader(grant_csv, delimiter=',')

		for row in csv_reader:
			for item in row:
				if item.count("$"): # found a row with a grant
					grant = parse_grant_csv_row(row)
					print(grant)

	return grants


def parse_config_file(config_file):
	return config


file = open_stock_cert_files()
grants = parse_grant_csv(file[0])