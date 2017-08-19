import random

c = int(input('What number you want to start from?\n'))
d = -1
while c > d:
    d = int(input('What number should be the last one? (Cant be lesser than starting one)\n'))
a = random.randint(c,d)

b = int(input('Input a number beetwen ' +  str(c) + ' and ' +  str(d) + '\n'))
while a != b:
    print(a)
    if b > a:
        print('Your number is higher than generated\n')
    elif b < a:
        print('Your number is lesser than generated\n')

    b = int(input('Input a number beetwen ' +  str(c) + ' and ' +  str(d) + '\n'))
print('You guessed it\n')