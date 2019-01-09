numeros = [1,2,3,4]
print('numeros = [1,2,3,4]')
datos = [4,"Una cadena",-15,3.14,"Otra cadena"]
print('datos = [4,"Una cadena",-15,3.14,"Otra cadena"]')
datos[0]
print('datos[0] = ', datos[0])
# 4
datos[-1]
print('datos[-1] = ', datos[-1])
# 'Otra cadena'
datos[-2:]
print('datos[-2:] = ', datos[-2:])
# [3.14, 'Otra cadena']
numeros = [1,2,3,4]
print('numeros = [1,2,3,4]')
numeros + [5,6,7,8]
print('numeros + [5,6,7,8] = ', numeros + [5,6,7,8])
# [1, 2, 3, 4, 5, 6, 7, 8]
numeros = numeros + [1,2,3,4]
print('numeros = numeros + [1,2,3,4] = ', numeros)
numeros
# [1, 2, 3, 4, 1, 2, 3, 4]
pares = [0,2,4,5,8,10]
print('pares = [0,2,4,5,8,10]')
pares[3] = 6
print('pares[3] = 6')
pares
print(pares)
# [0, 2, 4, 6, 8, 10]
pares = [0,2,4,5,8,10]
print('pares = [0,2,4,5,8,10]')
pares.append(12)
print('pares.append(12)')
pares
print(pares)
# [0, 2, 4, 5, 8, 10, 12]
pares.append(7*2)
print('pares.append(7*2)')
pares
print(pares)
# [0, 2, 4, 5, 8, 10, 12, 14]
letras = ['a','b','c','d','e','f']
print("letras = ['a','b','c','d','e','f']")
letras[:3]
print('letras[:3] = ', letras[:3])
# ['a', 'b', 'c']
letras[:3] = ['A','B','C']
print("letras[:3] = ['A','B','C']")
letras
print(letras)
# ['A', 'B', 'C', 'd', 'e', 'f']

letras = ['a','b','c','d','e','f']
print("letras = ['a','b','c','d','e','f']")
letras[:3] = []
print('letras[:3] = []')
letras
print('letras = ', letras)
# ['d', 'e', 'f']
letras = []
print("letras = []")
letras
print("letras = ", letras)
# []

letras = ['a','b','c','d','e','f']
print("letras = ['a','b','c','d','e','f']")
len(letras)
print("len(letras) = ", len(letras))
# 0
pares = [0, 2, 4, 5, 8, 10, 12, 14]
print("pares = [0, 2, 4, 5, 8, 10, 12, 14]")
len(pares)
print("len(pares) = ", len(pares))
# 8

a = [1,2,3]
print('a = [1,2,3]')
b = [4,5,6]
print('b = [4,5,6]')
c = [7,8,9]
print('c = [7,8,9]')
r = [a,b,c]
print('r = [a,b,c] = ', r)
r
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
r[0]  # Primera sublista
# [1, 2, 3]
r[-1]  # Última sublista
# [7, 8, 9]
r[0][0]  # Primera sublista, y de ella, primer ítem
# 1
r[1][1]  # Segunda sublista, y de ella, segundo ítem
# 5
r[2][2]  # Tercera sublista, y de ella, tercer ítem
# 9
r[-1][-1]  # Última sublista, y de ella, último ítem
# 9