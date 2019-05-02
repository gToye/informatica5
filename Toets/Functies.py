def doe_maar_gewoon(woord):
    for i in range(len(woord)-1):
        if woord[i + 1] != woord[i]:
            if woord[i] == woord[i+1].upper():
                letter = woord[i].lower()
                woord = woord[:i] + letter + woord[i+1:]
    return woord
print(doe_maar_gewoon('kaKken'))
def bereken_prijs(zin):
    prijs = 0
    x = zin.find('<')
    y = zin.find('>')
    oke = zin[y:]
    d = oke.find('<')
    e = oke.find('>')
    return len(zin[:x] + zin[y:]) * 1.33 + len(oke[:d]+oke[e:])
print(bereken_prijs('ik ben<gill> en ik hou van <jou>'))