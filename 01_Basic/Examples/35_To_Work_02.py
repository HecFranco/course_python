# Completa el ejercicio aquí
lista = [1, 2, 3, 4, 5]
try:
    lista[10]
except IndexError:
    print("Error: El índice al que intentas acceder se encuentra fuera del rango, debes utilizar un número mayor o igual que cero y menor que la longitud de la lista.")