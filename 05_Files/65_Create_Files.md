# Crear Archivos

[Volver al inicio](#-crear-archivos)

## MANEJO DE ARCHIVOS CON PYTHON: CREAR, ABRIR, LEER, ESCRIBIR

---------------------------------------------------------------------------

En **Python**, no hay necesidad de importar una biblioteca externa para leer y escribir archivos. **Python** proporciona una función incorporada para crear, escribir y leer archivos.

[Volver al inicio](#-crear-archivos)

### CREAR UN ARCHIVO

---------------------------------------------------------------------------

Con **Python** puedes crear un **archivo.text** (`textfile.txt`) usando el código siguiente:

```python
f = open("textfile.txt","w+")
```

Declaramos la variable `f` para abrir un archivo llamado `textfile.txt`. El método `open()` toma 2 argumentos, el archivo que queremos abrir y una cadena que representa los tipos de permisos u operaciones que queremos hacer en el archivo.

> **NOTA**: Aquí usamos la letra `w` en nuestro argumento, que indica **escritura** y el signo más que significa que **creará un archivo si no existe en la biblioteca**.
Las opciones alternativas de `w`, son `r` para lectura y `a` para añadir, y `+` que significa que si no está ahí, entonces créala.

```diff
f= open("textfile.txt","w+")
++ for i in range(10):
++     f.write("This is line %d\r\n" % (i+1))
```

* Tenemos un bucle que corre sobre un rango de 10 números.
* Usando la función de escritura para introducir datos en el archivo.
* La salida que queremos iterar en el archivo es "this is line number", que declaramos con la función write y luego percent `d` (muestra integer)

Así que básicamente estamos poniendo el número de línea que estamos escribiendo, luego lo ponemos en un retorno de carro y un nuevo carácter de línea

```diff
f= open("textfile.txt","w+")
for i in range(10):
    f.write("This is line %d\r\n" % (i+1))
++ f.close()
```

El método `f.close()` cerrará la instancia del archivo `textfile.txt` almacenado.

Aquí está el resultado después de la ejecución del código:

```python
f = open("textfile.txt","w+")
for i in range(10):
    f.write("This is line %d\r\n" % (i+1))
f.close()
```

Cuando haga clic en su archivo de texto en nuestro caso `textfile.txt` se verá de la siguiente manera

```bash
This is line 1

This is line 2

This is line 3

This is line 4

This is line 5

This is line 6

This is line 7

This is line 8

This is line 9

This is line 10
```

> **NOTA**: Para evitar la creación de líneas intermedias añadiremos el argumento siguiente `newline=''`.

```diff
-- f = open("textfile.txt","w+")
++ f = open("textfile.txt","w+", newline='')
for i in range(10):
    f.write("This is line %d\r\n" % (i+1))
f.close()
```

[Volver al inicio](#-crear-archivos)

### AÑADIR DATOS A UN ARCHIVO

---------------------------------------------------------------------------

También puede añadir un nuevo texto al archivo ya existente o al nuevo archivo.

```python
f=open("textfile.txt", "a+")
```

> **NOTA**: Una vez más si pudieras ver un signo `+` en el código, indica que creará un nuevo archivo si no existe. Pero en nuestro caso ya tenemos el archivo, así que no estamos obligados a crear un nuevo archivo.

```diff
f=open("textfile.txt", "a+")
++ for i in range(2):
++      f.write("Appended line %d\r\n" % (i+1))
```

Esto escribirá los datos en el archivo en modo `append`.

Puede ver la salida en el archivo `textfile.txt`. La salida del código es que el archivo anterior se añade con nuevos datos.

```bash
This is line 1

This is line 2

This is line 3

This is line 4

This is line 5

This is line 6

This is line 7

This is line 8

This is line 9

This is line 10

Appended line 1

Appended line 2
```

> **NOTA**: Para evitar la creación de líneas intermedias añadiremos el argumento siguiente `newline=''`.

```diff
-- f=open("textfile.txt", "a+")
++ f=open("textfile.txt", "a+", newline='')
for i in range(2):
     f.write("Appended line %d\r\n" % (i+1))
```

[Volver al inicio](#-crear-archivos)

### AÑADIR DATOS A UN ARCHIVO

---------------------------------------------------------------------------

No sólo puede crear un `textfile.txt` desde **Python**, sino que también puede llamar al **textfile.txt** en un "modo de lectura"(r).

1. Abrir el archivo en modo de lectura

```python
f=open("textfile.txt", "r")
```
2. Usamos la función de modo en el código para comprobar que el archivo está en modo abierto. En caso afirmativo, seguimos adelante

```diff
f=open("textfile.txt", "r")
++ f.mode == 'r':
```

3. Utilice f.read para leer los datos del archivo y almacenarlos en contenido variable

```diff
f=open("textfile.txt", "r")
f.mode == 'r':
++ contenido =f.read()
```
	
4. imprimir el contenido

```bash
$ python python-by-sample/05_Files/Examples/65_guru_3.py
# This is line 1
# 
# This is line 2
# 
# This is line 3
# 
# This is line 4
# 
# This is line 5
# 
# This is line 6
# 
# This is line 7
# 
# This is line 8
# 
# This is line 9
# 
# This is line 10
# 
# Appended line 1
# 
# Appended line 2
```

[Volver al inicio](#-crear-archivos)

### CÓMO LEER UN ARCHIVO LÍNEA POR LÍNEA

---------------------------------------------------------------------------

También puede leer su `textfile.txt` línea por línea si sus datos son demasiado grandes para leerlos. Este código separará sus datos en modo fácil de preparar

Cuando ejecute el código (`f1=f.readlines()`) para leer el archivo o documento línea por línea, separará cada línea y presentará el archivo en un formato legible. En nuestro caso la línea es corta y legible, la salida se verá similar al modo de lectura. Pero si hay un archivo de datos complejo que no es legible, este trozo de código podría ser útil.

[Volver al inicio](#-crear-archivos)

### MODOS DE ARCHIVO EN PYTHON

---------------------------------------------------------------------------

**Modo Descripción
* `r` Este es el modo por defecto. Abre archivo para lectura.
* `w` Este modo abre el archivo para escribir. 
    * Si el archivo no existe, crea un nuevo archivo.
    * Si existe un archivo, lo trunca.
* `x` Crea un nuevo archivo. Si el archivo ya existe, la operación falla.
* `a` Abrir archivo en modo append. 
    * Si el archivo no existe, crea un nuevo archivo.
* `t` Este es el modo por defecto. Se abre en modo texto.
* `b` Se abre en modo binario.
    * Se abrirá un archivo de lectura y escritura (actualización)

**Código de ejemplo**

```python
# EJEMPLO PYTHON 2
def main():
     f= open("textfile.txt","w+")
     # f=open("textfile.txt","a+")
     for i in range(10):
         f.write("This is line %d\r\n" % (i+1))
     f.close()   
     # Abrir el archivo de nuevo y lea el contenido
     # f=open("textfile.txt", "r")
     #   if f.mode == 'r': 
     #     contents =f.read()
     #     print contents
     # o, readlines() lee la línea individual en una lista
     # fl =f.readlines()
     # for x in fl:
     #  print x
if __name__== "__main__":
  main()
```

```python
# EJEMPLO PYTHON 3
def main():
    f= open("textfile.txt","w+")
    #f=open("textfile.txt","a+")
    for i in range(10):
         f.write("This is line %d\r\n" % (i+1))
    f.close()
    # Abrir el archivo de nuevo y lea el contenido
    # f=open("textfile.txt", "r")
    # if f.mode == 'r':
    #   contents =f.read()
    #    print (contents)
    # o, readlines() lee la línea individual en una lista
    # fl =f.readlines()
    # for x in fl:
    #   print(x)
if __name__== "__main__":
  main()
```

* Utilice la función `open("filename", "w+")` para crear un archivo. 

> **NOTA**: El `+` le dice al compilador de python que cree un archivo si no existe.

* Para añadir datos a un archivo existente, utilice el comando `open("Filename", "a")` (a ->append())
* Utilizar la función de `read` para leer TODO el contenido de un fichero.
* Utilice la función `readlines` de lectura para leer el contenido del archivo uno por uno.

![Fuente: https://www.guru99.com/reading-and-writing-files-in-python.html](https://www.guru99.com/reading-and-writing-files-in-python.html)
