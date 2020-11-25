
class Dolgozo:
    def munka(self):
        print('ások')

class Mernok(Dolgozo):
    def munka(self):
        print('mér')
    
    def asas(self):
        super().munka()

joska = Dolgozo()    
joska.munka()

mari = Mernok()
mari.asas()
    
