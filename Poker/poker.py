# Nagy János, 2020-11-18
import random

def jatekosDobas():
    dobasok = [];
    for i in range(5):
        vel = random.randrange(6) + 1
        dobasok.append(vel)
    dobasok.sort()
    return dobasok

def kiirDobasok(dobasok, nev):
    print('{:10}: '.format(nev), end='')
    for elem in dobasok:
        print(elem, end=' ')
    print()

print('Nagy János, 2020-11-18')
print('Póker')
print('--------------------')

emberDobasok = jatekosDobas()
gepDobasok = jatekosDobas()

kiirDobasok(emberDobasok, "Ember")
kiirDobasok(gepDobasok, "Gép")
