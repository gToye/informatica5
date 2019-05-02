def germaniseer(zin):
    #alle letters overlopen
    for i in range(0,len(zin) - 1):
        if zin[i] == ' ':
            zin = zin[0:i+1]+ zin[i+1].upper()+zin[i+2:]
    return zin
print(germaniseer('Geluk helpt soms, moed altijd.'))