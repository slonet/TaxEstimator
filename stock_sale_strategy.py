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

	sale_qty = min(np.ceil(proceeds_goal / fair_market_value), total_shares)
	proceeds = sale_qty * fair_market_value

	data_obj.sale_data["total_qty"] = total_shares
	data_obj.sale_data["total_sale_qty"] = sale_qty
	data_obj.sale_data["total_proceeds"] = proceeds

	return total_shares, sale_qty, proceeds

"""
1. Sort all grants in order of vesting date.
2. Iterate through starting with newest and sum up to the sale_qty. Mark shares to sell in the grant data
"""
def newest(data_obj):

	return

def newest_ltcg(data_obj):
	return

def high_cost_basis(data_obj):
	return

def avg_cost_basis(data_obj):
	return

def avg_age(data_obj):
	return

def low_cost_basis(data_obj):
	return