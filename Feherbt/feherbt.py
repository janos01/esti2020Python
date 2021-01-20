import mariadb

config = {
	'host': 'localhost',
	'user': 'feherbt',
	'password': 'titok',
}

sqlInsert = """
insert into employees
(name, city, salary)
values
(?,?,?)
"""

sqlQuery = """
select *
from employees
"""
employee = ('Tangó Katalin', 'Miskolc', 7350000)

def connect():
	conn = mariadb.connect(**config, database='feherbt')
	return conn 

def getEmployees(conn):
	cur = conn.cursor()
	cur.execute(sqlQuery)
	for (id, name, city, salary) in cur:
		print(f"{name}\t{salary}")

def insertEmployee(conn, employee):
	cur = conn.cursor()	
	cur.execute(sqlInsert, employee)
	conn.commit()

conn = connect()
insertEmployee(conn, employee)
getEmployees(conn)
conn.close()
