# BLOQUE 01

> **NOTA**: Estos ejercicios son optativos para hacer al final de la unidad y están pensados para apoyar el aprendizaje.

**1) Identifica el tipo de dato (int, float, string o list) de los siguientes valores literales**

```python
"Hola Mundo"            # ?
[1, 10, 100]            # ?
-25                     # ?
1.167                   # ?
["Hola", "Mundo"]       # ?
' '                     # ?
```

**2) Determina mentalmente (sin programar) el resultado que aparecerá por pantalla a partir de las siguientes variables:**

```python
a = 10                  # ?
b = -5                  # ?
c = "Hola "             # ?
d = [1, 2, 3]           # ?
print(a * 5)            # ?
print(a - b)            # ?
print(c + "Mundo")      # ?  
print(c * 2)            # ?
print(c[-1])            # ?
print(c[1:])            # ?
print(d + d)            # ?  
```

**3) El siguiente código pretende realizar una media entre 3 números, pero no funciona correctamente. ¿Eres capaz de identificar el problema y solucionarlo?**

```python
numero_1 = 9
numero_2 = 3
numero_3 = 6
​media = numero_1 + numero_2 + numero_3 / 3
print("La nota media es", media)
# La nota media es 14.0
```

**4) A partir del ejercicio anterior, vamos a suponer que cada número es una nota, y lo que queremos es obtener la nota media. El problema es que cada nota tiene un valor porcentual:**

```python
La primera nota vale un 15% del total
La segunda nota vale un 35% del total
La tercera nota vale un 50% del total
```

**Desarrolla un programa para calcular perfectamente la nota final.**

```python
nota_1 = 10
nota_2 = 7
nota_3 = 4
```

**Completa el ejercicio aquí**

**5) La siguiente matriz (o lista con listas anidadas) debe cumplir una condición, y es que en cada fila, el cuarto elemento siempre debe ser el resultado de sumar los tres primeros. ¿Eres capaz de modificar las sumas incorrectas utilizando la técnica del slicing?**

**Ayuda:** La función llamada sum(lista) devuelve una suma de todos los elementos de la lista ¡Pruébalo!

```python
matriz = [ 
    [1, 1, 1, 3],
    [2, 2, 2, 7],
    [3, 3, 3, 9],
    [4, 4, 4, 13]
]
```

**Completa el ejercicio aquí**

**6) Al realizar una consulta en un registro hemos obtenido una cadena de texto corrupta al revés. Al parecer contiene el nombre de un alumno y la nota de un exámen. ¿Cómo podríamos formatear la cadena y conseguir una estructura como la siguiente?:**

Nombre Apellido ha sacado un Nota de nota.
**Ayuda:** Para voltear una cadena rápidamente utilizando slicing podemos utilizar un tercer índice -1: *cadena[::-1]** *

```python
cadena = "zeréP nauJ,01"
```

**Completa el ejercicio aquí**

```python
cadena = "zeréP nauJ,01"
```

**Completa el ejercicio aquí**