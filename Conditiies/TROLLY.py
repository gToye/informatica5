antwoord_1 = (input('Trek je aan de hendel van de wissel?'))
antwoord_2 = (input('Duw je de man van de brug?'))
if antwoord_1 == 'ja' and antwoord_2 == 'ja':
    doden = 2
elif antwoord_1 == 'nee' and antwoord_2 == 'nee':
    doden = 5

else:
    doden = 1
print(doden)