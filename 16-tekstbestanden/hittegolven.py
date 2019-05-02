temperatuur = []
with open('temperaturen.txt') as bestand:
    temperatuur = bestand.readlines()
temp_25 = 0
temp_30 = 0
hittegolven = 0
for i in range(len(temperatuur)):
    if temp_25 >= 5 and temp_30 >= 2:
        hittegolven += 1
        temp_25 = 0
        temp_30 = 0
    if temperatuur[i] >= 30:
        temp_30 += 1

    if temperatuur[i] >= 25:
        temp_25 += 1
        if temp_25 >= 5 and temp_30 >= 2:
            hittegolven += 1
            temp_25 = 0
            temp_30 = 0
    if temperatuur[i] < 25:
        temp_25 = 0
        temp_30= 0

print(hittegolven)