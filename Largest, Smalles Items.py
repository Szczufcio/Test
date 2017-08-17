import heapq

grades =  [23,54,76,43,23,64,86,34,74,34,64,57,32,67]

print(heapq.nlargest(3,grades))

stocks = [
    {'ticker': 'AAPL', 'price': 201},
    {'ticker': 'GOOG', 'price': 600},
    {'ticker': 'MSFT', 'price': 343},
    {'ticker': 'F', 'price': 65}
]

print(heapq.nsmallest(2,stocks,key = lambda stock: stock['price']))