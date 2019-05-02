n = int(input('hoeveel lifters zijn er?'))
a = 0
for x in range(0,(n//2)):
    antwoord = (input('wat is de score'))
    maximum = max(antwoord,a)
maximum_2 = max(maximum,a)
print(maximum_2)
for y in range(n//2,n):
    antwoord_2 = (input('wat is de score'))
if antwoord_2 >= maximum:
    print(antwoord_2)
else:
    print(maximum)
