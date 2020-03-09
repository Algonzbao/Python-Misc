import sqlite3

miConexion = sqlite3.connect("PrimeraBase")
miCursor = miConexion.cursor()

#CREAR E INTRODUCIR DATO
#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")
#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON', 15, 'DEPORTES')")
#variosProductos = [
   # ("Camiseta", 10, "Deportes"),
   # ("Jarron", 90, "Cerámica")
#]
#miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)
#_________________________________________________________________________________________________--
#SELECCIONAR

miCursor.execute("SELECT * FROM PRODUCTOS")
variosProductos = miCursor.fetchall()
for producto in variosProductos:
    print(producto[0])

miConexion.commit()