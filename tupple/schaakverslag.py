def geldige_zet(zet):
    if len(zet) == 3 and ord(zet[0]) >= 96:
        mes = True

    elif len(zet)==2 and ord(zet[1]) >= 96:
        mes = True
    else:
        mes = False
    return mes

def geldige_zetten(zetten):
    n = 0
    for i in range (len(zetten)):
        if ord((zetten[i])[0]) >= 96:
            n += 1
        elif ord((zetten[i])[1]) >= 96:
            n += 1
        else:
            n+= 0
    if n == len(zetten):
        mes = True
    else:
        mes = False

    return mes


print(geldige_zetten(('Ta1', 'Kf4', 'ZBECF', 'h7', 'e2', 'HNJHD', 'Ph6')))