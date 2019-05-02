woord = str(input('Geef een verborgen woord: '))
geld = int(input('Geef gedraaid geldbedrag:'))
letter = str(input('Geef een letter: '))
totaal_geld = 0
string_woord = ''

while letter in woord and letter not in string_woord:
    totaal_geld += geld
    string_woord += letter
    letter = str(input('Geef een letter: '))

if letter not in woord:
    totaal_geld == 0

print(totaal_geld)