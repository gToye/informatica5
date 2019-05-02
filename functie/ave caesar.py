#def is letter
def is_letter(l):
    if l in 'abcdefghijklmnopqrstuvwxyz'  or l in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        return True

    else:
        return False
#def roteer letter
def roteer_letter(x, y):
    if x in 'abcdefghijklmnopqrstuvwxyz':
        if (ord(x) + y) > ord('z'):
            k = (ord(x) + y) - ord('z')
            letter = chr(ord('a') - 1 + k)
        else:
            letter = chr(ord(x) + y)
    else:
        if (ord(x) + y) > ord('Z'):
            k = (ord(x) + y) - ord('Z')
            letter = chr(ord('A') - 1 + k)
        else:
            letter = chr(ord(x) + y)
    return letter
#def versleutel
def versleutel(x, y):
    bericht = x
    bericht_2 = ''
    for letter in bericht:
        if is_letter(letter) == True:
            nieuwe_letter = roteer_letter(letter, y)
            bericht_2 += nieuwe_letter
        else:
            bericht_2 += letter
    return bericht_2
