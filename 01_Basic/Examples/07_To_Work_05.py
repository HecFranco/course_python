matriz = [ 
    [1, 1, 1, 3],
    [2, 2, 2, 7],   #corregir
    [3, 3, 3, 9],
    [4, 4, 4, 13]  #corregir
]
# Completa el ejercicio aquí
matriz[1][-1] = sum(matriz[1][:-1])
matriz[3][-1] = sum(matriz[3][:-1])

print(matriz)
# [[1, 1, 1, 3], [2, 2, 2, 6], [3, 3, 3, 9], [4, 4, 4, 12]]