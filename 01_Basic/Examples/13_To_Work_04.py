# Completa el ejercicio aquí
suma = 0
numeros = int(input("¿Cuántos números quieres introducir? ") )
for x in range(numeros):
    suma += float(input("Introduce un número: ") )
print("Se han introducido",numeros,"números que en total han sumado",suma,"y la media es",suma/numeros)
# ¿Cuántos numeros quieres introducir? 4
# Introduce un número: 3
# Introduce un número: 2
# Introduce un número: 4
# Introduce un número: 6
# Se han introducido 4 números que en total han sumado 15.0 y la media es 3.75