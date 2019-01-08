# Métodos de los diccionarios

```python
colores = { "amarillo":"yellow", "azul":"blue", "verde":"green" }
colores['amarillo']
# 'yellow'
```

`get()`: Busca un elemento a partir de su clave y si no lo encuentra devuelve un valor por defecto

```python
colores.get('negro','no se encuentra')
# 'no se encuentra'
'amarillo' in colores
# True
```

`keys()`: Genera una lista en clave de los registros del diccionario

```python
colores.keys()
dict_keys(['amarillo', 'azul', 'verde'])
```

`values()`: Genera una lista en valor de los registros del diccionario

```python
colores.values()
dict_values(['yellow', 'blue', 'green'])
```

`items()`: Genera una lista en clave-valor de los registros del diccionario

```python
colores.items()
dict_items([('amarillo', 'yellow'), ('azul', 'blue'), ('verde', 'green')])
for c in colores:
    print(colores[c])
# yellow
# blue
# green
for c,v in colores.items():
    print(c,v) # clave, valor
# amarillo yellow
# azul blue
# verde green
```

`pop()`: Extrae un registro de un diccionario a partir de su clave y lo borra, acepta valor por defecto

```python
colores.pop("amarillo","no se ha encontrado")
# 'yellow'
colores
# {'azul': 'blue', 'verde': 'green'}
colores.pop("negro","no se ha encontrado")
# 'no se ha encontrado'
colores
# {'azul': 'blue', 'verde': 'green'}
```

`clear()`: Borra todos los registros de un diccionario

```python
colores.clear()
colores
# {}
```

`update()`: Actualiza un diccionario

```python
autores = {'libro 1': 'Héctor', 'libro 2': 'Ricardo'}
print(autores)
# {'libro 1': 'Héctor', 'libro 2': 'Ricardo'}
diccionario = {'libro 1': 'Manuel'}
autores.update(diccionario)
print(autores)
# {'libro 1': 'Manuel', 'libro 2': 'Ricardo'}
```

[Volver al inicio](#-métodos-de-las-diccionarios)