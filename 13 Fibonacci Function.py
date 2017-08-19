def fibbo(a):
    c = [0,1]
    for x in range((a-1)):
        c.append((c[x] + c[x + 1] ))
    c.pop(0)
    print (c)

b = int(input('How many fibonacci numbers?\n'))

fibbo(b)

