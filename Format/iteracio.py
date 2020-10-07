

# Számok bekérése 0 végjelig
# Adja össze a bekért számokat

osszeg = 0
szam = -1
while szam != 0 :
    szam = int(input('Szám: '))
    osszeg = osszeg + szam

print('Összeg: {}'.format(osszeg))
