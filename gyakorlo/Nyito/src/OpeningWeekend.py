
from Film import Film
from Forgalmazo import Forgalmazo
import datetime

def fajl_beolvas():
    filmek = []
    fp = open('nyitohetvege.txt', 'r', encoding='utf-8')
    lines = fp.readlines()
    fp.close()
    for line in lines[1:]:
        n_line = line.rstrip()
        (eredetiCim, magyarCim,bemutato,forgalmazo,
            bevel,latogato) = n_line.split(';')
        film = Film(eredetiCim, magyarCim,bemutato,forgalmazo,
            bevel,latogato)
        filmek.append(film)
    return filmek

def feladat3(filmek):
    print('3. feladat: Filmek száma az állományban: ', end='')
    filmek_szama = len(filmek)
    print(filmek_szama, 'db')

def feladat4(filmek):
    print('4. feladat: UIP Duna Film forgalmazó 1. ', end='')
    print('hetes bevételeinek összege: ', end='')
    osszeg=0
    for film in filmek:
        if film.forgalmazo == 'UIP':
            osszeg+=int(film.bevel)
    print("{:,}".format(osszeg), 'Ft')
    
def feladat5(filmek):
    print('5. feladat: Legtöbb látogató az első héten:')
    max_film = filmek[0]
    for film in filmek:
        if int(film.latogato) > int(max_film.latogato):
            max_film = film

    print('\tEredeti cím:', max_film.eredetiCim)
    print('\tMagyar cím:', max_film.magyarCim)
    print('\tForgalmazó:', max_film.forgalmazo)
    print('\tBevétel az első héten:', max_film.bevel, 'Ft')
    print('\tLátogatók száma:', max_film.latogato, 'fő')

def tartalmazTeszt(eredetiCim, magyarCim):
    eredetiTartalmaz=False
    if 'W' in eredetiCim:
        eredetiTartalmaz=True
    if 'w' in eredetiCim:
        eredetiTartalmaz=True
    magyarTartalmazza=False
    if 'W' in magyarCim:
        magyarTartalmazza=True
    if 'w' in magyarCim:
        magyarTartalmazza=True

    if eredetiTartalmaz and magyarTartalmazza:
        return True
    else:
        return False        

def feladat6(filmek):
    print('6. feladat: ', end='')
    
    n=len(filmek)
    i=0
    while (i<n and 
        not tartalmazTeszt(filmek[i].eredetiCim, filmek[i].magyarCim)):
        i+=1
    if i<n:
        print("Ilyen film volt!")
    else:
        print("Ilyen film nem volt!")

def forgalmazoTeszt(forgalmazok, forgalmazo):
    n=len(forgalmazok)
    i=0
    while i<n and forgalmazok[i].nev != forgalmazo:
        i+=1
    if i<n:
        return True
    else:
        return False

def feladat7(filmek):
    mezonevek = 'forgalmazo;filmekSzama\n'
    forgalmazok = []
    for film in filmek:
        if not forgalmazoTeszt(forgalmazok, film.forgalmazo):
            forgalmazo = Forgalmazo(film.forgalmazo)
            forgalmazok.append(forgalmazo)
        else:
            n=len(forgalmazok)
            for i in range(0, n):
                if forgalmazok[i].nev == film.forgalmazo:
                    forgalmazok[i].filmek += 1    
    fp = open('stat.csv', 'w', encoding='utf-8')
    fp.write(mezonevek)
    for forgalmazo in forgalmazok:
        if forgalmazo.filmek>1:
            fp.write(forgalmazo.nev + ';' + str(forgalmazo.filmek) + '\n')
    fp.close()

def feladat8(filmek):
    print('8. feladat: A leghosszabb időszak két ', end='')
    print('InterCom-os bemutató között: ', end='')
    
    elsoBemutato = None
    max_kul = 0
    for film in filmek:
        if film.forgalmazo == 'InterCom':
            isoDatum = film.bemutato.replace('.', '-')
            if elsoBemutato == None:
                elsoBemutato=datetime.date.fromisoformat(isoDatum)
            else:
                kovBemutato = datetime.date.fromisoformat(isoDatum)
                kul = kovBemutato - elsoBemutato
                if kul.total_seconds() > max_kul:
                    max_kul=kul.total_seconds() 
                elsoBemutato = kovBemutato
    nap = max_kul  // (24 * 3600)
    print(int(nap), 'nap')

filmek = fajl_beolvas()
# ~ feladat3(filmek)
# ~ feladat4(filmek)
# ~ feladat5(filmek)
# ~ feladat6(filmek)
# ~ feladat7(filmek)
feladat8(filmek)

