import financial_data_class as fin
import stock_sale_strategy as strat

fin_data = fin.FinancialData("user_data/TaxEstimateConfig.json")
print(fin_data.config_data)
print("\n\n")
print(fin_data.grant_data)