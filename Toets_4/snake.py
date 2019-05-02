def beweeg(plaats,zetten):
    x = plaats[0]
    y = plaats[1]
    if zetten == '<' or zetten == '>':
        if zetten == '>':
            x += 1
        else:
            x -= 1
    else:
        if zetten == '^':
             y += 1
        else:
             y -= 1

    return x,y


def teruggekeerd(beweging):
    g1 = beweging[0]
    g2 = beweging[1]
    if (g2 == '>' and g1 =='<') or (g1 == '>' and g2=='<'):
        return True
    elif (g1 == '^' and (g2 != '<' and g2 != '>' and g2 != '^' )) or (g2 == '^' and (g1 != '<' and g1 != '>' and g1 != '^' )):
        return True
    else:
        return False


def laatste_levende_positie(zetten):
    geldige_zetten = 0
    x = 0
    y = 0

    for i in range(len(zetten)):
        if zetten[i] != zetten[0] :
            if teruggekeerd([zetten[i],zetten[i-1]]) == False:

                geldige_zetten += 1
                if zetten[i] == '<':
                    x -= 1
                elif zetten[i] == '>':
                    x += 1
                elif zetten[i] == '^':
                    y += 1
                else:
                    y -= 1
            else:
                return geldige_zetten, x, y
        else:
            geldige_zetten += 1
            if zetten[i] == '<':
                x -= 1
            elif zetten[i] == '>':
                x += 1
            elif zetten[i] == '^':
                y += 1
            else:
                y -= 1

    return geldige_zetten, x, y


print(laatste_levende_positie(['v', '>', 'v', '<', '^', '^']))



