#  Nagy János, 2020-11-11, esti szoft

import math

print('Nagy János, 2020-11-11, esti')
print('A 0415 feladat megoldása')
print('Oszthatóság vizsgálata')
print('---------------------------------------------')
print()

egeszSzam = int(input('Egész szám: '))

if (egeszSzam % 2 == 0) and (egeszSzam % 3 == 0):
    print('Osztható 2-vel és 3-mal')
elif egeszSzam % 2 == 0:
    print('Osztható 2-vel')
elif egeszSzam % 3 == 0:
    print('Osztható 3-mal')
else:
    print('Sem 2-vel, sem 3-mal nem osztható')
