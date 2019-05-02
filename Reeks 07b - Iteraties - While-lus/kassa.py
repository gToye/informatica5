totaal_bedrag = 0
prijs = 1

while prijs > 0:
    prijs = float(input('Hoeveel kost het? '))
    totaal_bedrag += prijs

print('De totale prijs is € ' + '{:.2f}'.format(totaal_bedrag))