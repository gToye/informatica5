leeftijd = float(input('leeftijd: '))
if leeftijd > 16 and leeftijd >= 21:
    print('Drink met mate.')
elif leeftijd >= 16:
    print('Wel een pilsje, geen sterke drank')
else:
    print('Alcohol verboden!')