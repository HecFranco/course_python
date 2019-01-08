# Funciones recursivas

Se trata de funciones que se llaman a sí mismas durante su propia ejecución. Funcionan de forma similar a las iteraciones, y debemos encargarnos de planificar el momento en que una función recursiva deja de llamarse o tendremos una función rescursiva infinita.

Suele utilizarse para dividir una tarea en subtareas más simples de forma que sea más fácil abordar el problema y solucionarlo.

[Volver al inicio](#-funciones-recursivas)

## SIN RETORNO

---------------------------------------------------------------------------

**EJEMPLO**: Cuenta regresiva hasta cero a partir de un número:

```python
def cuenta_atras(num):
    num -= 1
    if num > 0:
        print(num)
        cuenta_atras(num)
    else:
        print("Boooooooom!")
    print("Fin de la función", num)
​cuenta_atras(5)
# 4
# 3
# 2
# 1
# Boooooooom!
# Fin de la función 0
# Fin de la función 1
# Fin de la función 2
# Fin de la función 3
# Fin de la función 4
```

[Volver al inicio](#-funciones-recursivas)

## CON RETORNO

---------------------------------------------------------------------------

**EJEMPLO**: factorial de un número

El factorial de un número corresponde al producto de todos los números desde 1 hasta el propio número:

```python
3! = 1 x 2 x 3 = 6
5! = 1 x 2 x 3 x 4 x 5 = 120
def factorial(num):
    print("Valor inicial ->",num)
    if num > 1:
        num = num * factorial(num -1)
    print("valor final ->",num)
    return num
​factorial(5)
# Valor inicial -> 5
# Valor inicial -> 4
# Valor inicial -> 3
# Valor inicial -> 2
# Valor inicial -> 1
# valor final -> 1
# valor final -> 2
# valor final -> 6
# valor final -> 24
# valor final -> 120
# 120
```

[Volver al inicio](#-funciones-recursivas)
