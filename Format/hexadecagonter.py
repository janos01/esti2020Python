import math
print('Sallai András', end=',')
print('esti 2/14 szoft', end=',')
print('2020-10-07')
print('Hexadecagon területszámítás')

oldal = float(input('Oldal: '))

rad = math.pi/16
a = math.cos(rad)
b = math.sin(rad)
c = a/b

t=4*math.pow(oldal,2)*c

print('Terület: {:5.2f}'.format(t))
