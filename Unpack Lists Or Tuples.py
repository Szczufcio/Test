item = ['dwa', 'chuk', 9.45]
date,item,price = item
print (date,item,price)

def drop_first_last(grades):
    first, *middle, last = grades
    avg = sum(middle) / len(middle)
    print(avg)

drop_first_last([23,524,64,34,2,6,7,5,4])