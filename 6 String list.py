x = str(input("Input a string\n"))

print(x)

if len(x) % 2 == 1:
    middle = int(len(x)/2 + 1)
    print(middle)
    print('Prime number\n')
    print(x[:middle-1])
    print((x[(len(x)-1):middle-1:-1]))
    if (x[:middle-1]) == (x[(len(x)-1):middle-1:-1]):
        print('And palindrome')
    else:
        print('And not palindrome')

else:
    middle = int(len(x)/2)
    print(middle)
    print('Not a prime')
    print(x[:middle])
    print(x[(len(x)-1):(middle-1):-1])
    if x[:middle] == x[(len(x)-1):(middle-1):-1 ]:
        print('And a palindrome')
    else:
        print('Not a palindrome')


