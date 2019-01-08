# Leyendo valores por teclado

Se consigue utilizando la instrucción `input()` que lee y devuelve una cadena:

[Volver al inicio](#-leyendo-valores-por-teclado)

## MÉTODO INPUT()

---------------------------------------------------------------------------

```python
valor = input()
# algo
valor
# 'algo'
```

> **NOTA**: Este método siempre leerá **cadenas** de caracteres. En caso de ser necesario podemos convertir el tipo de dato a número con el siguiente método `int()`.

```python
valor = input()
# 100
# Aunque leemos un número, en realidad es una cadena de texto
valor 
# '100'
int(valor)
# 100
```

[Volver al inicio](#-leyendo-valores-por-teclado)

## USAR UN MENSAJE ANTES DEL INPUT

---------------------------------------------------------------------------

Podemos mostrar un mensaje antes de leer el valor:

```python
valor = input("Introduce un valor: ")
# Introduce un valor: 100
valor
# '100'
```

> **NOTA**: Una cadena y un número no se pueden operar:

```python
valor + 100  
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-6-5071d551e583> in <module>()
# ----> 1 valor + 100
# TypeError: Can't convert 'int' object to str implicitly
```

[Volver al inicio](#-leyendo-valores-por-teclado)

## CONVERTIR CADENAS A NúMEROS

---------------------------------------------------------------------------

Para evitar este problema en la captura de datos por teclado mediante `input()`, usaremos el método `int()`.

```python
valor = input("Introduce un número entero: ")
# Introduce un número entero: 500
```

La función `int()` de entero, devuelve un número entero a partir de una cadena. Convertiremos el dato de cadena a entero mediante `int()`:

```python
valor = int(valor)  
valor
# 500
valor + 1000  # Ahora ya es operable
# 1500
```

También podemos usar el método `float()` de flotante, devuelve un número flotante a partir de una cadena:

```python
valor = input("Introduce un número entero: ")
# Introduce un número entero: 10.50
valor = float(valor)
10 + valor
# 20.5
valor
# 10.5
valor = float( input("Introduce un número decimal o entero: ") )
# Introduce un número decimal o entero: 3.14
valor
# 3.14
```

[Volver al inicio](#-leyendo-valores-por-teclado)