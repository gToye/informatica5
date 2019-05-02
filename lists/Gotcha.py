def ik_heb_gemoord(spelers,ik):
    if len(spelers) != 1:
        if ik != spelers[-1]:
            spelers.remove(spelers[spelers.index(ik)+1])
            nieuwe_list = spelers

        else:
            spelers.remove(spelers[0])
            nieuwe_list = spelers
            volgende = spelers[0]
        if ik != nieuwe_list[-1]:
            volgende = nieuwe_list[nieuwe_list.index(ik) +1]
        else:
            volgende = nieuwe_list[0]
    else:
        nieuwe_list = spelers
        volgende = ik


    return (volgende,nieuwe_list)
def ik_ben_vermoord(spelers,ik):

        if len(spelers) != 1:
            moordenaar = spelers[spelers.index(ik) -1]
            if ik != spelers[0]:
                spelers.remove(ik)
                nieuwe_list = spelers

            else:
                spelers.remove(spelers[0])
                nieuwe_list = spelers
                volgende = spelers[0]
            if moordenaar != nieuwe_list[-1]:
                volgende = nieuwe_list[spelers.index(moordenaar) + 1]
            else:
                volgende = nieuwe_list[0]
        else:
            nieuwe_list = spelers
            volgende = ik

        return  (volgende,nieuwe_list)




print(ik_ben_vermoord(['jan', 'piet', 'joris'],'joris'))
##############################################################################################################################################################
def ik_heb_gemoord(lijst,moordenaar):
    index_moordenaar = lijst.index(moordenaar)
    index_slachtoffer = (index_moordenaar+1) % len(lijst)
    lijst[index_slachtoffer:index_slachtoffer+1]= []
    index_nieuw_doel = (index_moordenaar+1)% len(lijst)
    return lijst,index_nieuw_doel
