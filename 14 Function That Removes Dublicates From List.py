def Remove(a):
    b = []
    for x in range(len(a)):
        if a[x] not in b:
            b.append(a[x])
    print(b)

c = []
y = int(input('How many numbers you want in your list\n'))
for f in range(y):
    x = int(input('What numbers will it be (' + str(f + 1) + ')\n'))
    c.append(x)

Remove(c)