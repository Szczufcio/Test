def add_numbers(*args): #Bierzemy argumenty ale nwm ile, args można nazwać inaczej ale zazwyczaj "args"
    total = 0
    for a in args:
        total += a
    print (total)


add_numbers(3,4,6,7,8,5)
