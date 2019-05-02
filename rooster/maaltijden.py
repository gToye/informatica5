def dagprijs(rooster):

    prijs = 0
    for i in range(len(rooster)-1):
        if rooster[i] == 'middagmaal':
            prijs += ((rooster[i+1]) * 5.3)
        if rooster[i] == 'soep':
            prijs += ((rooster[i + 1]) * 1.7)
        if rooster[i] == 'vieruurtje':
            prijs += ((rooster[i + 1]) * 2.3)
        else:
            prijs += 0
    return prijs
def weekprijs(rooster):
    weekprijs = 0
    for dag in rooster:
        weekprijs += dagprijs(dag)
    return weekprijs

print(dagprijs(('middagmaal', 2, 'vieruurtje', 2)))