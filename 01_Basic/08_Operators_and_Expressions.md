# Operadores y Expresiones

Las expresiones son una parte fundamental de la programación ya que sirven para realizar una o varias operaciones sobre un dato o un conjunto de datos, obteniéndose otro dato como resultado. Los operadores definen algunas de las operaciones que pueden realizarse dentro de una expresión. 

[Volver al inicio](#-operadores-y-expresiones)

## TIPOS LÓGICOS

---------------------------------------------------------------------------

Representa la mínima expresión racional:

* Verdadero (True)
* Falso (False)

```python
1+1 == 3
# False
1+1 == 2
# True
```

[Volver al inicio](#-operadores-y-expresiones)

## OPERADORES RELACIONALES

---------------------------------------------------------------------------

Los operadores relacionales sirven para comparar dos valores, dependiendo del resultado de la comparación pueden devolver:

* Verdadero (True), si es cierta
* Falso (False), si no es cierta

#### IGUAL QUE

```python
3 == 2
# False
```

#### DISTINTO DE

```python
3 != 2
# True
```

#### MAYOR QUE

```python
3 > 2
# True
```

#### MENOR QUE

```python
3 < 2
# False
```

#### MAYOR O IGUAL QUE

```python
3 >= 4
# False
```

#### MENOR O IGUAL QUE

```python
3 <= 4
# True
```

[Volver al inicio](#-operadores-y-expresiones)

### COMPARANDO VARIABLES

---------------------------------------------------------------------------

También podemos comparar variables.

```python
a = 10
b = 5
a > b
# True
b != a
# True
a == b*2
# True
```

Y otros tipos, como cadenas, listas, el resultado de algunas funciones o los propios tipos lógicos

```python
"Hola" == "Hola"
# True
"Hola" != "Hola"
# False
c = "Hola"
c[0] == "H"
# True
c[-1] == "a"
# True
l1 = [0,1,2]
l2 = [2,3,4]
l1 == l2
# False
len(l1) == len(l2)
# True
l1[-1] == l2[0]
# True
True == True
# True
False == True
# False
False != True
# True
True > False
# True
False > True
# False
```

> **NOTA**: La representación aritmética de `True` y `False` equivale a `1` y `0` respectivamente

```python
True * 3
# 3
False / 5
# 0.0
True * False
# 0
```

[Volver al inicio](#-operadores-y-expresiones)

### OPERADORES LÓGICOS

---------------------------------------------------------------------------

Encontramos 3 básicos:

* `Not`
* `And`
* `Or`

#### NOT - NEGACIÓN LÓGICA

```python
not True
# False
not True == False
# True
```

#### AND - CONJUNCIÓN LÓGICA (AGRUPA UNIENDO)

```python
True and True
# True
True and False
# False
False and True
# False
False and False
# False
a = 45
a > 10 and a < 20
# False
c = "Hola Mundo"
len(c) >= 20 and c[0] == "H"
# False
```

#### OR - DISYUNCIÓN LÓGICA (AGRUPA SEPARANDO)

```python
True or True
# True
True or False
# True
False or True
# True
False or False
# False
c = "OTRA COSA"
c == "EXIT" or c == "FIN" or c == "SALIR"
# False
c = "Lector"
c[0] == "H" or c[0] == "h"
# False
```

[Volver al inicio](#-operadores-y-expresiones)

### EXPRESIONES ANIDADAS

---------------------------------------------------------------------------

Se pueden solucionar empleando las reglas de precedencia:

* **Primero** los paréntesis porque tienen prioridad
* **Segundo**, las expresiones aritméticas por sus propias reglas
* **Tercero**, las expresiones relacionales
* **Cuarto**, las expresiones lógicas

```python
a = 10
b = 5
a * b - 2**b >= 20 and not (a % b) != 0
# False
```

[Volver al inicio](#-operadores-y-expresiones)

### OPERADORES DE ASIGNACIÓN

---------------------------------------------------------------------------

Actúan directamente sobre la variable actual modificando su valor.

```python
a = 0
a += 5 # suma en asignación
a
# 10
a -= 10 # resta en asignación
a
# 0
a = 5
a *= 2 # producto en asignación
a
# 10
a /= 2 # división en asignación
a
# 5.0
a %= 2 # módulo en asignación
a
# 1.0
a **= 10 # potencia en asignación
a
# 1.0
a = 5
a **= 5
a
# 3125
```

[Volver al inicio](#-operadores-y-expresiones)

### REPASANDO NUESTRO EJEMPLO DE CABECERA

---------------------------------------------------------------------------

**¿Qué expresiones eres capaz de identificar?**

```python
n = 0  #  Asignación de 0 en n
while n < 10:  #  Expresión relacional n < 10, que devuelve True
    if (n % 2) == 0:  # Expresión aritmética y expresión relacional
        print(n,'es un número par') 
    else:
        print(n,'es un número impar')
    n += 1  # expresión aritmética n = n + 1 equivalente a operación en asignación n+=1
```

[Volver al inicio](#-operadores-y-expresiones)