x = 1
while x!=0:

    print('[1] - Paper\n'
          '[2] - Rock\n'
          '[3] - Scissors\n'
          )
    c = int(input('Player 1 pick a number\n'))
    y = int(input('Player 2 pick a number\n'))

    if (c == 3) and (y == 1) or (c == 2) and (y == 3) or (c == 1) and (y == 2):
        print('Player 1 wins')

    if (c == 1) and (y == 3) or (c == 3) and (y == 2) or (c == 2) and (y == 1):
        print('Player 2 wins')

    if c == y :
        print('Draw')

    x = int(input('Play Again - Any Number, End - [0]\n'))

