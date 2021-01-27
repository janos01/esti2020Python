# Nagy János, 2021-01-27

def vizsgalSzam(szoveg) :
    if szoveg.isdigit() :
        return True
    else:
        return False



if __name__ == "__main__":
    print('Nagy János, 2021-01-27')
    print(vizsgalSzam('34344'))
    print(vizsgalSzam('34344aa'))
