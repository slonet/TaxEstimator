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

"""
"""
def _total_shares(grant_data):
	return


def _sale_qty(grant_data, proceeds_goal, fair_market_value):


	return total_shares, sale_qty, proceeds


def newest_first(grant_data, proceeds_goal, fair_market_value):
	return