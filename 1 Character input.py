a = str(input ("Enter your name\n"))
b = int(input ("Enter you age\n"))
years_left = str(100 - b)
print ( a + " - you will turn 100 in " + years_left + " years")

print('Do you want to display message again ? 1 = Yes, 2 = No')
c = int(input ("Number:"))
if c == 1:
    d = int(input("How many times do you want to display message?"))
    for i in range(d):
        print(a + " - you will turn 100 in " + years_left + " years")
elif c == 2:
    print ("Good buy then")