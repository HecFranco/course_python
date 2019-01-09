# BLOQUE 03

> **NOTA**: Estos ejercicios son optativos para hacer al final de la unidad y están pensados para apoyar tu aprendizaje.

**1) Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:**

* Mostrar una suma de los dos números
* Mostrar una resta de los dos números (el primero menos el segundo)
* Mostrar una multiplicación de los dos números
* En caso de no introducir una opción válida, el programa informará de que no es correcta.

​**PASOS A SEGUIR**

1. Añadimos en nuestro script los métodos input que capturaran los datos de consola

```python
# Completa el ejercicio aquí
n1 = float(input("Introduce un número: ") )
n2 = float(input("Introduce otro número: ") )
```

2. Incluimos mediante un `print`las distintas opciones a elegir or nuestra aplicación:

```diff
# Completa el ejercicio aquí
n1 = float(input("Introduce un número: ") )
n2 = float(input("Introduce otro número: ") )
++ print("¿Qué quieres hacer? \n1) Sumar los dos números\n2) Restar los dos números\n3) Multiplicar los dos números")
```

3. E incluimos el input que capturará la opción seleccionada:

```diff
# Completa el ejercicio aquí
n1 = float(input("Introduce un número: ") )
n2 = float(input("Introduce otro número: ") )
print("¿Qué quieres hacer? \n1) Sumar los dos números\n2) Restar los dos números\n3) Multiplicar los dos números")
++ opcion = int(input("Introduce un número: ") )
```

4. Habrá que definir un valor por defecto a esa opción:


```diff
# Completa el ejercicio aquí
n1 = float(input("Introduce un número: ") )
n2 = float(input("Introduce otro número: ") )
++ opcion = 0
print("¿Qué quieres hacer? \n1) Sumar los dos números\n2) Restar los dos números\n3) Multiplicar los dos números")
opcion = int(input("Introduce un número: ") )
```

5. Mediante un condicional incluimos el selector de opciones con los resultados:

```diff
# Completa el ejercicio aquí
n1 = float(input("Introduce un número: ") )
n2 = float(input("Introduce otro número: ") )
opcion = 0
print("¿Qué quieres hacer? \n1) Sumar los dos números\n2) Restar los dos números\n3) Multiplicar los dos números")
opcion = int(input("Introduce un número: ") )
++ if opcion == 1:
++     print("La suma de",n1,"+",n2,"es",n1+n2)
++ elif opcion == 2:
++     print("La resta de",n1,"-",n2,"es",n1-n2)
++ elif opcion == 3:
++     print("El producto de",n1,"*",n2,"es",n1*n2)
++ else:
++     print("Opción incorrecta")
```

Nuestro script final será así:

```python
# Completa el ejercicio aquí
n1 = float(input("Introduce un número: ") )
n2 = float(input("Introduce otro número: ") )
opcion = 0
           
print("¿Qué quieres hacer? \n1) Sumar los dos números\n2) Restar los dos números\n3) Multiplicar los dos números")
opcion = int(input("Introduce un número: ") )     

if opcion == 1:
    print("La suma de",n1,"+",n2,"es",n1+n2)
elif opcion == 2:
    print("La resta de",n1,"-",n2,"es",n1-n2)
elif opcion == 3:
    print("El producto de",n1,"*",n2,"es",n1*n2)
else:
    print("Opción incorrecta")
```

Al ejecutarlo deberemos ver en pantalla algo parecido a esto:

```bash
# Introduce un número: 5
# Introduce otro número: 5
# ¿Qué quieres hacer? 
# 1) Sumar los dos números
# 2) Restar los dos números
# 3) Multiplicar los dos números
# Introduce un número: 3
# El producto de 5.0 * 5.0 es 25.0
```

**2) Realiza un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, debe repetise el proceso hasta que lo introduzca correctamente.**

​**PASOS A SEGUIR**

1. Crearemos una variable inicial con un valor por defecto:

```python
# Completa el ejercicio aquí
numero = 0
```

2. Ahora incluiremos nuestro `while` que devolverá el resultado esperado:

```diff
# Completa el ejercicio aquí
numero = 0
++ while numero % 2 == 0:  # Mientras sea par repetimos el proceso
++     numero = int(input("Introduce un número impar: ") )
```

