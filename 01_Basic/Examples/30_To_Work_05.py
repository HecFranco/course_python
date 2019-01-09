# Completa el ejercicio aquí
def recortar(numero, minimo, maximo):
    if numero < minimo:
        return minimo
    elif numero > maximo:
        return maximo
    return numero

print( recortar(15, 0, 10) )