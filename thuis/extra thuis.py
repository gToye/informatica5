
antwoord = input('neem een getal in je hoofd! ')
if  antwoord == 'ok' :
   antwoord_1 = input('vermenigvuldig dit met 4. ')
if antwoord == 'ok':
    antwoord_2 = input('deel door 2. ')
if antwoord_2 == 'ok':
    antwoord_3 = input('vermenigvuldig met 7. ')
if antwoord_3 == 'ok':
    antwoord_4 = input('wat is de uitkomst?')

print(int(antwoord_4) /14)
antwoord_5 = input('Is het juist? ')
if antwoord_5 == 'ja':
    print('\N{grinning face with smiling eyes}' + ' joepie ' + '\N{grinning face with smiling eyes}' )
elif antwoord_5 == 'nee':
    print('sorry')
