import csv
import json
from datetime import datetime

#TODO: flesh out sale data structure
"""
config_data:
	Contains all of the user inputs. Formatted as a JSON file that is read into a big dictionary

grant_data:
	Dictionary where the keys are grantees. Each key contains a list of dictionaries representing
	all of the individual grants held by the grantee.
"""
class FinancialData:

	def __init__(self, config_file_path):
		self.config_data = self._load_config_file(config_file_path)
		self.grant_data = self._load_grants()
		self.sale_data = {
			"total_qty"      : 0,
			"total_sale_qty" : 0,
			"total_proceeds" : 0
		}


	"""
	Extracts the grant data from a grant CSV file row after being converted to a list
	The date is represented as a datetime object so math can easily be done
	"""
	def _load_grant_csv_row(self, row):

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
	def _load_grant_csv(self, file_obj):

		grants = []

		with file_obj:
			csv_reader = csv.reader(file_obj, delimiter=',')

			for row in csv_reader:
				for item in row:
					if item.count("$"): # found a row with a grant					
						grants += self._load_grant_csv_row(row)

		return grants

	"""
	Loads a number of stock certificate summary CSV files and creates a dictionary of the grant lists
	Each key is named after the grantee
	"""
	def _load_grants(self):

		grant_data = {}

		try:
			grant_files = self.config_data["StockCertificateSummaryFiles"]
			
			for i, (grantee, file_path) in enumerate(grant_files.items()):
				with open(file_path, 'r') as grant_file:
					grant_data[grantee] = self._load_grant_csv(grant_file)

		except:
			print("No grant info available. Is the config file loaded / are grant files specified?")

		return grant_data


	def _load_config_file(self, file_path):

		with open(file_path) as file_obj:
			config_data = json.loads(file_obj.read())

		return config_data