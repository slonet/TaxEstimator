"""
stock_sale_strategy.py is a module that accepts stock grant data, desired pre-tax proceeds,
and outputs stock grant data with specific shares marked for sale. The shares are selected
based on a number of strategies. One strategy can be selected per run.

Stock sale strategies
1. Sell Newest 1st
2. Sell Newest LTCG Shares
3. Sell Highest Cost Basis
4. Sell Average Cost Basis Mix
5. Sell Average Age Mix
6. Sell Lowest Cost Basis
"""

#TODO: move code that fills shares to sell into a private function

from datetime import datetime
import numpy as np


def _total_shares(data_obj):

	shares = 0

	for grant in data_obj.grant_data:
		shares += grant["shares_qty"]

	return shares


def sale_qty(data_obj):
	proceeds_goal = data_obj.config_data["ProceedsGoal"]
	fair_market_value = data_obj.config_data["FairMarketValue"]
	
	total_shares = _total_shares(data_obj)

	# if the goal is to raise more funds than possible with the total no. of shares, 
	# the sale qty caps out at the total no. of shares and the proceeds will similarly cap out

	qty = min(np.ceil(proceeds_goal / fair_market_value), total_shares)
	proceeds = qty * fair_market_value

	data_obj.tax_data["total_qty"] = total_shares
	data_obj.tax_data["total_sale_qty"] = qty
	data_obj.tax_data["total_proceeds"] = proceeds

	return total_shares, qty, proceeds

"""
1. Sort all grants in order of vesting date.
2. Iterate through starting with newest and sum up to the sale_qty. Mark shares to sell in the grant data
"""
def sort_vest_date_ascend(data_obj):
	
	n = len(data_obj.grant_data)
	swaps = 1
	
	while swaps:
		swaps = 0

		for i in range(1,n):
			prev_grant = data_obj.grant_data[i-1]
			curr_grant = data_obj.grant_data[i]

			if prev_grant["vesting_date"] > curr_grant["vesting_date"]: # swap elements
				data_obj.grant_data[i-1] = curr_grant
				data_obj.grant_data[i] = prev_grant
				swaps += 1

	return data_obj


def sort_vest_date_descend(data_obj):
	
	n = len(data_obj.grant_data)
	swaps = 1
	
	while swaps:
		swaps = 0

		for i in range(1,n):
			prev_grant = data_obj.grant_data[i-1]
			curr_grant = data_obj.grant_data[i]

			if prev_grant["vesting_date"] < curr_grant["vesting_date"]: # swap elements
				data_obj.grant_data[i-1] = curr_grant
				data_obj.grant_data[i] = prev_grant
				swaps += 1

	return data_obj


def sort_cost_basis_ascend(data_obj):
	
	n = len(data_obj.grant_data)
	swaps = 1
	
	while swaps:
		swaps = 0

		for i in range(1,n):
			prev_grant = data_obj.grant_data[i-1]
			curr_grant = data_obj.grant_data[i]

			if prev_grant["cost_basis"] > curr_grant["cost_basis"]: # swap elements
				data_obj.grant_data[i-1] = curr_grant
				data_obj.grant_data[i] = prev_grant
				swaps += 1

	return data_obj


def sort_cost_basis_descend(data_obj):
	
	n = len(data_obj.grant_data)
	swaps = 1
	
	while swaps:
		swaps = 0

		for i in range(1,n):
			prev_grant = data_obj.grant_data[i-1]
			curr_grant = data_obj.grant_data[i]

			if prev_grant["cost_basis"] < curr_grant["cost_basis"]: # swap elements
				data_obj.grant_data[i-1] = curr_grant
				data_obj.grant_data[i] = prev_grant
				swaps += 1

	return data_obj


def newest(data_obj):

	total_shares, qty, proceeds = sale_qty(data_obj)
	data_obj = sort_vest_date_descend(data_obj)
	
	for grant in data_obj.grant_data:
		if qty >= grant["shares_qty"]:
			grant["shares_to_sell"] = grant["shares_qty"]
			qty -= grant["shares_to_sell"]

		elif qty <= 0:
			break

		elif qty < grant["shares_qty"]:
			grant["shares_to_sell"] = qty
			qty -= grant["shares_to_sell"]

	return data_obj


def oldest(data_obj):

	total_shares, qty, proceeds = sale_qty(data_obj)
	data_obj = sort_vest_date_ascend(data_obj)
	
	for grant in data_obj.grant_data:
		if qty >= grant["shares_qty"]:
			grant["shares_to_sell"] = grant["shares_qty"]
			qty -= grant["shares_to_sell"]

		elif qty <= 0:
			break

		elif qty < grant["shares_qty"]:
			grant["shares_to_sell"] = qty
			qty -= grant["shares_to_sell"]

	return data_obj


def newest_ltcg(data_obj):
	
	today = datetime.today()
	total_shares, qty, proceeds = sale_qty(data_obj)
	data_obj = sort_vest_date_descend(data_obj)

	start_ind = -1

	for grant in data_obj.grant_data:
		start_ind += 1
		if (today - grant["vesting_date"]).days >= 365: # long term shares held for more than 1 year
			break

	if start_ind == len(data_obj.grant_data) - 1: # no LTCG shares
		return -1

	i = start_ind

	while qty > 0:
		if qty >= data_obj.grant_data[i]["shares_qty"]:
			data_obj.grant_data[i]["shares_to_sell"] = data_obj.grant_data[i]["shares_qty"]
			qty -= data_obj.grant_data[i]["shares_to_sell"]

		elif qty < data_obj.grant_data[i]["shares_qty"]:
			data_obj.grant_data[i]["shares_to_sell"] = qty
			qty -= data_obj.grant_data[i]["shares_to_sell"]

		i += 1

	return data_obj


def high_cost_basis(data_obj):

	total_shares, qty, proceeds = sale_qty(data_obj)
	data_obj = sort_cost_basis_descend(data_obj)
	
	for grant in data_obj.grant_data:
		if qty >= grant["shares_qty"]:
			grant["shares_to_sell"] = grant["shares_qty"]
			qty -= grant["shares_to_sell"]

		elif qty <= 0:
			break

		elif qty < grant["shares_qty"]:
			grant["shares_to_sell"] = qty
			qty -= grant["shares_to_sell"]

	return data_obj


def avg_cost_basis(data_obj):
	return


def avg_age(data_obj):
	return


def low_cost_basis(data_obj):
	return