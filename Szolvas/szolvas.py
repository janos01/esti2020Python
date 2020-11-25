
fp = open('adat.txt', 'r')

while 1:
    line = fp.readline()
    if line == '':
        break
    
    tomb = line.split(':')
    fizetes = tomb[3];
    fizetes = fizetes.rstrip();
    if (fizetes == "1450000"):
        print('van ilyen')
    print(fizetes)
fp.close()


