# BLOQUE 10

> **NOTA**: Estos ejercicios son optativos para hacer al final de la unidad y están pensados para apoyar tu aprendizaje.

**1) Utilizando todo lo que sabes sobre cadenas, listas, sus métodos internos... Transforma este texto:**

```bash
un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro
En este otro:
```
```pre
Un día que el viento soplaba con fuerza...
- Mira como se mueve aquella banderola -dijo un monje.
- Lo que se mueve es el viento -respondió otro monje.
- Ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro.
```

> **NOTA**: Lo único prohibido es modificar directamente el texto

```python
texto = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"
```

**2) Crea una función `modificar()` que a partir de una lista de números realice las siguientes tareas sin modificar la original:**
```pre
Borrar los elementos duplicados
Ordenar la lista de mayor a menor
Eliminar todos los números impares
Realizar una suma de todos los números que quedan
Añadir como primer elemento de la lista la suma realizada
Devolver la lista modificada
Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, concuerda con el primer número de la lista, tal que así:
nueva_lista = modificar(lista)
print( nueva_lista[0] == sum(nueva_lista[1:]) )
> True
```

> **NOTA**: La función `sum(lista)` devuelve una suma de los elementos de una lista

```python
lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]
```
