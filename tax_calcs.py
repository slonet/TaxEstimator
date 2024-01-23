import numpy as np
from datetime import datetime


def _load_tax_brackets(data_obj, bracket_key):

	thresholds = data_obj.config_data["TaxBrackets"][bracket_key]["TaxThresholds"]
	rates = data_obj.config_data["TaxBrackets"][bracket_key]["TaxRates"]
	
	return thresholds, rates


def total_regular_income(data_obj):

	'''
	1. identify the regular income dictionaries from the config data
	2. sum the pre-tax and other income entries
	3. write the total regular income into the tax data dictionary
	'''

	reg_income = 0.00

	for field in data_obj.config_data:
		if field.find("RegularIncome") + 1:
			try:
				reg_income += data_obj.config_data[field]["PreTaxIncome"]

			except:
				pass

			try:
				reg_income += data_obj.config_data[field]["OtherIncome"]

			except:
				pass

	data_obj.tax_data["total_regular_income"] = reg_income

	return data_obj


def total_taxable_income(data_obj):
	
	taxable_income = 0.00

	for field in data_obj.config_data:
		if field.find("RegularIncome") + 1:
			try:
				taxable_income += data_obj.config_data[field]["PreTaxIncome"]

			except:
				pass

			try:
				taxable_income += data_obj.config_data[field]["OtherIncome"]

			except:
				pass

			try:
				taxable_income -= data_obj.config_data[field]["401kContributions"]

			except:
				pass

	data_obj.tax_data["total_taxable_income"] = taxable_income

	return data_obj


def long_term_cap_gains(data_obj):
	
	'''
	1. iterate through all grants
		a. if today - vesting date > 365, sum (FMV - cost basis) * qty to sell
	'''

	fmv = data_obj.config_data["FairMarketValue"]
	ltcg = 0.00
	today = datetime.today()

	for grant in data_obj.grant_data:
		if (today - grant["vesting_date"]).days >= 365:
			ltcg += (fmv - grant["cost_basis"]) * grant["shares_to_sell"]

	data_obj.tax_data["long_term_cap_gains"] = ltcg

	return data_obj


def short_term_cap_gains(data_obj):
	
	fmv = data_obj.config_data["FairMarketValue"]
	stcg = 0.00
	today = datetime.today()

	for grant in data_obj.grant_data:
		if (today - grant["vesting_date"]).days < 365:
			stcg += (fmv - grant["cost_basis"]) * grant["shares_to_sell"]

	data_obj.tax_data["short_term_cap_gains"] = stcg

	return data_obj


def state_tax_liability(data_obj):

	'''
	1. load state tax brackets into lists
	'''

	return


def fed_tax_liability(data_obj):
	return


def fed_ltcg_liability(data_obj):
	return


def niit_liability(data_obj):
	return


def est_tax_payment(data_obj):
	return