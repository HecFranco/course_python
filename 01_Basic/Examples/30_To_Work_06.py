numeros = [-12, 84, 13, 20, -33, 101, 9]

# Completa el ejercicio aquí

def separar(lista):
    numeros.sort()
    pares = []
    impares = []
    for n in numeros:
        if n%2 == 0:
            pares.append(n)
        else:
            impares.append(n)
    return pares, impares

pares, impares = separar(numeros)
print(pares)
print(impares)