Nuestro script final será así:

```python
# Completa el ejercicio aquí
numero = 0
while numero % 2 == 0:  # Mientras sea par repetimos el proceso
    numero = int(input("Introduce un número impar: ") )
```

Al ejecutarlo deberemos ver en pantalla algo parecido a esto:

```bash
# Introduce un número impar: 4
# Introduce un número impar: 2
# Introduce un número impar: 3
```

**3) Realiza un programa que sume todos los números enteros pares desde el `0` hasta el `100`:**

**Sugerencia**: Puedes utilizar la funciones `sum()` y `range()` para hacerlo más fácil. El tercer parámetro en la función range(inicio, fin, salto) indica un salto de números, pruébalo.

​**PASOS A SEGUIR PRIMERA OPCIÓN**

1. Generamos nuestro array con los número enteros pares medante `range`:

```python
# Completa el ejercicio aquí
range(0, 101, 2)
```

2. Realizamos la suma del array:

```diff
# Completa el ejercicio aquí
-- range(0, 101, 2)
++ suma = sum( range(0, 101, 2) )
```

3. Iprimimos el resultado:

```diff
# Completa el ejercicio aquí
suma = sum( range(0, 101, 2) )
++ print(suma)
```

Nuestro script final será así:

```python
# Completa el ejercicio aquí
suma = sum( range(0, 101, 2) )
print(suma)
```

Al ejecutarlo deberemos ver en pantalla algo parecido a esto:

```bash
# 2550
```

​**PASOS A SEGUIR SEGUNDA OPCIÓN**

1. Definimos el rango de suma:

```python
# Completa el ejercicio aquí
num = 0
suma = 0
```

2. Recorremos los números pares existentes en el rango:

```diff
# Completa el ejercicio aquí
num = 0
suma = 0
++ while num <= 100:
++  print(num)
++  num += 1
```

3. Seleccionamos sólo los números pares del rango:

```diff
# Completa el ejercicio aquí
num = 0
suma = 0
while num <= 100:
++  if num % 2 == 0:
--  print(num)
++    print(num)
++  num += 1
```

4. Si es par el número lo sumaremos al inicial:

```diff
# Completa el ejercicio aquí
num = 0
suma = 0
while num <= 100:
    if num % 2 == 0:
++      suma += num
    num += 1
print(suma)
```

Nuestro script final será así:

```python
# Segunda forma con bucles
num = 0
suma = 0

while num <= 100:
    if num % 2 == 0:
        suma += num
    num += 1
    
print(suma)
```

Al ejecutarlo deberemos ver en pantalla algo parecido a esto:

```bash
# 2550
```

**4) Realiza un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números y realiza una media aritmética:**

​**PASOS A SEGUIR**

1. Definimos un valor inicial para la suma

```python
# Completa el ejercicio aquí
suma = 0
```

2. Capturamos el primer valor que define el número de datos a sumar:

```diff
# Completa el ejercicio aquí
suma = 0
++ numeros = int(input("¿Cuántos números quieres introducir? ") )
```

3. Recorremos mediante un `for` el rango definido solicitando valores:

```diff
# Completa el ejercicio aquí
suma = 0
numeros = int(input("¿Cuántos números quieres introducir? ") )
++ for x in range(numeros):
++     suma += float(input("Introduce un número: ") )
```

4. Imprimimos el resultado de la suma:

```diff
# Completa el ejercicio aquí
suma = 0
numeros = int(input("¿Cuántos números quieres introducir? ") )
for x in range(numeros):
    suma += float(input("Introduce un número: ") )
++ print("Se han introducido",numeros,"números que en total han sumado",suma,"y la media es",suma/numeros)
```

Al ejecutarlo deberemos ver en pantalla algo parecido a esto:

```bash
# ¿Cuántos numeros quieres introducir? 4
# Introduce un número: 3
# Introduce un número: 2
# Introduce un número: 4
# Introduce un número: 6
# Se han introducido 4 números que en total han sumado 15.0 y la media es 3.75
```

**5) Realiza un programa que pida al usuario un número entero del `0` al `9`, y que mientras el número no sea correcto se repita el proceso. Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:**

