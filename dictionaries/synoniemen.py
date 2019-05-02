def synoniemen(zin, synoniemen):
    zin = zin.split()
    for i in range(len(zin)):
        if zin[i] in synoniemen:
            zin[i] = synoniemen.get(zin[i])

    zin = ' '.join(zin)
    return zin

