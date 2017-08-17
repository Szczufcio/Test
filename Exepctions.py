while True:
    try:
        number = int(input('Fav num\n'))
        print(18/number)
        break
    except ValueError:
        print('Make sure you enter a number')
    except ZeroDivisionError:
        print('Make sure number isnt zero')
    finally:    #zawsze się wyświetla
        print ('Ey b0ss, fuck you man')