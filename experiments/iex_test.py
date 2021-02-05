from iexfinance.stocks import Stock


a = Stock("AAPL", token="Tpk_2fd9978373f24564a5a786757629c422")
a.version='iexcloud-sandbox'
print(a.get_quote())
