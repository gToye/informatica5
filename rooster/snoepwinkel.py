def bereken_prijs(rooster):
    prijs = 0
    for i in rooster:
        prijs += i[1]
    return prijs

def winkelbriefje(rooster):
    lijst = []
    for i in rooster:
        lijst.append(i[0])
    return lijst

def sorteer(rooster):
    from operator import itemgetter
    rooster.sort(key=itemgetter(1))
    return rooster


print(sorteer([('Lays Paprika', 3.94), ('Napoleon', 1.48), ('Milky Way', 3.64), ('M&M', 3.06), ('Crocky Zout', 3.62), ('Bounty', 1.86)]))