# python 60_To_Work_02.py inc
# python 60_To_Work_02.py dec
# cambiamos el contenido a no integer y ejecutamos python 60_To_Work_02.py dec
from io import open
import sys

fichero = open("contador.txt", "a+") 
fichero.seek(0)
contenido = fichero.readline()

if len(contenido) == 0:
    contenido = "0"
    fichero.write(contenido)

fichero.close()

# Vamos a intentar transformar el texto a un número
try:
    contador = int(contenido)

    # En función de lo que el usuario quiera...
    if len(sys.argv) == 2:
        if sys.argv[1] == "inc":
            contador += 1
        elif sys.argv[1] == "dec":
            contador -= 1

    print(contador)

    # Finalmente volvemos a escribir los cambios en el fichero
    fichero = open("contador.txt", "w")
    fichero.write( str(contador) )
    fichero.close()

except:
    print("Error: Fichero corrupto.")