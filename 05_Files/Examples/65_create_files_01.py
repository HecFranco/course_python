def crear_archivo():
  # r read and w write 
  archivo = open('./05_Files/Examples/datos.txt', 'w')
  archivo.close() # cerramos el archivo


crear_archivo()