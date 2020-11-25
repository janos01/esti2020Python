
fp = open('dolgozo.txt', 'w')

dolgozNev = ''
while dolgozNev != 'vege':
    dolgozNev = input('A dolgozó neve: ')
    if dolgozNev != 'vege':
        fp.write(dolgozNev)
        fp.write('\n')

fp.close()
