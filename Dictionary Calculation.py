stocks = {
    'GOOG' : 434,
    'AAPL' : 325,
    'FB' : 54,
    'AMZN' : 674,
    'F' : 32,
    'MSFT' : 547
}

min_price = min(zip(stocks.values(), stocks.keys()))
print(min_price)