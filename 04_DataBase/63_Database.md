# Consultando registros específicos

Una vez contamos con algún campo que nos sirva de identificador único, podemos realizar consultas específicas utilizando la cláusula `WHERE`:

[Volver al inicio](#-consultando-registros-específicos)

## CONSULTANDO REGISTROS ESPECÍFICOS

---------------------------------------------------------------------------

```python
# Importamos el módulo
import sqlite3
​# Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
conexion = sqlite3.connect('usuarios_autoincremental.db')
​# Creamos el cursor
cursor = conexion.cursor()
# Recuperamos un registro de la tabla de usuarios
cursor.execute("SELECT * FROM usuarios WHERE id=1")
​usuario = cursor.fetchone()
print(usuario)
​conexion.close()
```

Al ejecutar el script en consola obtendremos el siguiente resultado:

```bash
$ python 63_Database_01_Select.py
# (1, '11111111A', 'Hector', 27, 'hector@ejemplo.com')
```

También podemos buscar sólo algunos campos específicos utilizando el DNI:

```python
# Importamos el módulo
import sqlite3
​# Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
conexion = sqlite3.connect('usuarios_autoincremental.db')
​# Creamos el cursor
cursor = conexion.cursor()
# Recuperamos un registro de la tabla de usuarios
cursor.execute("SELECT nombre, edad, email FROM usuarios WHERE dni='22222222B'")
​usuario = cursor.fetchone()
print(usuario)
​conexion.close()
```

Y obtendremos por consola al ejecutar el script:

```bash
$ python 63_Database_02_Select_by_dni.py
# ('Mario', 51, 'mario@ejemplo.com')
```

[Volver al inicio](#-consultando-registros-específicos)

## MODIFICANDO REGISTROS ESPECÍFICOS

---------------------------------------------------------------------------

De forma similar al `SELECT` podemos utilizar la cláusula:

```python
UPDATE tabla
SET columna1 = valor1, columna2 = valor2...., columnaN = valorN
WHERE [condicion]
```

Modificamos nuestro script:

```python
# Importamos el módulo
import sqlite3
# Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
conexion = sqlite3.connect('usuarios_autoincremental.db')
# Creamos el cursor
cursor = conexion.cursor()
​# Actualizamos un registro
cursor.execute("UPDATE usuarios SET nombre='Hector Costa' WHERE dni='11111111A'")
​# Ahora lo consultamos de nuevo
cursor.execute("SELECT * FROM usuarios WHERE dni='11111111A'")
usuario = cursor.fetchone()
print(usuario)
​conexion.commit()
conexion.close()
```

Y al ejecutarlo en consola obtenemos el siguiente resultado:

```bash
$ python 63_Database_03_Update_by_dni.py
(1, '11111111A', 'Hector Costa', 27, 'hector@ejemplo.com')
```

> **IMPORTANTE**: No olvidar la cláusula `WHERE` o podéis acabar actualizando todos los registros

[Volver al inicio](#-consultando-registros-específicos)

## BORRANDO REGISTROS ESPECÍFICOS

---------------------------------------------------------------------------

Finalmente, para borrar un registro a partir de su id o campo único:

```python
DELETE FROM tabla WHERE [condicion]
```

```python
# Importamos el módulo
import sqlite3
# Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
conexion = sqlite3.connect('usuarios_autoincremental.db')
# Creamos el cursor
cursor = conexion.cursor()
# Creamos un registro de prueba
cursor.execute("INSERT INTO usuarios VALUES (null, '55555555E', 'Fernando', 31, 'fernando@ejemplo.com')")
​# Consultamos los usuarios
for usuario in cursor.execute("SELECT * FROM usuarios"):
    print(usuario)
​# Ahora lo borramos
cursor.execute("DELETE FROM usuarios WHERE dni='55555555E'")
​print() # Espacio en blanco
​# Consultamos de nuevo los usuarios
for usuario in cursor.execute("SELECT * FROM usuarios"):
    print(usuario)
​conexion.commit()
conexion.close()
```

Si ejecutamos el script en consola podremos ver el siguiente resultado:

```bash
$ python 63_Database_04_Delete_by_dni.py
(1, '11111111A', 'Hector Costa', 27, 'hector@ejemplo.com')
(2, '22222222B', 'Mario', 51, 'mario@ejemplo.com')
(3, '33333333C', 'Mercedes', 38, 'mercedes@ejemplo.com')
(4, '44444444D', 'Juan', 19, 'juan@ejemplo.com')
(5, '55555555E', 'Fernando', 31, 'fernando@ejemplo.com')

(1, '11111111A', 'Hector Costa', 27, 'hector@ejemplo.com')
(2, '22222222B', 'Mario', 51, 'mario@ejemplo.com')
(3, '33333333C', 'Mercedes', 38, 'mercedes@ejemplo.com')
(4, '44444444D', 'Juan', 19, 'juan@ejemplo.com')
```

> **NOTA**: **No te olvides el WHERE**. En SQL es posible realizar actualizaciones y borrados en masa, pero las dos últimas son un poco peligrosas. Sin embargo realizarlas es tan sencillo como olvidarnos la cláusula WHERE en el UPDATE o el DELETE.

Canción: No te olvides el `WHERE` en el `DELETE FROM`: 

<iframe width="560" height="315" src="https://www.youtube.com/embed/i_cVJgIz_Cs" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

```python
# Importamos el módulo
import sqlite3
# Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
conexion = sqlite3.connect('usuarios_autoincremental.db')
# Creamos el cursor
cursor = conexion.cursor()
​# Borramos sin el WHERE
cursor.execute("DELETE FROM usuarios")
​# Consultamos de nuevo los usuarios
usuarios = cursor.execute("SELECT * FROM usuarios").fetchall()
print(usuarios)
​conexion.commit()
conexion.close()
```

Si ejecutamos nuestro script obtendremos el siguiente resultado:

```bash
$ python 63_Database_05_Delete_all.py
[]
```

[Volver al inicio](#-consultando-registros-específicos)

## MÁS QUE APRENDER
---------------------------------------------------------------------------

SQL es un lenguaje muy extenso con muchísimas posibilidades. Ya que esta unidad no deja de ser una introducción, te animo a seguir aprendiendo por tu cuenta conceptos tan importantes como:

* **Consultas avanzadas: `or`, `and`, `like`,`join`**
* **Funciones simples: `count`, `group by`, `distinct`**
* **Funciones avanzadas: `sum`, `avg`, `min`, `max`**
* **Manejo de fechas: `date`, `year`, `month`, `day`**
* **Relaciones y claves foráneas**

[Volver al inicio](#-consultando-registros-específicos)