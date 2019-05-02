snelheid_stijn = int(input('Wat is de snelheid van Stijn?'))
snelheid_kaat = int(input('wat is de snelheid van Kaat?'))
afstand = int(input('wat is de afstand tussen stijn en kaat?'))
tijd = 0
while afstand > (snelheid_kaat+snelheid_stijn):
    tijd += 1
    afstand -= (snelheid_kaat + snelheid_stijn)
while afstand == (snelheid_kaat+snelheid_stijn):
    tijd += 1
    afstand -= (snelheid_stijn+snelheid_kaat)

if afstand > 0:
    tijd += 1

print('Na ' + str(tijd) + ' s hebben Stijn en Kaat elkaar ontmoet.')