import sqlite3

conn = sqlite3.connect('test.db')
cur = conn.cursor()

def lekerDolgozok():
    sql='select * from dolgozok'    
    cur.execute(sql)
    dolgozok = cur.fetchall()
    for dolgozo in dolgozok:
        print(dolgozo[1])


def lekerDolgozoTelepulesbol(telepules):
    sql='select * from dolgozok where telepules="'+ telepules+ '"'    
    cur.execute(sql)
    dolgozo = cur.fetchone()
    print(dolgozo)
        

def beszurDolgozo(nev, telepules, fizetes):
    sql='''
    insert into dolgozok
    (nev, telepules, fizetes)
    values
    (?,?,?)
'''
    cur.execute(sql, [nev, telepules, fizetes])
    conn.commit()

# ~ nev = input('Név: ')
# ~ telepules = input('Település: ')
# ~ fizetes = input('Fizetés: ')
# ~ beszurDolgozo(nev, telepules, fizetes)
lekerDolgozok()
lekerDolgozoTelepulesbol('Hatvan')






