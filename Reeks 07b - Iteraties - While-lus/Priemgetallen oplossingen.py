getal = int(input('getal:'))
#Zolang je het niet kan delen door 2,3,4 is het allicht een priemgetal.
deler = 2
while getal % deler != 0 and getal != 1:
    deler += 1

if deler == getal:
    print('priemgetal')
else:
    print('geen priemgetal')