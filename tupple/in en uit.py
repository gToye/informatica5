from math import sqrt
def binnen_of_buiten(m,c,p):
    straal = sqrt(((m[0]-c[0])**2)+(m[1]-c[1])**2)
    d_mp = sqrt(((m[0]-p[0])**2)+((m[1]-p[1])**2))
    if straal == d_mp:
        return('op',round(d_mp,4))
    elif straal >= d_mp:
        return('binnen',round(d_mp,4))
    else:
        return('buiten',round(d_mp,4))

print(binnen_of_buiten((17, 31),(-10, 6),(-6, 26)))