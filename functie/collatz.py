def volgend_collatz_getal(n):
    getal = 0
    if n % 2 == 0:
        getal += n / 2
    else:
        getal += (3*n)+1
        return getal
def collatz(n):
    lengte = 0
    if n == 1:
        lengte += 1
    else:
        lengte == collatz(volgend_collatz_getal(n))
    return lengte