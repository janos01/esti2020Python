#  Nagy János, 2020-11-11, esti

import math

print('Nagy János, 2020-11-11, esti')
print('A 0312 feladat megoldása')
print('Egy rombuszba írható kör sugarának számítása')
print('---------------------------------------------')
print()

oldal = float(input('Oldal: '))
alfa = float(input('Alfa szög: '))
rad = alfa * math.pi / 180
sugar = 1.0/2.0 * oldal * math.sin(rad)

print("Sugár: ", sugar)
