operation = int(input("Operation 1 or 2\n"))

if operation == 1:
    number = int(input("Give me a number\n"))
    if (number % 2) == 0:
        print ('Your nubmer is even')
        if (number % 4) == 0:
            print('And is a multiple of 4')
    else:
        print('Your number is odd')

elif operation == 2:
    num = int(input('Number one:'))
    check = int(input('Number two:'))
    if (num % check) == 0:
        print('Your first number is divided by the second one')
    else:
        print("Your first number isn't divided by the secon one")





