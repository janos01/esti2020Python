

lista = [85, 27, 12, 43, 58]
print(lista)
lista[2] = 89
print(lista)
print(lista[0])

lista2 = [8, 2, 3, 5, 6]
lista3 = [85, 27, 12, 43, 58]

lista4 = lista

if lista3 is lista4:
    print('egyenlő')
else:
    print('nem egyenlő')

print(lista4)

print(lista2 + lista3)

for szam in lista2:
    print(szam)

valosSzamok = [3.5, 4.6, 5.8 ]
szovegLista = ['alma', 'körte']

szovegLista.append('szilva')
szovegLista.insert(1, 'barack')
szovegLista.remove('alma')
print(szovegLista)
print(szovegLista.index('szilva'))
szovegLista.clear()
print(szovegLista)

lista5 = lista.copy()

if lista5 is lista:
    print('egyenlő')
else:
    print('nem egyenlő')
    
egyLista = list((45, 65, 75))




