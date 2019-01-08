# Colección de Datos - Diccionarios

Son junto a las listas las colecciones más utilizadas. Se basan en una estructura mapeada donde cada elemento de la colección se encuentra identificado con una clave única. Por tanto, no puede haber dos claves iguales. En otros lenguajes se conocen como arreglos asociativos.

> **NOTA**: En otros lenguajes se les conoce como **Arrays Asociativos**.

```python
vacio = {}
vacio
# {}
```

[Volver al inicio](#-colección-de-datos---diccionarios)

## TIPO DE UNA VARIABLE

---------------------------------------------------------------------------

```python
type(vacio)
# dict
```

[Volver al inicio](#-colección-de-datos---diccionarios)

## DEFINICIÓN

---------------------------------------------------------------------------

Para cada elemento se define la **estructura** -> *clave:valor*

```python
colores = {'amarillo':'yellow','azul':'blue'}
```

También se pueden añadir elementos sobre la marcha

```python
colores['verde'] = 'green'
colores
# {'amarillo': 'yellow', 'azul': 'blue', 'verde': 'green'}
colores['azul']
# 'blue'
colores['amarillo']
# 'yellow'
```

> **NOTA**: Las claves también pueden ser números, pero **son un poco confusas**

```python
numeros = {10:'diez',20:'veinte'}
numeros[10]
# 'diez'
```

[Volver al inicio](#-colección-de-datos---diccionarios)

## MODIFICACIÓN DE VALOR A PARTIR DE LA CLAVE

---------------------------------------------------------------------------

```python
colores['amarillo'] = 'white'
colores
# {'amarillo': 'white', 'azul': 'blue', 'verde': 'green'}
```

[Volver al inicio](#-colección-de-datos---diccionarios)

## FUNCIÓN DEL()

---------------------------------------------------------------------------

La función `del()`, sirve para borrar un elemento del diccionario.

```python
del(colores['amarillo'])
colores
# {'azul': 'blue', 'verde': 'green'}
```

[Volver al inicio](#-colección-de-datos---diccionarios)

## TRABAJANDO CON REGISTROS

---------------------------------------------------------------------------

```python
edades = {'Hector':27,'Juan':45,'Maria':34}
edades
# {'Hector': 27, 'Juan': 45, 'Maria': 34}
edades['Hector']+=1
edades
# {'Hector': 28, 'Juan': 45, 'Maria': 34}
edades['Juan'] + edades['Maria']
# 79
```

[Volver al inicio](#-colección-de-datos---diccionarios)

## LECTURA SECUENCIA CON FOR ... IN ...

---------------------------------------------------------------------------

Podemos realizar una lectura secuencial del diccionarion con `for .. in ..`. Así, es posible utilizar una iteración for para recorrer los elementos del diccionario:

```python
for edad in edades:
    print(edad)
# Maria
# Hector
# Juan
```

> **NOTA**: El problema es que se devuelven las claves, no los valores. Para solucionarlo deberíamos indicar la clave del diccionario para cada elemento.

```python
for clave in edades:
    print(edades[clave])
# 34
# 28
# 45
for clave in edades:
    print(clave,edades[clave])
# Maria 34
# Hector 28
# Juan 45
```

[Volver al inicio](#-colección-de-datos---diccionarios)

## MÉTODO .ITEMS()

---------------------------------------------------------------------------

El método `.items()`, nos facilita la lectura en clave y valor de los elementos porque devuelve ambos valores en cada iteración automáticamente:

```python
for c,v in edades.items():
    print(c,v)
# Maria 34
# Hector 28
# Juan 45
```

[Volver al inicio](#-colección-de-datos---diccionarios)

## EJEMPLO UTILIZANDO DICCIONARIOS Y LISTAS A LA VEZ

---------------------------------------------------------------------------

Podemos crear nuestras propias estructuras avanzadas mezclando ambas colecciones. Mientras los diccionarios se encargarían de manejar las propiedades individuales de los registros, las listas nos permitirían manejarlos todos en conjunto.

```python
personajes = []
p = {'Nombre':'Gandalf','Clase':'Mago','Raza':'Humano'}  # No sé si era un humano pero lo parecía jeje
personajes.append(p)
personajes
# [{'Clase': 'Mago', 'Nombre': 'Gandalf', 'Raza': 'Humano'}]
p = {'Nombre':'Legolas','Clase':'Arquero','Raza':'Elfo'}
personajes.append(p)
p = {'Nombre':'Gimli','Clase':'Guerrero','Raza':'Enano'}
personajes.append(p)
personajes
# [{'Clase': 'Mago', 'Nombre': 'Gandalf', 'Raza': 'Humano'},
#  {'Clase': 'Arquero', 'Nombre': 'Legolas', 'Raza': 'Elfo'},
#  {'Clase': 'Guerrero', 'Nombre': 'Gimli', 'Raza': 'Enano'}]
for p in personajes:
    print(p['Nombre'], p['Clase'], p['Raza'])
# Gandalf Mago Humano
# Legolas Arquero Elfo
# Gimli Guerrero Enano
```

> **NOTA**: Estaba pensando que Gandalf en realidad no era un humano, pero como parecía uno podéis disculparme jeje

[Volver al inicio](#-colección-de-datos---diccionarios)