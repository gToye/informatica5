antwoord_1 = input('Blad,steen of schaar?')
antwoord_2 = input('Blad,steen of schaar?')
if  antwoord_1 == antwoord_2 :
    print('onbeslist')
if  antwoord_1 == 'blad' and antwoord_2 == 'steen':
    print('speler 1 wint')
if  antwoord_1 == 'blad' and antwoord_2 == 'schaar':
    print('speler 2 wint')
if  antwoord_1 == 'steen' and antwoord_2 == 'blad':
    print('speler 2 wint')
if  antwoord_1 == 'steen' and antwoord_2 == 'schaar':
    print('speler 1 wint')
if  antwoord_1 == 'schaar' and antwoord_2 == 'blad':
    print('speler 1 wint')
if  antwoord_1 == 'schaar' and antwoord_2 == 'steen':
    print('speler 2 wint')
