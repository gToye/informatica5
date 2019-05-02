from math import sqrt

a = float(input('geef een getal a groter dan 0: '))
b = float(input('geef een getal b groter dan 0: '))

c = float(sqrt((a ** 2)+ (b ** 2)))
print('In een rechthoekige driehoek met rechthoekszijden a = ' + str(round(a, 2)) + ' en b = ' + str(round(b, 2)) + ' is de schuine zijde ' + str(round(c, 2)))