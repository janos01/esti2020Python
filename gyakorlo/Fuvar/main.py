from fuvar import Fuvar
import datetime

def fajl_beolvas():
    fuvarok = []
    fp = open('fuvar.csv', 'r', encoding='utf-8')
    lines = fp.readlines()
    
    for line in lines[1:]:
        nline = line.rstrip()
        (taxi_id, indulas, 
            idotartam, tavolsag, viteldij,
            borravalo, fizetes_modja) = nline.split(';')
        fuvar = Fuvar(taxi_id, indulas, 
            idotartam, tavolsag, viteldij,
            borravalo, fizetes_modja)
        fuvarok.append(fuvar)
        # ~ print(fuvar.indulas)
    fp.close()
    return fuvarok

def feladat3(fuvarok):
    print('3. feladat: ', end='')
    fuvarok_szama = len(fuvarok)
    print(fuvarok_szama, ' fuvarok')

def feladat4(fuvarok):
    print('4. feladat: ', end='')
    szamlalo = 0
    osszeg = 0
    for fuvar in fuvarok:
        if fuvar.taxi_id == '6185':
            szamlalo += 1
            viteldijStr = fuvar.viteldij
            viteldijStr = viteldijStr.replace(',', '.')
            osszeg += float(viteldijStr)
    print(szamlalo, 'fuvar alatt: ', end='')
    print(osszeg, '$', sep='')

def feladat5(fuvarok):
    print('5. feladat:')
    bankkartya = 0
    keszpenz = 0
    vitatott = 0
    ingyenes = 0
    ismeretlen = 0
    for fuvar in fuvarok:
        if fuvar.fizetes_modja == 'bankkártya':
            bankkartya += 1
        elif fuvar.fizetes_modja == 'készpénz':
            keszpenz += 1
        elif fuvar.fizetes_modja == 'vitatott':
            vitatott += 1
        elif fuvar.fizetes_modja == 'ingyenes':
            ingyenes += 1
        elif fuvar.fizetes_modja == 'ismeretlen':
            ismeretlen += 1
    
    print('\tbankkártya: ', bankkartya, 'fuvar' )
    print('\tkészpénz: ', keszpenz, 'fuvar' )
    print('\tvitatott: ', vitatott, 'fuvar' )
    print('\tingyenes: ', ingyenes, 'fuvar' )
    print('\tismeretlen: ', ismeretlen, 'fuvar' )
    
def feladat6(fuvarok):
    print('6. feladat:', end='')
    merfoldek = 0
    for fuvar in fuvarok:
        merfoldStr = fuvar.tavolsag
        merfoldStr = merfoldStr.replace(',', '.')
        merfoldek += float(merfoldStr)
        kilometerek = merfoldek * 1.6
    print(" %.2fkm" % kilometerek)

def feladat7(fuvarok):
    print('7. feladat: Leghosszabb fuvar')
    max_fuvar = fuvarok[0]
    for fuvar in fuvarok:
        if int(fuvar.idotartam) > int(max_fuvar.idotartam):
            max_fuvar = fuvar
    print('\tFuvar hossza:', max_fuvar.idotartam, 'másodperc')
    print('\tTaxi azonosító:', max_fuvar.taxi_id)
    print('\tMegtett távolság:', max_fuvar.tavolsag, 'km')
    print('\tViteldíj: ', max_fuvar.viteldij, '$', sep='')

def feladat8(fuvarok):
    print('8. feladat: ', end='')
    hibasak = []    
    for fuvar in fuvarok:
        if (fuvar.tavolsag == '0,0' and 
            fuvar.viteldij != '0,0'
            ):
            hibasak.append(fuvar)
    
    n = len(hibasak)
    for i in range(n-1, 0, -1):
        for j in range(0, i):
            jido = datetime.datetime.fromisoformat(hibasak[j].indulas)
            pido = datetime.datetime.fromisoformat(hibasak[j+1].indulas)
            if jido > pido:
                tmp = hibasak[j]
                hibasak[j] = hibasak[j+1]
                hibasak[j+1] = tmp

    fajlnev = 'hibak.txt'
    fp = open(fajlnev, 'w', encoding='utf-8')
    for hibas in hibasak:
        line = (
            hibas.taxi_id + ";" +
            hibas.indulas + ";" +
            hibas.idotartam + ";" +
            hibas.tavolsag + ";" +
            hibas.viteldij + ";" +
            hibas.borravalo + ";" +
            hibas.fizetes_modja + "\n"
        )
        fp.write(line)
    fp.close()
    print(fajlnev)


fuvarok = fajl_beolvas()
feladat3(fuvarok)
feladat4(fuvarok)
feladat5(fuvarok)
feladat6(fuvarok)
feladat7(fuvarok)
feladat8(fuvarok)


