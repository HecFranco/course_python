# Claves primarias

Una clave primaria es un campo especial de una tabla que actúa como identificador único de los registros, en otras palabras, no se puede repetir un registro con la misma clave primaria. Por ejemplo dos usuarios con el mismo DNI:

[Volver al inicio](#-claves-primarias)

## PRYMARY KEY

---------------------------------------------------------------------------

```python
# Importamos el módulo
import sqlite3
​# Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
conexion = sqlite3.connect('usuarios.db')
​# Creamos el cursor
cursor = conexion.cursor()
​# Creamos un campo dni como clave primaria
cursor.execute('''CREATE TABLE usuarios (
                    dni VARCHAR(9) PRIMARY KEY,
                    nombre VARCHAR(100), 
                    edad INTEGER,
                    email VARCHAR(100))''')
​usuarios = [('11111111A', 'Hector', 27, 'hector@ejemplo.com'),
            ('22222222B', 'Mario', 51, 'mario@ejemplo.com'),
            ('33333333C', 'Mercedes', 38, 'mercedes@ejemplo.com'),
            ('44444444D', 'Juan', 19, 'juan@ejemplo.com')]
​cursor.executemany("INSERT INTO usuarios VALUES (?,?,?,?)", usuarios)
​conexion.commit()
conexion.close()
```

Si ahora intentamos introducir un registro con un DNI duplicado, saltará un error:

```python
# Importamos el módulo
import sqlite3
​# Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
conexion = sqlite3.connect('usuarios.db')
​# Creamos el cursor
cursor = conexion.cursor()
# Añadimos un usuario con el mismo DNI
cursor.execute("INSERT INTO usuarios VALUES ('11111111A', 'Fernando', 31, 'fernando@ejemplo.com')")
​conexion.commit()
conexion.close()
```

Esto ocurre ya que el campo **dni** debe ser único.

```bash
$ python 62_Database_02_Primary_Key_Unique.py
# ---------------------------------------------------------------------------
# IntegrityError                            Traceback (most recent call last)
# <ipython-input-88-1f8a69b706db> in <module>()
#       6 
#       7 # Añadimos un usuario con el mismo DNI
# ----> 8 cursor.execute("INSERT INTO usuarios VALUES ('11111111A', 'Fernando', 31, 'fernando@ejemplo.com')")
#       9 
#     10 conexion.commit()
# IntegrityError: UNIQUE constraint failed: usuarios.dni
```

[Volver al inicio](#-claves-primarias)

### CAMPOS AUTOINCREMENTALES

---------------------------------------------------------------------------

No siempre contaremos con claves primarias en nuestras tablas (como el DNI), sin embargo siempre necesitaremos uno para identificar cada registro y poder consultarlo, modificarlo o borrarlo.

Para estas situaciones lo más útil es utilizar campos autoincrementales, campos especiales que asignan automáticamente un número (de uno en uno) al crear un nuevo registro. Es muy útil para identificar de forma única cada registro ya que nunca se repiten.

En SQLite, si indicamos que un campo numérico entero es una clave primaria, automáticamente se tomará como un campo auto incremental. Podemos hacerlo fácilmente así:

```python
# Importamos el módulo
import sqlite3
​# Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
conexion = sqlite3.connect('usuarios.db')
​# Creamos el cursor
cursor = conexion.cursor()
# Las cláusulas not null indican que no puede ser campos vacíos
cursor.execute('''CREATE TABLE productos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nombre VARCHAR(100) NOT NULL, 
                    marca VARCHAR(50) NOT NULL, 
                    precio FLOAT NOT NULL)''')
​conexion.close()
```

> **IMPORTANTE**: **¡Problema al insertar registros con campos autoincrementales!** Al utilizar un nuevo campo autoincremental, la sintaxis sencilla para insertar registros ya no funciona, pues en primer lugar se espera un identificador único, por lo que recibimos un error indicándonos se esperan 4 columnas en lugar de 3:

```python
# Importamos el módulo
import sqlite3
​# Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
conexion = sqlite3.connect('usuarios.db')
​# Creamos el cursor
cursor = conexion.cursor()​
productos = [('Teclado', 'Logitech', 19.95),
             ('Pantalla 19"' 'LG', 89.95),]
​cursor.executemany("INSERT INTO productos VALUES (?,?,?)", productos)
​conexion.commit()
conexion.close()
```

Al ejecutarlo obtendremos el siguiente error:

```bash
$ python 62_Database_04_Add_Data_Error_with_Autoincremental_Field.py
Traceback (most recent call last):
  File "62_Database_04_Add_Data_Error_with_Autoincremental_Field.py", line 9, in <module>
    cursor.executemany("INSERT INTO productos VALUES (?,?,?)", productos)
sqlite3.OperationalError: table productos has 4 columns but 3 values were supplied
```

Para arreglarlo cambiaremos la notación durante la inserción, especificando el valor null para el auto incremento:

```python
# Importamos el módulo
import sqlite3
​# Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
conexion = sqlite3.connect('usuarios.db')
​# Creamos el cursor
cursor = conexion.cursor()​
productos = [('Teclado', 'Logitech', 19.95),
             ('Pantalla 19"','LG', 89.95),
             ('Altavoces 2.1','LG', 24.95),]
​cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)
​conexion.commit()
conexion.close()
```

Ahora podemos consultar nuestros productos fácilmente con su identificador único:

```python
# Importamos el módulo
import sqlite3
​# Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
conexion = sqlite3.connect('usuarios.db')
​# Creamos el cursor
cursor = conexion.cursor()​​
# Recuperamos los registros de la tabla de usuarios
cursor.execute("SELECT * FROM productos")
​# Recorremos todos los registros con fetchall, y los volvamos en una lista de usuarios
productos = cursor.fetchall()
​# Ahora podemos recorrer todos los productos
for producto in productos:
    print(producto)
​conexion.close()
```

Obtendremos en consola al ejecutar el script el siguiente resultado:

```bash
$ python 62_Database_06_Fecth_Data.py
(1, 'Teclado', 'Logitech', 19.95)
(2, 'Pantalla 19"', 'LG', 89.95)
(3, 'Altavoces 2.1', 'LG', 24.95)
```

[Volver al inicio](#-claves-primarias)

### CLAVE ÚNICA

---------------------------------------------------------------------------

El problema con las claves primarias es que sólo podemos tener un campo con esta propiedad, y si da la casualidad que utilizamos un campo autoincremental, ya no podemos asignarla a otro campo.

Para estos casos existen las claves únicas, que nos permiten añadir otros campos únicos no repetibles.

Podemos adaptar el ejemplo de los usuarios con un campo autoincremental que haga de clave primaria, y a su vez marcar el DNI como un campo único:

```python
# Importamos el módulo
import sqlite3
​# Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
conexion = sqlite3.connect('usuarios_autoincremental.db')
​# Creamos el cursor
cursor = conexion.cursor()​​
​# Creamos un campo dni como clave primaria
cursor.execute('''CREATE TABLE usuarios (
                    id INTEGER PRIMARY KEY,
                    dni VARCHAR(9) UNIQUE,
                    nombre VARCHAR(100), 
                    edad INTEGER(3),
                    email VARCHAR(100))''')
​usuarios = [('11111111A', 'Hector', 27, 'hector@ejemplo.com'),
            ('22222222B', 'Mario', 51, 'mario@ejemplo.com'),
            ('33333333C', 'Mercedes', 38, 'mercedes@ejemplo.com'),
            ('44444444D', 'Juan', 19, 'juan@ejemplo.com')]
​cursor.executemany("INSERT INTO usuarios VALUES (null, ?,?,?,?)", usuarios)
​conexion.commit()
conexion.close()
```

Si intentamos añadir un usuario con la misma clave da error de integridad:

```python
# Importamos el módulo
import sqlite3
​# Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
conexion = sqlite3.connect('usuarios_autoincremental.db')
​# Creamos el cursor
cursor = conexion.cursor()​​
# Añadimos un usuario con el mismo DNI
cursor.execute("INSERT INTO usuarios VALUES (null, '11111111A', 'Fernando', 31, 'fernando@ejemplo.com')")
​conexion.commit()
conexion.close()
```

Obtendremos el siguiente error al ejecutar el script:

```bash
$ python 63_Database_08_Insert_Unique_Field.py
Traceback (most recent call last):
  File "63_Database_08_Insert_Unique_Field.py", line 8, in <module>
    cursor.execute("INSERT INTO usuarios VALUES (null, '11111111A', 'Fernando', 31, 'fernando@ejemplo.com')")
sqlite3.IntegrityError: UNIQUE constraint failed: usuarios.dni
```

Con la ventaja de contar con un identificador automático para cada registro:

```python
# Importamos el módulo
import sqlite3
​# Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
conexion = sqlite3.connect('usuarios_autoincremental.db')
​# Creamos el cursor
cursor = conexion.cursor()​​
​# Recuperamos los registros de la tabla de usuarios
cursor.execute("SELECT * FROM usuarios")
​# Recorremos todos los registros con fetchall, y los volvamos en una lista de usuarios
usuarios = cursor.fetchall()
​# Ahora podemos recorrer todos los usuarios
for usuario in usuarios:
    print(usuario)
​conexion.close()
```

Al ejecutar el script obtendremos el siguiente resultado:

```bash
$ python 62_Database_09_Select.py
(1, '11111111A', 'Hector', 27, 'hector@ejemplo.com')
(2, '22222222B', 'Mario', 51, 'mario@ejemplo.com')
(3, '33333333C', 'Mercedes', 38, 'mercedes@ejemplo.com')
(4, '44444444D', 'Juan', 19, 'juan@ejemplo.com')
```

> **IMPORTANTE**: **Importancia de los identificadores únicos** Es muy importante contar siempre con identificadores únicos para cada registro, ya que sin ellos nos sería prácticamente imposible editar y borrar campos de forma fácil.

[Volver al inicio](#-claves-primarias)