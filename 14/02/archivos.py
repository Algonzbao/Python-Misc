from io import open
archivo = open("../archivo.txt", "r")
lineas_texto = archivo.readlines()
archivo.close()
print(lineas_texto[2])