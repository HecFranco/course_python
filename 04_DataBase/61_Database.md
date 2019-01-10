# Conexión a la base de datos, creación y desconexión

**¿Qué es una base de datos?** También conocidas como **bancos de datos**, son simplemente conjuntos de datos. Ya conocemos algunos tipos de datos, como los números, las cadenas de caracteres, las fechas, etc.

Bueno, pues estos conjuntos de datos hacen referencia a información perteneciente a un mismo contexto. Es decir, si hablamos de los clientes de una empresa, éstos datos comunes de todos los clientes podrían ser sus nombres, apellidos, direcciones, teléfonos… O los productos de una tienda, cada uno con su nombre, precio, descripción, etc.

[Volver al inicio](#-conexión-a-la-base-de-datos-creación-y-desconexión)

## MODELOS

---------------------------------------------------------------------------

De todas formas, los tipos de datos y la forma de almacenarlos pueden diferir mucho dependiendo exactamente del contexto, y es por eso que con el tiempo se han ido desarrollando una serie de modelos distintos para gestionar las bases de datos.

* **Jerárquicas**: Utilizan un modelo los datos que se organiza en forma de árbol invertido, en donde un nodo padre de información puede tener varios hijos...
* **De red**: Una mejora del modelo jerárquico que permite a un hijo tener varios padres...
* **Transaccionales**: Cuyo único fin es el envío y recepción de datos a grandes velocidades, estas bases son muy poco comunes
Relacionales**: Éste es el modelo utilizado en la actualidad para representar problemas reales y administrar datos dinámicamente. Es en el que nos vamos a centrar, pero hay otros...
* **Documentales**: Permiten guardar texto completo, y en líneas generales realizar búsquedas más potentes. Sirven para almacenar grandes volúmenes de información de antecedentes históricos. Junto a las relacionales son de las más utilizadas en el desarrollo web.
* **Orientadas a objetos**: Este modelo es bastante reciente y propio de los modelos informáticos orientados a objetos, donde se trata de almacenar en la base de datos los objetos completos. Es posible que tome más importancia en el futuro.
* **Deductivas**: Son bases de datos que permiten hacer deducciones. Se basan principalmente en reglas y hechos que son almacenados en la base de datos, por lo que son algo complejas.

[Volver al inicio](#-conexión-a-la-base-de-datos-creación-y-desconexión)

## MODELO RELACIONAL

---------------------------------------------------------------------------

Las bases de datos Relacionales son muy utilizadas actualmente gracias a que es fácil representar y gestionar problemas del mundo real.

Se basan en la idea de crear relaciones entre conjuntos de datos, en los que cada relación es también una tabla. Cada tabla consta de registros, formados por filas y columnas, también conocidos como tuplas y campos.

![https://upload.wikimedia.org/wikipedia/commons/e/ed/Diagrama_Empleado.jpeg](https://upload.wikimedia.org/wikipedia/commons/e/ed/Diagrama_Empleado.jpeg)

Evidentemente dentro de las bases de datos relacionales, existen muchos SGBD. La mayoría también son compatibles con Python. Algunos son de pago, otros gratuitos, los hay sencillos y otros muy avanzados. Hagamos un repaso:

[Volver al inicio](#-conexión-a-la-base-de-datos-creación-y-desconexión)

## DB BROWSER

---------------------------------------------------------------------------

Para poder practicar lo que veremos en esta sección deberemos descargar este software, [http://sqlitebrowser.org/](http://sqlitebrowser.org/), que nos permitirá visualizar en tiempo real el estado de la base de datos con la que trabajaremos.

[Volver al inicio](#-conexión-a-la-base-de-datos-creación-y-desconexión)

## BASES DE DATOS SQLITE

---------------------------------------------------------------------------

[Volver al inicio](#-conexión-a-la-base-de-datos-creación-y-desconexión)

### CONEXIÓN BASE DE DATOS

---------------------------------------------------------------------------

```python
# Importamos el módulo
import sqlite3
​# Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
conexion = sqlite3.connect('ejemplo.db')
​# Cerramos la conexión, si no la cerramos se mantendrá en uso y no podremos gestionar el fichero
conexion.close()
```

> **NOTA IMPORTANTE**: Al generar el archivo nuevo, python lo creará en la ruta relativa cn respecto a la ubicación de l ejecución del comando.

[Volver al inicio](#-conexión-a-la-base-de-datos-creación-y-desconexión)

### CREACIÓN DE UNA TABLA UTILIZANDO LA SINTAXIS SQL

---------------------------------------------------------------------------

Antes de ejecutar una consulta (**query**) en código SQL, tenemos que crear un **cursor**.

> **NOTA**: Una vez creada la tabla, si intentamos volver a crearla dará error indicándonos que esta ya existe. **Esto se debe a que no se puede crear una tabla ya creada con anterioridad.**

```python
# Importamos el módulo
import sqlite3
​# Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
conexion = sqlite3.connect('ejemplo.db')
​# Creamos el cursor
cursor = conexion.cursor()
​# Ahora crearemos una tabla de usuarios para almacenar nombres, edades y emails
cursor.execute("CREATE TABLE usuarios (nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))")
​# Guardamos los cambios haciendo un commit
conexion.commit()
​conexion.close()
```

> **NOTA**: Al ejecutar el script por segunda vez, ya creada la tabla obtendremos el siguiente resultado.

```bash
# ---------------------------------------------------------------------------
# OperationalError                          Traceback (most recent call last)
# <ipython-input-14-279f8cd3e83f> in <module>()
#       7 
#       8 # Ahora crearemos una tabla de usuarios para almacenar nombres, edades y emails
# ----> 9 cursor.execute("CREATE TABLE usuarios (nombre text, edad int, email text)")
#      10 
#      11 # Guardamos los cambios haciendo un commit
# OperationalError: table usuarios already exists
```

[Volver al inicio](#-conexión-a-la-base-de-datos-creación-y-desconexión)

### INSERTANDO UN REGISTRO

---------------------------------------------------------------------------

```python
# Importamos el módulo
import sqlite3
​# Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
conexion = sqlite3.connect('ejemplo.db')
​# Creamos el cursor
cursor = conexion.cursor()
# Insertamos un registro en la tabla de usuarios
cursor.execute("INSERT INTO usuarios VALUES ('Hector', 27, 'hector@ejemplo.com')")
​# Guardamos los cambios haciendo un commit
conexion.commit()
​conexion.close()
```

> **NOTA**: Si accedemos al inspector de **base de datos** instalado, y accedemos a **Navegar Datos**, veremos que tenemos un nuevo registro.

[Volver al inicio](#-conexión-a-la-base-de-datos-creación-y-desconexión)

### RECUPERANDO EL PRIMER REGISTRO CON .FETCHONE()

---------------------------------------------------------------------------

```python
# Importamos el módulo
import sqlite3
​# Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
conexion = sqlite3.connect('ejemplo.db')
​# Creamos el cursor
cursor = conexion.cursor()
​# Recuperamos los registros de la tabla de usuarios
cursor.execute("SELECT * FROM usuarios")
​# Mostrar el cursos a ver que hay ?
print(cursor)
​# Recorremos el primer registro con el método fetchone, devuelve una tupla
usuario = cursor.fetchone()
print(usuario)
​conexion.close()
```

Al ejecutar el script obtendremos la siguiente respuesta:

```bash
$ python 61_Database_04_Fetch_Data.py
<sqlite3.Cursor object at 0x02BC4E60>
('Hector', 27, 'hector@ejemplo.com')
```

[Volver al inicio](#-conexión-a-la-base-de-datos-creación-y-desconexión)

### INSERTANDO VARIOS REGISTROS CON .EXECUTEMANY()

---------------------------------------------------------------------------

```python
# Importamos el módulo
import sqlite3
# Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
conexion = sqlite3.connect('ejemplo.db')
# Creamos el cursor
cursor = conexion.cursor()
​# Creamos una lista con varios usuarios
usuarios = [('Mario', 51, 'mario@ejemplo.com'),
            ('Mercedes', 38, 'mercedes@ejemplo.com'),
            ('Juan', 19, 'juan@ejemplo.com'),
            ]
​# Ahora utilizamos el método executemany() para insertar varios
cursor.executemany("INSERT INTO usuarios VALUES (?,?,?)", usuarios)
​# Guardamos los cambios haciendo un commit
conexion.commit()
​conexion.close()
```

[Volver al inicio](#-conexión-a-la-base-de-datos-creación-y-desconexión)

### RECUPERANDO VARIOS REGISTROS CON .FETCHALL()

---------------------------------------------------------------------------

```python
# Importamos el módulo
import sqlite3
# Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
conexion = sqlite3.connect('ejemplo.db')
# Creamos el cursor
cursor = conexion.cursor()
​# Recuperamos los registros de la tabla de usuarios
cursor.execute("SELECT * FROM usuarios")
​# Recorremos todos los registros con fetchall, y los volvamos en una lista de usuarios
usuarios = cursor.fetchall()
​# Ahora podemos recorrer todos los usuarios
for usuario in usuarios:
    print(usuario)
​conexion.close()
('Hector', 27, 'hector@ejemplo.com')
('Mario', 51, 'mario@ejemplo.com')
('Mercedes', 38, 'mercedes@ejemplo.com')
('Juan', 19, 'juan@ejemplo.com')
```

Al ejecutar nuestro script obtendremos el siguiente resultado:

```bash
$ python 61_Database_06_Fecth_Many_Data.py
('Hector', 27, 'hector@ejemplo.com')
('Mario', 51, 'mario@ejemplo.com')
('Mercedes', 38, 'mercedes@ejemplo.com')
('Juan', 19, 'juan@ejemplo.com')
```

[Volver al inicio](#-conexión-a-la-base-de-datos-creación-y-desconexión)