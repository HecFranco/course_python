# El módulo random

El modulo random proporciona un generador de números aleatorios, por lo que es adecuado para una gran gama de aplicaciones: juegos, web, bases de datos, etc.

```python
import random
random.random() # Flotante aleatorio >= 0 y < 1.0
# 0.12539542779843138
random.random() # Flotante aleatorio >= 0 y < 1.0
# 0.3332807222427663
random.uniform(1,10) # Flotante aleatorio >= 1 y <10.0
# 6.272300429556777
random.randrange(10) # Entero aleatorio de 0 a 9, 10 excluído
# 7
random.randrange(0,101) # Entero aleatorio de 0 a 100
# 14
random.randrange(0,101,2) # Entero aleatorio de 0 a 100 cada 2 números, múltiples de 2
# 68
random.randrange(0,101,5) # Entero aleatorio de 0 a 100 cada 5 números, múltiples de 5
# 25
c = 'Hola mundo'
random.choice(c) # letra aleatoria
# 'o'
l = [1,2,3,4,5]
random.choice(l) # elemento aleatorio
# 3
random.shuffle(l) # barajar una lista, queda guardado
l
# [3, 4, 2, 5, 1]
random.sample(l, 2) # muestra aleatoria de 2 elementos de la lista
# [3, 4]
```