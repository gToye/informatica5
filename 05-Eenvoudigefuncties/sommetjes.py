a = float(input('getal 1:'))
b = float(input('getal 2:'))
from random import random, randint, seed
getal_1 = (10**0) * a
getal_2 = (10 ** 0) * b
getal_3 = getal_1 + getal_2

getal_4 = (10**1) * a
getal_5 = (10 **1) * b
getal_6 = getal_4 + getal_5

getal_7 = (10**2) * a
getal_8 = (10 ** 2) * b
getal_9 = getal_7 + getal_8

getal_10 = (10 ** 3) * a
getal_11 = (10 ** 3) * b
getal_12 = getal_10 + getal_11

getal_13 = (10**4) * a
getal_14 = (10 ** 4) * b
getal_15 = getal_13 + getal_14

print('{:>6.0f} + {:<6.0f} = {:<6.0f}'.format(getal_1,getal_2,getal_3))
print('{:>6.0f} + {:<6.0f} = {:<6.0f}'.format(getal_4,getal_5,getal_6))
print('{:>6.0f} + {:<6.0f} = {:<6.0f}'.format(getal_7,getal_8,getal_9))
print('{:>6.0f} + {:<6.0f} = {:<6.0f}'.format(getal_10,getal_11,getal_12))
print('{:>6.0f} + {:<6.0f} = {:<6.0f}'.format(getal_13,getal_14,getal_15))
