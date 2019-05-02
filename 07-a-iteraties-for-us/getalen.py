aantal = int(input('aantal'))
som = 0
grootste = int(input('getal: '))
for i in range(aantal ):
    getal = int(input('getal:'))
    som += getal
    if(getal > grootste):
        grootste == getal

print('Het grootste getal is {} en het gemiddelde is {:.2f}'.format(grootste,som/aantal))