# Archivos CSV

El formato **CSV** es el formato de importación y exportación más comúnmente usado para bases de datos y hojas de cálculo. Este tutorial te dará una introducción detalladas a los CSV y los módulos y clases disponibles para leer y escribir datos a archivos CSV. También cubrirá un ejemplo de trabajo para mostrarte cómo leer y escribir datos a un archivo CSV en Python.

[Volver al inicio](#-archivos-csv)

## QUE ES UN ARCHIVO CSV

---------------------------------------------------------------------------

Un archivo **CSV** (valores separados por comas) permite que los datos sean guardados en una estructura tabular con una extensión **.csv**. Los archivos **CSV** han usados de manera extensiva en aplicaciones de comercio electrónico porque son considerados muy fáciles de procesar. Algunas de las áreas en donde han sido usados incluyen:

* **importar y exportar datos de clientes**
* **importar y exportar productos**
* **exportar órdenes**
* **exportar reportes analíticos de comercio electrónico**

[Volver al inicio](#-archivos-csv)

## MÓDULOS DE LECTURA Y ESCRITURA

---------------------------------------------------------------------------

El módulo **CSV** tiene varia funciones y clases disponibles para leer y escribir **CSVs**, y estas incluyen:

* función `csv.writer`
* función `csv.reader`
* clase `csv.Dictwriter`
* clase `csv.DictReader`

[Volver al inicio](#-archivos-csv)

### CSV.WRITER

---------------------------------------------------------------------------

Este módulo es similar al módulo `csv.reader` y es usado para escribir datos a un **CSV**. Este toma tres parámetros:

* `csvfile`: Este puede ser cualquier objeto con un método write().
* `dialect=’exel’`: Un parámetro opcional usado para definir un conjunto de parámetros específicos a un CSV en particular.
* `fmtparam`: Un parámetro opcional que puede ser usado para sobrescribir parámetros de formato existentes.

```python
import csv
doc_csv = open('./05_Files/Examples/datos_1.csv', 'w')  
csv_data = csv.writer(doc_csv)
list = [ "Jose", 912349817234 ]
csv_data.writerow(list)
doc_csv.close()
```

```python
import csv
doc_csv = open('./05_Files/Examples/datos_1.csv', 'w', newline='')  
csv_data = csv.writer(doc_csv)
list = [[ "Jose", 912349817234 ],[ "Juan", 912349817234 ],[ "Manuel", 912349817234 ]]
for element in list:
    csv_data.writerow(element)
doc_csv.close()
```

[Volver al inicio](#-archivos-csv)

### CSV.READER

---------------------------------------------------------------------------

El módulo `csv.reader` toma los siguientes parámetros:

* `csvfile`: Este es usualmente un objeto el cuál soporta el protocolo iterador y usualmente devuelve una cadena cada vez que su método `__next__()` es llamado.
* `dialect=’excel’`: Un parámetro opcional usado para definir un conjunto de parámetros específicos a un dialecto CSV en particular.
* `fmtparams`: Un parámetro opcional que puede ser usado para sobrescribir parámetros de formato existentes.

Aquí está un ejemplo de cómo usar el módulo `csv.reader`.

```python
import csv
with open('./05_Files/Examples/datos_1.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        print(row)
File.close()
```

[Volver al inicio](#-archivos-csv)

### CLASES DICTREADER Y DICTWRITER

---------------------------------------------------------------------------

`DictReader` y `DictWriter` son clases disponibles en **Python** para leer y escribir a un **CSV**. Aunque son similares a las funciones `reader` y `writer`, estas clases usan objetos de diccionario para leer y escribir a archivos csv.

[Volver al inicio](#-archivos-csv)

#### DICTWRITER

---------------------------------------------------------------------------

Esta clase es similar a la clase `DictWriter` y hace lo contrario, que es escribir datos a un archivo **CSV**. La clase es definida como `csv.DictWriter(csvfile, fieldnames, restval='', extrasaction='raise', dialect='excel', *args, **kwds)`

El parámetro `fieldnames` define la secuencia de llaves que identifican el orden en el cuál los valores en el diccionario son escritos al archivo **CSV**. A diferencia de `DictReader`, esta llave no es opcional y debe ser definida para evitar errores cuando se escribe a un **CSV**.

```python
import csv
 
with open('./05_Files/Examples/datos_2.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name', 'Grade']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
 
    writer.writeheader()
    writer.writerow({'Grade': 'B', 'first_name': 'Alex', 'last_name': 'Brian'})
    writer.writerow({'Grade': 'A', 'first_name': 'Rachael',
                     'last_name': 'Rodriguez'})
    writer.writerow({'Grade': 'B', 'first_name': 'Jane', 'last_name': 'Oscar'})
    writer.writerow({'Grade': 'B', 'first_name': 'Jane', 'last_name': 'Loive'})
 
print("Writing complete")
```

[Volver al inicio](#-archivos-csv)

#### DICTREADER

---------------------------------------------------------------------------

Esta crea un objeto el cuál mapea la información leída a un diccionario cuyas llaves están dadas por el parámetro `fieldnames`. Este parámetro es opcional, pero cuando no se especifica en el archivo, la primera fila de datos se vuelve las llaves del diccionario.

```python
import csv
with open('./05_Files/Examples/datos_2.csv') as csvfile:
reader = csv.DictReader(csvfile)
for row in reader:
         print(row['first_name'], row['last_name'])
```

[Volver al inicio](#-archivos-csv)

### DIALECTOS Y FORMATOS

---------------------------------------------------------------------------

Un dialecto es una clase ayudante usada para definir los parámetros para una instancia `reader` o `writer` específica. Los parámetros de dialecto y formato necesitan ser declarados cuando se realiza una función lectora o writer.

Hay varios atributos los cuáles están soportados por un dialecto:

* `delimiter`: Una cadena usada para separar campos. Por defecto es ‘,‘.
* `double quoute`: Controla cómo las instancias de quotechar que aparecen dentro de un campo deberían ser citadas. Puede ser Verdadero o Falso.
* `escapechar`: Una cadena usada por el escritor para escapar el delimitador si quoiting está establecido a QUOTE_NONE.
* `lineterminator`: Una cadena usada para terminar líneas producidas por el writer. Por defecto es '\r\n'.
* `quotechar`: Una cadena usada para citar campos conteniendo caracteres especiales. Por defecto es '"'.
* `skipinitialspace`: Si se establece a True, cualquier espacio en blanco después del delimitador es ignorado inmediatamente.
* `strict`: Si se establece a True, levanta una excepción Error en mala entrada CSV.
* `quoting`: Controla cuando deberían ser generadas las citas cuando se lee o escribe a un CSV.

[Volver al inicio](#-archivos-csv)

## LEYENDO UN ARCHIVO CSV

---------------------------------------------------------------------------

Veamos cómo leer un archivo CSV usando los módulos de ayuda que hemos discutido arriba.

Crea tu archivo **CSV** y guárdalo como `ejemplo.csv`. Asegura que tiene la extensión .csv y llena algunos datos. Aquí tenemos nuestro archivo **CSV** el cual contiene los nombres de los estudiantes y sus calificaciones.

Creating a spreadsheet to generate a CSV
Abajo está el código para leer los datos en nuestro CSV usando tanto la función `csv.reader` como la clase `csv.DictReader`.

[Volver al inicio](#-archivos-csv)

### LEYENDO UN ARCHIVO CSV CON CSV.READER

---------------------------------------------------------------------------

```python
import csv
 
with open('./05_Files/Examples/datos_2.csv') as File:
    reader = csv.reader(File, delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        print(row)
# ['first_name', 'last_name', 'Grade']
# ['Alex', 'Brian', 'B']
# ['Rachael', 'Rodriguez', 'A']
# ['Jane', 'Oscar', 'B']
# ['Jane', 'Loive', 'B']
```

En el código de arriba, importamos el módulo **CSV** y después abrimos nuestro archivo **CSV** como **File**. Entonces definimos el objeto lector y usamos el método csv.reader para extraer los datos al objeto. Entonces iteramos sobre el objeto reader y recuperamos cada fila de nuestros datos. 

Mostramos los datos leídos imprimiendo sus contenidos a la consola. También hemos especificado los parámetros requeridos tales como delimiter, quotechar, y quoting.

Salida

```bash
# ['first_name', 'last_name', 'Grade']
# ['Alex', 'Brian', 'B']
# ['Rachael', 'Rodriguez', 'A']
# ['Jane', 'Oscar', 'B']
# ['Jane', 'Loive', 'B']
```

**NOTA**: Otra opción para imprimir sólo algunos elementos de cada fila es usar el siguiente código:

```python
import csv
 
with open('./05_Files/Examples/datos_2.csv') as File:
    reader = csv.reader(File, delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
    for (first_name, last_name) in reader:
        print(first_name, last_name)
# ['first_name', 'last_name', 'Grade']
# ['Alex', 'Brian', 'B']
# ['Rachael', 'Rodriguez', 'A']
# ['Jane', 'Oscar', 'B']
# ['Jane', 'Loive', 'B']
```

[Volver al inicio](#-archivos-csv)

### LEYENDO UN ARCHIVO CSV CON DICTREADER

---------------------------------------------------------------------------

Como mencionamos arriba, `DictReader` nos permite leer un archivo CSV mapeando datos a un diccionario en vez de cadenas como en el caso del módulo `csv.rader`. Aunque el `fieldname` es un parámetro opcional, es importante siempre tener etiquetadas tus columnas para legibilidad.

Aquí está cómo leer un CSV usando la clase DictReader.

```python
import csv
 
results = []
with open('./05_Files/Examples/datos_3.csv') as File:
    reader = csv.DictReader(File)
    for row in reader:
        results.append(row)
    print (results)
# [
#   OrderedDict(
#       [
#           ('first_name', 'Alex'),
#           ('last_name', 'Brian'),
#           ('Grade', 'B')
#       ]
#   ), 
#   OrderedDict(
#       [
#           ('first_name', 'Rachael'), 
#           ('last_name', 'Rodriguez'), 
#           ('Grade', 'A')
#       ]
#   ), 
#   OrderedDict(
#       [
#           ('first_name', 'Jane'), 
#           ('last_name', 'Oscar'), 
#           ('Grade', 'B')
#       ]
#   ), 
#   OrderedDict(
#       [
#           ('first_name', 'Jane'),
#           ('last_name', 'Loive'), 
#           ('Grade', 'B')
#       ]
#   )
# ]    
```

Primero importamos el **módulo csv** e inicializamos una lista vacía `results` la cuál usaremos para almacenar los datos recuperados. Después definimos el objeto lector y usamos el método `csv.DictReader` para extraer los datos en el objeto. Entonces iteramos el objeto `reader` y recuperamos cada fila de nuestros datos.

Finalmente, adjuntamos cada fila a la lista de resultados e imprimimos los contenidos a la consola.

Salida

```bash
# [
#   OrderedDict(
#       [
#           ('first_name', 'Alex'),
#           ('last_name', 'Brian'),
#           ('Grade', 'B')
#       ]
#   ), 
#   OrderedDict(
#       [
#           ('first_name', 'Rachael'), 
#           ('last_name', 'Rodriguez'), 
#           ('Grade', 'A')
#       ]
#   ), 
#   OrderedDict(
#       [
#           ('first_name', 'Jane'), 
#           ('last_name', 'Oscar'), 
#           ('Grade', 'B')
#       ]
#   ), 
#   OrderedDict(
#       [
#           ('first_name', 'Jane'),
#           ('last_name', 'Loive'), 
#           ('Grade', 'B')
#       ]
#   )
# ]
```

Como puedes ver arriba, usar la clase `DictReader` es mejor porque da nuestros datos en un formato de diccionario con el cual es más sencillo trabajar.

[Volver al inicio](#-archivos-csv)

### ESCRIBIENDO UN ARCHIVO CSV

---------------------------------------------------------------------------

Veamos ahora cómo escribir datos a un archivo **CSV** usando la función `csv.writer` y la clase `csv.Dictwriter` discutida al inicio de este tutorial.

[Volver al inicio](#-archivos-csv)

### ESCRIBIENDO UN ARCHIVO CSV CON CSV.WRITER

---------------------------------------------------------------------------

El código de abajo escribe los datos definidos al archivo example2.csv.

```python
import csv
 
myData = [["first_name", "second_name", "Grade"],
          ['Alex', 'Brian', 'A'],
          ['Tom', 'Smith', 'B']]
 
myFile = open('./05_Files/Examples/datos_4.csv', 'w', newline='')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)
     
print("Writing complete")
```

Primero importamos el **módulo csv**, y la función `writer()` creará un objeto apto para escritura. Para iterar los datos sobre las filas, necesitaremos usar la función `writerows()`.

Aquí está nuestro CSV con los danos que le hemos escrito.

[Volver al inicio](#-archivos-csv)

### ESCRIBIENDO UN ARCHIVO CSV CON DICTWRITER

---------------------------------------------------------------------------

Escribamos los siguientes datos a un CSV.

```python
data = [{'Grade': 'B', 'first_name': 'Alex', 'last_name': 'Brian'}, 
{'Grade': 'A', 'first_name': 'Rachael', 'last_name': 'Rodriguez'},
{'Grade': 'C', 'first_name': 'Tom', 'last_name': 'smith'},
{'Grade': 'B', 'first_name': 'Jane', 'last_name': 'Oscar'},
{'Grade': 'A', 'first_name': 'Kennzy', 'last_name': 'Tim'}]
```

El código es como se muestra abajo.

```python
import csv
 
with open('./05_Files/Examples/datos_5.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name', 'Grade']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
 
    writer.writeheader()
    writer.writerow({'Grade': 'B', 'first_name': 'Alex', 'last_name': 'Brian'})
    writer.writerow({'Grade': 'A', 'first_name': 'Rachael',
                     'last_name': 'Rodriguez'})
    writer.writerow({'Grade': 'B', 'first_name': 'Jane', 'last_name': 'Oscar'})
    writer.writerow({'Grade': 'B', 'first_name': 'Jane', 'last_name': 'Loive'})
 
print("Writing complete")
```

Primero definimos los `fieldnames`, los cuales representarán los encabezados de cada columna en el archivo **CSV**. El método `writerrow()` escribirá a una fila a la vez. Si quieres escribir todos los datos de una vez, usarás el método `writerrows()`.

Aquí está cómo escribir a todas las filas de una vez.

```python
import csv
 
with open('./05_Files/Examples/datos_6.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name', 'Grade']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
 
    writer.writeheader()
    writer.writerows([{'Grade': 'B', 'first_name': 'Alex', 'last_name': 'Brian'},
                      {'Grade': 'A', 'first_name': 'Rachael',
                          'last_name': 'Rodriguez'},
                      {'Grade': 'C', 'first_name': 'Tom', 'last_name': 'smith'},
                      {'Grade': 'B', 'first_name': 'Jane', 'last_name': 'Oscar'},
                      {'Grade': 'A', 'first_name': 'Kennzy', 'last_name': 'Tim'}])
 
print("writing complete")
```

[Volver al inicio](#-archivos-csv)