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


def parse_stock_certs(stock_cert_files):
	return grant_data


def parse_config_file(config_file):
	return config

files = open_stock_cert_files()
print(files)