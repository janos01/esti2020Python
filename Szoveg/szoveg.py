

szoveg = 'alma '

print(szoveg.rstrip() + 'fa')

print('Hossz: ', len(szoveg))

fajlSor = '35,Nagy Béla,3850000'
tombSor = fajlSor.split(',')
print('Név: ', tombSor[1])

if 'Béla' in fajlSor:
    print('A sorban van Béla')

ujFajlSor = fajlSor.replace(',', ':')
print(ujFajlSor)

for karakter in ujFajlSor:
    print(karakter, end=' ')

lista1 = ['a', 'b', 'c']
str1 = ''.join(lista1)
print('\n------------------------')
print(lista1)
print(str1)
print(type(lista1))
print(type(str1))












