def crear_archivo():
  # r read and w write 
  archivo = open('./05_Files/Examples/datos.txt', 'w')
  archivo.close() # cerramos el archivo

def escribir_archivo():
  archivo = open('./05_Files/Examples/datos.txt', 'a')
  archivo.write('Primera línea\n')
  archivo.write('Segunda línea')
  archivo.close()

def leer_archivo():
  archivo = open('./05_Files/Examples/datos.txt', 'r')
  linea = archivo.readline()
  while linea != "":
    print (linea)
    linea = archivo.readline()
  archivo.close()


crear_archivo()
escribir_archivo()
leer_archivo()