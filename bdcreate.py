import sqlite3
conn = sqlite3.connect('churrinche.db')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE T_Config (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Nombre TEXT NOT NULL,
	Valor TEXT)
''')
###------------------T_Config-----------------------
### CARGA DATOS EN TABLA T_Manejo ###
# Larger example that inserts many records at a time
configs = [('wifi','True'),
            ('bt','False'),]
print(configs)
c.executemany('INSERT INTO T_Config(Nombre, Valor) VALUES (?,?)', configs)
### LEE LOS DATOS EN LA TABLA T_Atributos ###

for row in c.execute('SELECT * FROM T_Config'):
    print row
###------------------------------------------------------


#Imprimir tablas en la base y su disenio
c.execute("select name from sqlite_master where type = 'table' and name <> 'sqlite_sequence'")
registros = c.fetchall()
for registro in registros:
	print registro
print
c.execute("select sql from sqlite_master where type = 'table' and name <> 'sqlite_sequence'")
registros1 = c.fetchall()
for registro1 in registros1:
	print registro1
	print

	
	
# Insert a row of data
#c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()



# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()