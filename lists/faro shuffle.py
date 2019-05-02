def nieuw_kaartspel(lijst,lijst_2):
    nieuwe_lijst =[]
    for i in range(len(lijst)):
        for x in range(len(lijst_2)):
            nieuwe_lijst.append(lijst[i] + lijst_2[x])
    return nieuwe_lijst



def splits_kaartspel(lijst):
    lijst_2 = lijst[:(len(lijst)//2)]
    lijst_1 = lijst[len(lijst)//2:]

    return (lijst_2 ,lijst_1)

def faro_shuffle(lijst,lijst_2):
    if len(lijst_2) != 1:
        nieuwe_lijst = []
        for i in range(len(lijst)):
            nieuwe_lijst.append(lijst[i])
            nieuwe_lijst.append(lijst_2[i])
            x = i+1
        oplossing = nieuwe_lijst + lijst_2[x:]
    else:
        oplossing = lijst_2
    return oplossing


print(splits_kaartspel(['blad 1', 'blad 2', 'blad 3', 'steen 1', 'steen 2', 'steen 3', 'schaar 1', 'schaar 2', 'schaar 3']))