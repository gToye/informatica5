def volgende_rij(rij):
    nieuwe_rij = []
    for i in range(len(rij)-1):
            if rij[i] == rij[i+1]:
                nieuwe_rij.append(rij[i])
            else:
                if (rij[i] == 'G' or rij[i] == 'Y') and (rij[i+1] == 'G' or rij[i+1] == 'Y'):

                    nieuwe_rij.append('R')
                elif (rij[i] == 'G' or rij[i] == 'R') and (rij[i+1] == 'R' or rij[i+1] == 'G'):
                    nieuwe_rij.append('Y')
                else:
                    nieuwe_rij.append('G')
    return nieuwe_rij
def driehoek(onderste_rij):
    driehoek = [onderste_rij]
    volgende = volgende_rij(onderste_rij)
    while len(volgende) > 0:
        driehoek.append(volgende)
        volgende = volgende_rij(volgende)
    return driehoek
def kleuren(driehoek):
    Y = 0
    G = 0
    R = 0
    for i in range(len(driehoek)):
        Y += driehoek[i].count('Y')
        R += driehoek[i].count('R')
        G += driehoek[i].count('G')
    return(G,R,Y)
print(kleuren([['Y', 'R', 'G', 'Y', 'Y'], ['G', 'Y', 'R', 'Y'], ['R', 'G', 'G'], ['Y', 'G'], ['R']]))