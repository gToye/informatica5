def hoogtemeters(hoogtes):
    lijst = []
    for i in range(len(hoogtes)-1):
            verschil = hoogtes[(i+1)] - hoogtes[i]
            lijst.append(verschil)
    return lijst

def dalen_en_stijgen(hoogtes):
    dalen = 0
    stijgen = 0

    for i in range(len(hoogtes)):
        if hoogtes[i] > 0:
            stijgen += hoogtes[i]
        else:
            dalen += hoogtes[i]

    return (-dalen , stijgen)
print(dalen_en_stijgen([-761, 286, -113, 649, -547]))