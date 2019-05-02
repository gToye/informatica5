def ontdubbelen(woord):

    nieuw_woord = ''
    for i in range(len(woord)-1):
        if woord[i] != woord[i+1]:
            nieuw_woord += woord[i]
    nieuw_woord += woord[-1]
    return nieuw_woord
print(ontdubbelen('grootte'))