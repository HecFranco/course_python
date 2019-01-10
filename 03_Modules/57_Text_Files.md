# Ficheros de texto

[Volver al inicio](#-ficheros-de-texto)

**Crear fichero y escribir texto**

```python
texto = "Una línea con texto\nOtra línea con texto"
fichero = open('fichero.txt','w')  # fichero.txt ruta donde lo crearemos, w indica modo de escritura, write (puntero principio)
fichero.write(texto) # escribimos el texto
fichero.close()  # cerramos el fichero
```

**Lectura de un fichero de texto**

```python
fichero = open('fichero.txt','r')  # modo lectura read, por defecto ya es r, no es necesario
texto = fichero.read() # lectura completa
fichero.close()
print(texto)
# Una línea con texto
# Otra línea con texto
```

**Extensión de un fichero de texto**

```python
fichero = open('fichero.txt','a')  # modo a, append, añadir - extender (puntero al final)
fichero.write('\nOtra línea más abajo del todo')
fichero.close()
```

**Otra línea más abajo del todo**

```python
fichero = open('fichero.txt','r')
texto = fichero.readlines() # leer creando una lista de líneas
fichero.close()
print(texto)
# ['Una línea con texto\n', 'Otra línea con texto\n', 'Otra línea más abajo del todo']
print(texto[-1]) # Última línea
# Otra línea más abajo del todo
```

**Lectura de un fichero no existente**

**¿Qué ocurre cuando intentamos leer un archivo que no existe?**

```python
fichero = open('fichero_inventado.txt','r')
# ---------------------------------------------------------------------------
# FileNotFoundError                         Traceback (most recent call last)
# <ipython-input-2-c2865d5b1523> in <module>()
# ----> 1 fichero = open('fichero_inventado.txt','r')
# FileNotFoundError: [Errno 2] No such file or directory: 'fichero_inventado.txt'
```

Ahora lo solucionaremos añadiendo el siguiente atributo, `a+`.

```python
fichero = open('fichero_inventado.txt','a+')  # Extensión con escritura simultánea, crea fichero si no existe
```

**Lectura línea a línea**

```python
fichero = open('fichero.txt','r')
fichero.readline()   # Línea a línea
# 'Una línea con texto\n'
fichero.readline()
# 'Otra línea con texto'
fichero.readline()
# ''
fichero.close()
```

**Lectura línea a línea secuencial**

```python
with open("fichero.txt", "r") as fichero:
    for linea in fichero:
        print(linea)
# Una línea con texto
# Otra línea con texto
# Otra línea más abajo del todo
```

**Manejando el puntero**

```python
fichero = open('fichero.txt','r')
fichero.seek(0) # Puntero al principio
fichero.read(10) # Leemos 10 carácteres
# 'Una línea '
fichero.read(10) # Leemos 10 carácteres más, a partir del 10 donde está el puntero
# 'con texto\n'
fichero.seek(0)
fichero.seek( len(fichero.readline()) ) # Leemos la primera línea y situamos el puntero al principio de la segunda
# 20
fichero.read() # Leemos todo lo que queda del puntero hasta el final
# '\nOtra línea con texto\nOtra línea más abajo del todo'
```

**Lectura y escritura a la vez**

```python
fichero2 = open('fichero2.txt','w')
texto = "Línea 1\nLínea 2\nLínea 3\nLínea 4"
fichero2.write(texto)
# 31
fichero2.close()
fichero2 = open('fichero2.txt','r+')  # + escritura simultánea, puntero al principio por defecto
fichero2.write('asdfgh')
# 6
fichero2.close()
```

**Modificar una línea específica**

```python
fichero2 = open('fichero2.txt','r+')  # modo lectura con escritura, puntero al principio por defecto
texto = fichero2.readlines() # leemos todas las líneas
texto[2] = "Esta es la línea 3 modificada\n"  # indice menos 1
texto
# ['asdfgh1\n', 'Línea 2\n', 'Esta es la línea 3 modificada\n', 'Línea 4']
fichero2.seek(0) # Ponemos el puntero al principio
fichero2.writelines(texto)
fichero2.close()
```

[Volver al inicio](#-ficheros-de-texto)