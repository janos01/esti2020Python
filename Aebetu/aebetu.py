#  Nagy János, 2020-11-11, esti szoft

print('Nagy János, 2020-11-11, esti')
print('A 1058 feladat megoldása')
print('Szövegben a és e betű számolása')
print('---------------------------------------------')
print()

szoveg = input('Írjon be egy szöveget: ')

aSzamlalo = 0
eSzamlalo = 0
for karakter in szoveg:
    if karakter == "a":
        aSzamlalo += 1
    if karakter == "e":
        eSzamlalo += 1

print('a betűk száma: ', aSzamlalo)
print('e betűk száma: ', eSzamlalo)
