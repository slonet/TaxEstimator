import financial_data_class as fin
import stock_sale_strategy as strat
import tax_calcs as tax

fin_data = fin.FinancialData("user_data/TaxEstimateConfig.json")


print("APPLYING SHARES SALE STRATEGY")

fin_data = strat.newest(fin_data)
'''
for grant in fin_data.grant_data:
	print(grant["grant_id"])
	print(grant["vesting_date"])
	cost_basis = grant["cost_basis"]
	print(f"Cost basis: ${cost_basis}")
	total = grant["shares_qty"]
	print(f"Shares in grant: {total}")
	qty = grant["shares_to_sell"]
	print(f"Shares to sell: {qty}\n")


fin_data = tax.total_regular_income(fin_data)
fin_data = tax.total_taxable_income(fin_data)
fin_data = tax.long_term_cap_gains(fin_data)
fin_data = tax.short_term_cap_gains(fin_data)

print(fin_data.tax_data["total_regular_income"])
print(fin_data.tax_data["total_taxable_income"])
print(fin_data.tax_data["long_term_cap_gains"])
print(fin_data.tax_data["short_term_cap_gains"])
'''

thresholds, rates = tax._load_tax_brackets(fin_data, "StateIncomeTax")

print(thresholds)
print(rates)