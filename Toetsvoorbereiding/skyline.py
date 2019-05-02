gebouwen = int(input('aantal gebouwen'))
for i in range(0,1):
    naam = input('naam gebouw')
    hoogte = input('hoogte gebouw')
    print(naam +' is zichtbaar van het gelijkvloers tot '+ hoogte + ' meter.')
    y = hoogte
for i in range (0,gebouwen):
    naam = input('naam gebouw')
    hoogte = input('hoogte gebouw')
    if hoogte >= y:
        print(naam +' is zichtbaar van ' + y + ' meter tot '+ hoogte + ' meter.')
        y = hoogte


