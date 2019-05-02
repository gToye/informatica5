#invoer
v1 = float(input('verkeersdichtheid vrachtvoer eerst rijvak?'))
d1 = float(input('snelheid van vrachtverkeer eerste rijvak?'))
v2 = float(input('verkeersdichtheid van het personenvervoer op het tweede rijvak?'))
d2 = float(input('snelheid van het personenvervoer op het tweede rijvak?'))
#berekeningen
pv = min((v1*d1/40),1)
pa = min((v2*d2/40),1)
min = min(pv,pa)
max = max(pv,pa)
verschil = abs(pv - pa)
#bepalen filegevaar
if min > 0.7 :
    mes = 'zwart'
elif max >0.7 and verschil < 0.2 :
    mes = 'rood'
elif max > 0.7 and verschil > 0.7 :
    mes = 'geel'
else :
    mes = 'groen'
#uitvoer
print(mes)