def kleur_toevoegen(rooster,kleur):
    g1 = rooster[0]
    g2 = rooster[1]
    g3 = rooster[2]
    if kleur == 'groen':
        g2 += 1
    if kleur == 'blauw':
        g3 += 1
    if kleur == 'rood':
        g1 += 1
    nieuw_rooster = [g1,g2,g3]
    return nieuw_rooster
def is_wit(rooster):
    g1 = rooster[0]
    g2 = rooster[1]
    g3 = rooster[2]
    if g3 == g2 and g2 == g1:
        return True
    else:
        return False
def verf_verzamelen(kleuren):
    g1 = 0
    g2 = 0
    g3 = 0
    ok = 0
    aantal_keer = 0
    for i in range(len(kleuren)):
        if (g1 != g2 or g2 != g3) or g1 == 0:
            if kleuren[i] == 'groen':
                g2 += 1
            elif kleuren[i] == 'rood':
                g1 += 1
            else:
                g3 += 1
            aantal_keer += 1
        else:
            ok += 1
    if ok != 0:
        return (aantal_keer, [g1, g2, g3])
    else:
        'niets'


print(verf_verzamelen(['blauw', 'rood', 'groen', 'blauw', 'rood', 'groen']))
