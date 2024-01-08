import financial_data_class as fin
import stock_sale_strategy as strat

fin_data = fin.FinancialData("user_data/TaxEstimateConfig.json")
strat.sale_qty(fin_data)
print(fin_data.sale_data["total_qty"])
print(fin_data.sale_data["total_sale_qty"])
print(fin_data.sale_data["total_proceeds"])
print("\nAll shares:\n")

for grant in fin_data.grant_data:
	print(f"{grant}\n")