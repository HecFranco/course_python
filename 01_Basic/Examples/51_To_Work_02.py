# Completa el ejercicio aquí
lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

def modificar(l):
  
    l = list(set(l))  # Borrar los elementos duplicados (recrea la lista a partir de un nuevo diccionario)
    l.sort(reverse=True)  # Ordenar la lista de mayor a menor
 
    l_tmp = []  # Lista temporal que contendrá solo los números pares
    for n in l:
        if n%2 == 0:
            l_tmp.append(n)
            
    suma = sum(l_tmp)  # Realizar una suma de todos los números que quedan
    l_tmp.insert(0, suma)  # Añadir como primer elemento de la lista de pares la suma realizada
    return l_tmp  # Devolver la lista de pares modificada


nueva_lista = modificar(lista)
print( nueva_lista[0] == sum(nueva_lista[1:]) )