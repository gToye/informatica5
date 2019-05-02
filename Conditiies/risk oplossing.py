worp_1a = int(input('worp 1 aanvaller: '))
worp_2a = int(input('worp 2 aanvaller: '))
worp_3a = int(input('worp 3 aanvaller: '))
worp_4b = int(input('worp 4 aanvaller: '))
worp_5b = int(input('worp 5 aanvaller: '))
#sorteren
sa2 = max(worp_3a,worp_2a, worp_1a)
sa1 = min(worp_1a, worp_2a, worp_3a)
middel = worp_1a + worp_2a + worp_3a - sa1 + sa2

sv1 = min( worp_4b, worp_5b)
sv2 = max(worp_4b, worp_5b)
#winnaar bepalen
if sa2 > sv2 and middel > sv1:
    mes = 'aanvaller verliest 0 legers, verdediger verliest 2 legers'
elif sv1 >= middel and sv2 >= sa2:
    mes = 'aanvaller verliest 2 lelgers, verdediger verliest 0 legers'
else: mes = 'aanvaller verliest 1 leger,verdediger verliest 1 leger'
#uitvoer
print(mes)