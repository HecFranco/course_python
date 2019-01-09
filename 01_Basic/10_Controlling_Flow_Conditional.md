# Controlando el Flujo - Condicionales

Una **sentencia condicional** es una instrucción o grupo de instrucciones que se pueden ejecutar o no en función del valor de una condición.

Los tipos más conocidos de sentencias condicionales son el SI.. (if..) y el SI..SI NO (if..else), aunque también podríamos mencionar al manejo de excepciones como una alternativa más moderna para evitar el "anidamiento" de sentencias condicionales.

[Volver al inicio](#-controlando-el-flujo---condicionales)

## SENTENDIA IF

---------------------------------------------------------------------------

Permite dividir el flujo de un programa en diferentes caminos. El `if` se ejecuta siempre que la expresión que comprueba devuelva `True`

```python
if True:  # equivale a if not False
    print("Se cumple la condición")
    print("También se muestre este print")
# Se cumple la condición
```

Para que también se muestre este `print()` podemos encadenar diferentes `If`.

```python
a = 5
if a == 2:
    print("a vale 2")
if a == 5:
    print("a vale 5")
# a vale 5
```

O también anidar If dentro de If

```python
a = 5
b = 10
if a == 5:
    print("a vale",a)
    if b == 10:
        print("y b vale",b)
# a vale 5
# y b vale 10
```

Como condición podemos evaluar múltiples expresiones, siempre que éstas devuelvan True o False

```python
if a==5 and b == 10:
    print("a vale 5 y b vale 10")
# a vale 5 y b vale 10
```

[Volver al inicio](#-controlando-el-flujo---condicionales)

## SENTENDIA ELSE

---------------------------------------------------------------------------

La sentencia `Else`, (sino), se encadena a un `If` para comprobar el caso contrario (en el que no se cumple la condición).

```python
n = 11
if n % 2 == 0:
    print(n,"es un número par")
else:
    print(n,"es un número impar")
# 11 es un número impar
```

[Volver al inicio](#-controlando-el-flujo---condicionales)

## SENTENDIA ELIF

---------------------------------------------------------------------------

La sentencia `Elif`, (Sino Si), se encadena a un `if` u otro `elif` para comprobar múltiples condiciones, siempre que las anteriores no se ejecuten.

```python
comando = "OTRA COSA"
if comando == "ENTRAR":
    print("Bienvenido al sistema")
elif comando == "SALUDAR":
    print("Hola, espero que te lo estés pasando bien aprendiendo Python")
elif comando == "SALIR":
    print("Saliendo del sistema...")
else:
    print("Este comando no se reconoce")
# Este comando no se reconoce
nota = float(input("Introduce una nota: "))
print("Insertaste el valor: {}".format(nota))
if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 6:
    print("Bien")
elif nota >= 5:
    print("Suficiente")
else:
    print("Insuficiente")
# Introduce una nota: 10
# Sobresaliente
```

> **NOTA**: Forzaremos el tipo de dato en el `float(input("Introduce una nota: "))`, **casting** sobre la variable.

Es posible simular el funcionamiento de `elif` con `if` utilizando expresiones condicionales `and` y `or`:

```python
nota = float(input("Introduce una nota: "))
if nota >= 9:
    print("Sobresaliente")
if nota >= 7 and nota < 9:
    print("Notable")
if nota >= 6 and nota < 7:
    print("Bien")
if nota >= 5 and nota < 6:
    print("Suficiente")
if nota < 5:
    print("Insuficiente")
# Introduce una nota: 8
# Notable
```

[Volver al inicio](#-controlando-el-flujo---condicionales)

## INSTRUCCIÓN PASS

---------------------------------------------------------------------------

Sirve para finalizar un bloque, se puede utilizar en un bloque vacío.

```python
if True:
    pass
if True:
    pass
```

[Volver al inicio](#-controlando-el-flujo---condicionales)