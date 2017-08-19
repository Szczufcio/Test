a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
y = []
for x in a:
    if x % 2 == 1:
        print(str(x) + ' is not a even')
    else:
        y.append(x)

print (y)

