
def vlag(richting,kleur):


    if richting == 'verticaal':
        mes = ''
        for i in range (0,len(kleur)-1):

            mes += kleur[i] + ' | '
        mes += kleur[-1]

    if richting == 'horizontaal':
        mes = ''
        for i in range(0,len(kleur)-1):
            mes += kleur[i] + '\n' + '-' + '\n'
        mes += kleur[-1]

    return  mes
print(vlag('verticaal',('zwart','geel','rood')))