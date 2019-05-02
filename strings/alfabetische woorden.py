def positie_laagste_ascii(tekst):

    p_laagste = 0
    ord_laagste = ord(tekst[0])
    for i in range(1,len(tekst)):
        if(ord(tekst[i]) < ord_laagste):
            p_laagste= i
            ord_laagste = ord(tekst[i])

    return p_laagste

def sorteer(woord):
    s_woord = ''
    while len(woord) > 0:
        i = positie_laagste_ascii(woord)
        s_woord += woord[i]
        woord = woord[:i] + woord[i+1:]
    return s_woord
print(sorteer('vincent.vangogh@gmail.com'))
def is_alfabetisch(tekst):
    return tekst == sorteer(tekst)