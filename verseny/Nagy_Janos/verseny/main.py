# Nagy János, 2021-02-24, 2/24 Szoft

from verseny import Verseny

def about():
     print('Nagy János, 2021-02-24, 2/24 Szoft')
# coding: utf8

def loadFile():
    versenyek = []
    fp = open('versenyek.txt', 'r', encoding='utf-8')
    
    lines = fp.readlines()
    
    for line in lines[1:]:
        line = line.rstrip()
        az, nev, helyszin, datum, helyezes = line.split(':')
        versenyek.append(Verseny(az, nev, helyszin, datum, helyezes))
    fp.close()
    return versenyek

def feladat2(versenyek):
    print('Feladat 2')
    darab = 0
    for verseny in versenyek:
        if verseny.az == '5':
            darab += 1
    print('Az 5 versenyző ennyi versenyen volt: ' + str(darab))

def feladat3(versenyek):
    print('Feladat 3')
    darab = 0
    for verseny in versenyek:
        if verseny.datum == '2020-03-11' and verseny.helyszin == 'Kaposvár' :
            darab += 1            
    print('Kaposvári, 2020-03-11-i versenyen részt vettek: ' + str(darab))

def feladat4(versenyek):
    print('Feladat 4')
    print('Fehér Erik versenyei')
    print('{:12}{:12}{:8}'.format('Helyszín', 'Időpont', 'Helyezés'))
    for verseny in versenyek:
        if verseny.nev == 'Fehér Erik':
            print(
                '{:12}{:12}{:8}'.format(
                verseny.helyszin, 
                verseny.datum, 
                verseny.helyezes
                ))

def feladat5(versenyek):
    print('Feladat 5')
    legjobbEredmeny = versenyek[0]
    for verseny in versenyek:
        if verseny.helyezes < legjobbEredmeny.helyezes:
            legjobbEredmeny = verseny
    print('Legjobb eredmény: ', 
        legjobbEredmeny.nev,
        legjobbEredmeny.helyezes,
        legjobbEredmeny.helyszin)

# Ha az összes legjobbat ki kell íratni:
def feladat5_2(versenyek):
    print('Feladat 5')
    legjobbEredmeny = versenyek[0]
    for verseny in versenyek:
        if verseny.helyezes < legjobbEredmeny.helyezes:
            legjobbEredmeny = verseny
    legjobbHelyezes = legjobbEredmeny.helyezes
    for verseny in versenyek:
        if verseny.helyezes == legjobbHelyezes:
            print('Legjobb eredmény: ', 
                verseny.nev,
                verseny.helyezes,
                verseny.helyszin)

def feladat6(versenyek):
    print('Feladat 6')
    for verseny in versenyek:
        if verseny.az == '15':
            print(verseny.helyszin, verseny.datum)

# Milyen helyszíneken volt verseny?
# Egy település csak egyszer szerepeljen.
def feladat7(versenyek):
    print('Feladat 7')
    helyszinek = []
    for verseny in versenyek:
        if verseny.helyszin not in helyszinek:
            helyszinek.append(verseny.helyszin)
    for helyszin in helyszinek:
        print(helyszin)

# Hány helyszínen volt verseny?
def feladat8(versenyek):
    print('Feladat 8')
    helyszinek = []
    darab = 0    
    for verseny in versenyek:
        if verseny.helyszin not in helyszinek:
            helyszinek.append(verseny.helyszin)
            darab += 1
    print('Helyszínek száma: ', str(darab))


# ~ about()
versenyek = loadFile()
# ~ feladat2(versenyek)
# ~ feladat3(versenyek)
# ~ feladat4(versenyek)
# ~ feladat5_2(versenyek)
# ~ feladat6(versenyek)
# ~ feladat7(versenyek)
feladat8(versenyek)

