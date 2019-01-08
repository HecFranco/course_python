# BLOQUE 03

> **NOTA**: Estos ejercicios son optativos para hacer al final de la unidad y están pensados para apoyar tu aprendizaje.

**1) Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:**

* Mostrar una suma de los dos números
* Mostrar una resta de los dos números (el primero menos el segundo)
* Mostrar una multiplicación de los dos números
* En caso de no introducir una opción válida, el programa informará de que no es correcta.

**2) Realiza un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, debe repetise el proceso hasta que lo introduzca correctamente.**

**3) Realiza un programa que sume todos los números enteros pares desde el `0` hasta el `100`:**

**Sugerencia**: Puedes utilizar la funciones `sum()` y `range()` para hacerlo más fácil. El tercer parámetro en la función range(inicio, fin, salto) indica un salto de números, pruébalo.

**4) Realiza un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números y realiza una media aritmética:**

**5) Realiza un programa que pida al usuario un número entero del `0` al `9`, y que mientras el número no sea correcto se repita el proceso. Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:**

**Consejo**: La sintaxis "valor in lista" permite comprobar fácilmente si un valor se encuentra en una lista (devuelve True o False)

```python
numeros = [1, 3, 6, 9]
```

**6) Utilizando la función `range()` y la conversión a listas genera las siguientes listas dinámicamente:**

* Todos los números del 0 al 10 [0, 1, 2, ..., 10]
* Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
* Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
* Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
* Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]
**Pista**: Utiliza el tercer parámetro de la función range(inicio, fin, salto).
​
**7) Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, pero no debe repetise ningún elemento en la nueva lista:**