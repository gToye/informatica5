def palindroom(woord):
    index = 0
    while woord[i] == woord[-i-1] and i < len(woord)//2:
        index += 1

    return i == len(woord)//2  