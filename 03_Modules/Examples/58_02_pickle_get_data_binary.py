import pickle
fichero = open('lista.pckl','rb') # Lectura en modo binario
lista_fichero = pickle.load(fichero)
print(lista_fichero)
# [1, 2, 3, 4, 5]