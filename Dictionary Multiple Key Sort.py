from operator import itemgetter

users = [
    {'fname':'Ofal', 'lname': 'Szewczak'},
    {'fname':'Konrad', 'lname': 'Bagieta'},
    {'fname':'Ala', 'lname': 'Cebula'},
    {'fname':'Wojtek', 'lname': 'Kryminalista'},
    {'fname':'Maciej', 'lname': 'Friendzone'},
    {'fname':'Grzechu', 'lname': 'Kuc'}
]

for x in sorted(users, key=itemgetter('fname')):
    print(x)

print('----')
for x in sorted(users, key=itemgetter('fname','lname')):#to sortuje najpierw pierwsze imię a potem drugie
    print(x)
