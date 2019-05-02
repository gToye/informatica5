def fruitstuk_toevoegen(mand,fruitstuk):
    nieuwe_mand = []
    if mand.count(fruitstuk) > 0:
        oplossing = mand
    else:
        nieuwe_mand.append(fruitstuk)
        for i in range(len(mand)):
         if len(mand[i]) == len(fruitstuk):
            mand.remove(mand[i])
    oplossing = mand + nieuwe_mand
    oplossing.sort(key=len)
    return oplossing
def maak_fruitmand(fruit):
    nieuwe_mand = []
    wegdoen = 0
    for i in range(len(fruit)):
        if fruit.count(fruit[i]) == 1:
            nieuwe_mand.append(fruit[i])

        else:
            wegdoen += 1
    if wegdoen == len(fruit):
        nieuwe_mand.append(fruit[0])
    nieuwe_mand.sort(key=len)
    for i in range(len(nieuwe_mand) - 1):
        if i != len(nieuwe_mand) -1:
            if len(nieuwe_mand[i]) == len(nieuwe_mand[i+1]):
                nieuwe_mand.remove(fruit[i+1])

        else:
            if len(nieuwe_mand[i]) == len(nieuwe_mand[0]):
                nieuwe_mand.remove(fruit[i])
    return nieuwe_mand


print(maak_fruitmand(['peer', 'kiwi','ananas', 'aardbei', 'framboos']))