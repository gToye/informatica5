def vergeten_woorden(tekst,verplicht):
    woorden = set(tekst.split())
    aantal_verplicht = len(verplicht)
    aantal_vergeten =  len(verplicht.difference(woorden))
    aantal_juist = aantal_verplicht - aantal_vergeten
    return (aantal_verplicht,aantal_vergeten,aantal_juist)

print(vergeten_woorden('hello world world world',{'python', 'world', 'hello', 'java'}))