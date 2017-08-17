stocks = {
    'GOOG': 520.24,
    'FB': 342.34,
    'YHOO': 235.23,
    'AMZN': 345.54,
    'AAPL': 98.34
}

print(min(zip(stocks.values(),stocks.keys())))
print(max(zip(stocks.values(),stocks.keys())))
print(sorted(zip(stocks.values(),stocks.keys())))