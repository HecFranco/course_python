# Completa el ejercicio aquí
colores = { 'rojo':'red', 'verde':'green', 'negro':'black' } 
try:
    colores['blanco']
except KeyError:
    print("Error: La clave del diccionario no se encuentra, debes probar con otra que sí exista.")