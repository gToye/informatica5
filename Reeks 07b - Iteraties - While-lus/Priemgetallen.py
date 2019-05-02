getal = int(input('Geef een getal: '))
a = 2
b = 1

while a < getal:
    if (getal % a ) == 0:
        mess = '{} is geen priemgetal'.format(getal)
        b = 0
    a += 1
if b and getal != 1:
    mess = '{} is een priemgetal'.format(getal)
elif getal == 1:
    mess = '{} is geen priemgetal'.format(getal)

print(mess)
