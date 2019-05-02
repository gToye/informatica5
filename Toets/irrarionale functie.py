from math import sqrt
#input
x = float(input('geef x?'))
#bepalen uitvoer
if  x > 2 :
    fx = sqrt(x - 2)
    mes = 'f('+'{:.2f}'.format(x)+') = '+'{:.2f}' . format(fx)
elif    x == 2:
    mes = '{:.2f}'.format(x) + ' is nulpunt van f'
if x < 2 :
    mes = '{:.2f}'.format(x) + ' ∉ dom(f)'
#uitvoer
print(mes)

