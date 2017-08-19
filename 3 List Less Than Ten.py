a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
for i in a:
    if i < 5:
        print (i)
        b.append(i)
print (b)

c = int(input("\nEnter a number"))
for i in a:
    if i < c:
        print (i)
