a = int(input('Give a number\n'))
c = 0
for x in range(2,(a + 1)):
    print (a % x)
    if a % x == 0:
        c += 1

if c > 2:
    print('Not a prime')
else:
    print('Prime')