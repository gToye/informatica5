def printbaar_rek(rek):
    rij_1 = rek[0][0] + rek[0][1] + rek[0][2] + rek[0][3] + rek[0][4]
    rij_2 = rek[1][0] + rek[1][1] + rek[1][2] + rek[1][3] + rek[1][4]
    rij_3 = rek[2][0] + rek[2][1] + rek[2][2] + rek[2][3] + rek[2][4]
    rij_4 = rek[3][0] + rek[3][1] + rek[3][2] + rek[3][3] + rek[3][4]
    oplossing = rij_4 +  '\n' + rij_3  + '\n' + rij_2+ '\n' + rij_1

    return oplossing


def speel(kleur,kolom,bord):
    hulp = 0

    for i in range(len(bord)):
        if bord[i][kolom-1] == 'O':
         hulp += 1

    if hulp == 4:
        bord[0][kolom] = kleur
    if hulp == 3:
        bord[1][kolom] = kleur
    if hulp == 2:
        bord[2][kolom] = kleur
    if hulp == 1:
        bord[3][kolom] = kleur

    return printbaar_rek(bord)


print(speel('G',3,[['R', 'R', 'R', 'R', 'G'], ['G', 'G', 'R', 'G', 'R'], ['O', 'G', 'O', 'O', 'O'], ['O', 'R', 'O', 'O', 'O']]))