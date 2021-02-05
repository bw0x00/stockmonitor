from iexfinance.stocks import Stock

a = Stock("AAPL", token="pk_5bc5ea10ae99491f91ab7b8a7c75c7f4")
print(a.get_quote())
