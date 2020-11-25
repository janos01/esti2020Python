import random

class Jatekos:    
    def __init__(self):
        self.nev = 'Névtelen'
        self.dobasok = []
    
    def dobas(self):
        for i in range(5):     
            dob = random.randrange(1, 6)
            self.dobasok.append(dob)

    def kiir(self):
        print(self.nev, ': ', end='')
        for dob in self.dobasok:
            print(dob, end=' ')
        print()

ember = Jatekos()
ember.nev = 'Human'
ember.dobas()
ember.kiir()

gep = Jatekos()
gep.nev = 'Machine'
gep.dobas()
gep.kiir()
