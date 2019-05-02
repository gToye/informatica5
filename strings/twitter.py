taal = input('Wat is de twitter tekst?')
woord = taal.find('#')
print(taal[taal.find('#')+1:taal.find(' ')])