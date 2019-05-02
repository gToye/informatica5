g1 = float(input('getal 1:'))

g2 = float(input('getal 2:'))
linker_lid =abs(abs(g1) - abs(g2))
rechter_lid= abs(g1- g2)
uitvoer = '{:.4f} ≤ {:.4f}'.format(linker_lid, rechter_lid)
print(uitvoer)