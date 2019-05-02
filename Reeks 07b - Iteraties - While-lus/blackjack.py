kaart = int(input('Geef een kaart tussen 1 en 11:'))
totaal = 0

while kaart > 0 and kaart + totaal < 21:
    totaal += kaart
    kaart = int(input('Geef een kaart tussen 1 en 11:'))
if kaart  + totaal == 21:
    mess = 'Gewonnen!'
elif kaart + totaal < 21:
    mess = 'Voorzichtig gespeeld ({})'.format(kaart + totaal)
else:
    mess = 'Verbrand ({})'.format(totaal + kaart)

print(mess)