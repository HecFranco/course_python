# Tipos de Datos

**Python** dispone de tres tipos de datos con los cuales manejarse:

* **NÚMEROS**, engloban **int** (1,3,5,7,8,...), **float** (3.5, 4.3)
* **CADENAS DE CARACTERES**
* **LISTAS**

> **NOTA**: A diferencia de otros lenguajes, **Python** presume de tener un número de tipos de datos bajo. (**JAVA** presume de tener muchos)

[Volver al inicio](#-tipos-de-datos)

## NÚMEROS

---------------------------------------------------------------------------

Como inicio a **Python** y de paso aprendizaje del uso de **Jupiter** realizaremos los siguientes ejemplos, usando **Python** como una calculadora:

> **NOTA**: Podemos utilizar comentarios `#` para explicar lo que hace nuestro código.

[Volver al inicio](#-tipos-de-datos)

### TIPOS DE NÚMEROS

---------------------------------------------------------------------------

En **Python** podemos distinguir **2 tipos de números**:

* **Enteros**: Que no tienen una parte decimal y van desde menos infinito a más infinito.
* **Flotantes o decimales**: Números que tienen una parte decimal escrita con un punto.

```python
# Número entero
1
# Número flotante
323239829389.238273283
```

[Volver al inicio](#-tipos-de-datos)

### OPERACIÓNES BÁSICAS CON NÚMEROS

---------------------------------------------------------------------------

#### SUMA

```python
3 + 2
# 5
```

#### RESTA

```python
3 - 2
# 1
```

#### MULTIPLICACIÓN

```python
3 * 2
# 6
```

#### DIVISIÓN

```python
3 / 2
# 1.5
```

> **NOTA**: Al ser un lenguaje desarrollado en por el mundo anglosajón, empleará los puntos, `.`, en lugar de comas, `,`, para la separación de la parte entera de la decimal en los números.

#### DIVISIÓN PARTE ENTERA

```python
19 // 2
# 9
```

#### MÓDULO

El módulo es el resultado del resto en una división entera, es decir, si se realizase una divisón en la que el resultado fuera un número entero el módulo sería igual al resto de la misma.

```python
3 % 2
# 1
```

#### POTENCIA

```python
3 ** 2
# igual a 9^2
# 9
```

[Volver al inicio](#-tipos-de-datos)

### OPERACIÓNES COMPLEJAS CON NÚMEROS

---------------------------------------------------------------------------

También podemos realizar operaciones más complejas. 

**¿QUÉ OCURRIRÍA SI EJECUTASEMOS LA SIGUIENTE OPERACIÓN CON PYTHON, `3 - 2 + 4 * 10`?**

Python interpretará automáticamente las prioridades de los operadores:

```python
3 - 2 + 4 * 10
# 41
```

Lo ideal sería escribir `3 - 2 + ( 4 * 10 )`

> **NOTA**: Este es el concepto más importante en la programación, ya que no prevalece el orden de las operaciones para se ejecuación, sino su peso.
> **RECOMENDACIÓN**: Siempre ante la duda se podrán usar parénteisis, `()` para separar operaciones, asignando pesos.

**ESTE ASPECTO ES MUY IMPORTANTE, ASÍ QUE PRACTICAR MUCHO**

[Volver al inicio](#-tipos-de-datos)