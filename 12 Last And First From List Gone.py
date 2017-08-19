a = [ x for x in range(1,101) if x % 5 == 0]

print (a)

print(len(a))

b = []
b.append(a[0])
b.append(a[(len(a) - 1)])

print (b)

