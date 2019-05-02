def hint(gok1,woord):
    taal = gok1
    taal_2 = woord
    if taal == taal_2:
        return taal.upper()
    letter_1 = taal[0]
    letter_2 = taal[1]
    letter_3 = taal[2]
    letter_4 = taal[3]
    letter_5 = taal[4]
    a = ''
    b = ''
    c = ''
    d = ''
    e = ''


    #letter_1
    if taal.find(taal_2[0]) != -1:

        if taal.find(taal_2[0]) == 0:
            a = letter_1.upper()
        else:
            a = taal[taal.find(taal_2[0])]
    else:
        a = '.'
    #letter_2
    if taal.find(taal_2[1]) != -1:

        if taal.find(taal_2[1]) == 1:
             b = letter_2.upper()
        else:
             b = taal[taal.find(taal_2[1])]
    else:
        b = '.'

    if taal.find(taal_2[2]) != -1:

        if taal.find(taal_2[2]) == 2:
             c = letter_3.upper()
        else:
             c = taal[taal.find(taal_2[2])]
    else:
        c = '.'

    if taal.find(taal_2[3]) != -1:
        if taal.find(taal_2[3]) == 3:
             d = letter_4.upper()
        else:
             d = taal[taal.find(taal_2[3])]
    else:
        d = '.'

    if taal.find(taal_2[4]) != -1:

        if taal.find(taal_2[4]) == 4:
             e = letter_5.upper()
        else:
             e = taal[taal.find(taal_2[4])]
    else:
        e = '.'

    return taal[taal.find(taal_2[4])]
    return a+b+c+d+e

print(hint('spoed','depri'))