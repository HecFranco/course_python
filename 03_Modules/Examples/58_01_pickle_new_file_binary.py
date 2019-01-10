import pickle
lista = [1,2,3,4,5] # Podemos guardar lo que queramos, listas, diccionarios, tuplas...
fichero = open('lista.pckl','wb') # Escritura en modo binario, vacía el fichero si existe
pickle.dump(lista, fichero) # Escribe la estructura en el fichero 
fichero.close()