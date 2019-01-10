# El módulo math

Este módulo está siempre disponible. Permite acceder a las funciones matemáticas definidas por la norma C.

Estas funciones no se pueden utilizar con números complejos; utilice las funciones del mismo nombre del módulo `math` si necesita soporte para números complejos. 

La distinción entre las funciones que soportan números complejos y las que no lo hacen se hace porque la mayoría de los usuarios no quieren aprender la cantidad de matemáticas que se requieren para entender los números complejos. Recibir una excepción en lugar de un resultado complejo permite una detección más temprana del número complejo inesperado utilizado como parámetro, para que el programador pueda determinar cómo y por qué se generó en primer lugar.

```python
import math
```

[Volver al inicio](#-el-módulo-math)

## REDONDEOS

---------------------------------------------------------------------------

```python
import math

pi = 3.14159
round(pi) # Redondeo integrado
# 3
math.floor(pi) # Redondeo a la baja - Suelo
# 3
math.floor(3.99)
# 3
math.ceil(pi)  # Redondeo al alta - Techo
# 4
math.ceil(3.01)
# 4
```

[Volver al inicio](#-el-módulo-math)

## VALOR ABSOLUTO

---------------------------------------------------------------------------

```python
import math

abs(-10)
# 10
```

[Volver al inicio](#-el-módulo-math)

## SUMATORIO

---------------------------------------------------------------------------

* **Sumatorio integrado**

```python
import math

n = [0.9999999, 1, 2, 3]
sum(n)
# 6.999999900000001
```

* **Sumatorio mejorado para números reales**

```python
import math

math.fsum(n) 
# 6.9999999
```

[Volver al inicio](#-el-módulo-math)

## TRUNCAMIENTO

---------------------------------------------------------------------------

```python
import math

math.trunc(123.45) # Truncar, cortar la parte decimal
# 123
```

[Volver al inicio](#-el-módulo-math)

## POTENCIAS Y RAÍCES

---------------------------------------------------------------------------

```python
import math

math.pow(2, 3)  # Potencia con flotante 
# 8.0
2 ** 3  # Potencia directa
# 8
math.sqrt(9)  # Raíz cuadrada (square root)
# 3.0
```

[Volver al inicio](#-el-módulo-math)

## CONSTANTES

---------------------------------------------------------------------------

```python
import math

math.pi   # Constante pi
# 3.141592653589793
math.e   # Constante e
# 2.718281828459045
```

> **NOTA**: Podemos importar funciones exactas de una librería.

```python
from math import sqrt
n = sqrt(10)
print (n)
```

[Volver al inicio](#-el-módulo-math)