**Consejo**: La sintaxis "valor in lista" permite comprobar fácilmente si un valor se encuentra en una lista (devuelve True o False)

```python
numeros = [1, 3, 6, 9]
```

​**PASOS A SEGUIR**

1. Incluimos el array en nuestro script:

```python
# Completa el ejercicio aquí
numeros = [1, 3, 6, 9]
```

2. Incluimos un while que solicite números del 1 al 9:

```diff
# Completa el ejercicio aquí
numeros = [1, 3, 6, 9]

++ while True:
++     numero = int(input("Escribe un número del 0 al 9: "))
```

3. Añadimos las distintas opciones:

```diff
# Completa el ejercicio aquí
numeros = [1, 3, 6, 9]

while True:
    numero = int(input("Escribe un número del 0 al 9: "))
++  if numero in numeros:
++      print("El número",numero,"se encuentra en la lista",numeros)
++  else:
++      print("El número",numero,"no se encuentra en la lista",numeros)
```

4. Como extra incluimos la opción de que no se encuentre en el rango el número:

```diff
# Completa el ejercicio aquí
numeros = [1, 3, 6, 9]

while True:
    numero = int(input("Escribe un número del 0 al 9: "))
++  if numero >= 0 and numero <= 9:
++      break
    if numero in numeros:
        print("El número",numero,"se encuentra en la lista",numeros)
    else:
        print("El número",numero,"no se encuentra en la lista",numeros)
```



**6) Utilizando la función `range()` y la conversión a listas genera las siguientes listas dinámicamente:**

* Todos los números del 0 al 10 [0, 1, 2, ..., 10]
* Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
* Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
* Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
* Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]
**Pista**: Utiliza el tercer parámetro de la función range(inicio, fin, salto).
​
​**PASOS A SEGUIR**

1. Cumplimos la primera condición:

```python
# Completa el ejercicio aquí
print( list( range( 0, 11 ) ) )
```

2. Cumplimos la segunda condición:

```diff
# Completa el ejercicio aquí
print( list( range( 0, 11 ) ) )
++ print( list( range( -10, 1 ) ) )
```

3. Cumplimos la tercera condición:

```diff
# Completa el ejercicio aquí
print( list( range( 0, 11 ) ) )
print( list( range( -10, 1 ) ) )
++ print( list( range( 0, 21, 2 ) ) )
```

4. Cumplimos la segunda condición:

```diff
# Completa el ejercicio aquí
print( list( range( 0, 11 ) ) )
print( list( range( -10, 1 ) ) )
print( list( range( 0, 21, 2 ) ) )
++ print( list( range( -19, 0, 2 ) ) )
```

5. Cumplimos la segunda condición:

```diff
# Completa el ejercicio aquí
print( list( range( 0, 11 ) ) )
print( list( range( -10, 1 ) ) )
print( list( range( 0, 21, 2 ) ) )
print( list( range( -19, 0, 2 ) ) )
++ print( list( range( 0, 51, 5 ) ) )
```

Al ejecutarlo deberemos ver en pantalla algo parecido a esto:

```bash
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# [-19, -17, -15, -13, -11, -9, -7, -5, -3, -1]
# [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
```

**7) Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, pero no debe repetise ningún elemento en la nueva lista:**

​**PASOS A SEGUIR**

1. Incluimos las dos listas a comparar:

```python
# Completa el ejercicio aquí
lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
```

2. Incluimos la lista inicial vacía:

```diff
# Completa el ejercicio aquí
lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
++ lista_3 = []
```

3. Recorremos mediante un for la primera lista para comprobar si está o no en la lista 2 y 3 (nueva):

```diff
# Completa el ejercicio aquí
lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
lista_3 = []
++ for letra in lista_1:
++     if letra in lista_2 and letra not in lista_3:
++         lista_3.append(letra)
```

4. Imprimimos el reusltado:

```diff
# Completa el ejercicio aquí
lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']

lista_3 = []

for letra in lista_1:
    if letra in lista_2 and letra not in lista_3:
        lista_3.append(letra)

++ print(lista_3)
```

Al ejecutarlo deberemos ver en pantalla algo parecido a esto:

```bash
# ['h', 'o', 'l', 'a', ' ', 'u', 'n']
```
