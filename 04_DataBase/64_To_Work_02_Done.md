# BLOQUE 14: Bases de datos con SQLite (Enunciados)

> **NOTA**: Estos ejercicios son optativos para hacer al final de la unidad y están pensados para apoyar tu aprendizaje.

> **NOTA IMPORTANTE**: Todos los ejercicios deberás realizarlos en scripts creados en el mismo directorio donde trabajarás con las bases de datos.

**1.1) A lo largo de estos ejercicios vamos a crear un pequeño sistema para gestionar los platos del menú de un restaurante. Por ahora debes empezar creando un script llamado `restaurante.py` y dentro una función `crear_bd()` que creará una pequeña base de datos `restaurante.db` con las siguientes dos tablas:**

```sql
CREATE TABLE categoria(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL)
CREATE TABLE plato(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL, 
                categoria_id INTEGER NOT NULL,
                FOREIGN KEY(categoria_id) REFERENCES categoria(id))
```

* **Si ya existen deberá tratar la excepción y mostrar que las tablas ya existen. En caso contrario mostrará que se han creado correctamente.**



> **NOTA:** La línea `FOREIGN KEY(categoria_id) REFERENCES categoria(id)` indica un tipo de clave especial (foránea), por la cual se crea una relación entre la categoría de un plato con el registro de categorías.

**Llama a la función y comprueba que la base de datos se crea correctamente.**

**PASOS A SEGUIR**

1. Importamos la librería `sqlite3`:

```python
import sqlite3
```

2. Creamos nuestra función llamada `crear_bd()`:

```diff
import sqlite3

++ def crear_bd():
```

3. Conectamos con la base de datos y definimos el cursor:


```diff
import sqlite3

def crear_bd():
++  conexion = sqlite3.connect("restaurante.db")
++  cursor = conexion.cursor()
```

4. Cerramos la conexión:

```diff
import sqlite3

def crear_bd():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
++  conexion.close()
```

5. Añadimos la excepción para la creación de la primera tabla:

```diff
import sqlite3

def crear_bd():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

++  try:
++      cursor.execute('''CREATE TABLE categoria(
++              id INTEGER PRIMARY KEY AUTOINCREMENT,
++              nombre VARCHAR(100) UNIQUE NOT NULL)''')
++  except sqlite3.OperationalError:
++      print("La tabla de Categorías ya existe.")
++  else:
++      print("La tabla de Categorías se ha creado correctamente.")
    conexion.close()
```

6. Añadimos la excepción en la creación de la segunda tabla:

```diff
import sqlite3

def crear_bd():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    try:
        cursor.execute('''CREATE TABLE categoria(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL)''')
    except sqlite3.OperationalError:
        print("La tabla de Categorías ya existe.")
    else:
        print("La tabla de Categorías se ha creado correctamente.")

++  try:
++      cursor.execute('''CREATE TABLE plato(
++              id INTEGER PRIMARY KEY AUTOINCREMENT,
++              nombre VARCHAR(100) UNIQUE NOT NULL, 
++              categoria_id INTEGER NOT NULL,
++              FOREIGN KEY(categoria_id) REFERENCES categoria(id))''')
++  except sqlite3.OperationalError:
++      print("La tabla de Platos ya existe.")
++  else:
++      print("La tabla de Platos se ha creado correctamente.")

    conexion.close()
```

7. Ejecutamos el método creado:

```diff
import sqlite3

def crear_bd():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    try:
        cursor.execute('''CREATE TABLE categoria(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL)''')
    except sqlite3.OperationalError:
        print("La tabla de Categorías ya existe.")
    else:
        print("La tabla de Categorías se ha creado correctamente.")

    try:
        cursor.execute('''CREATE TABLE plato(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL, 
                categoria_id INTEGER NOT NULL,
                FOREIGN KEY(categoria_id) REFERENCES categoria(id))''')
    except sqlite3.OperationalError:
        print("La tabla de Platos ya existe.")
    else:
        print("La tabla de Platos se ha creado correctamente.")


    conexion.close()
    
++ # Crear la base de datos
++ crear_bd()
```

El código final será así:

```python
import sqlite3

def crear_bd():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    try:
        cursor.execute('''CREATE TABLE categoria(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL)''')
    except sqlite3.OperationalError:
        print("La tabla de Categorías ya existe.")
    else:
        print("La tabla de Categorías se ha creado correctamente.")

    try:
        cursor.execute('''CREATE TABLE plato(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL, 
                categoria_id INTEGER NOT NULL,
                FOREIGN KEY(categoria_id) REFERENCES categoria(id))''')
    except sqlite3.OperationalError:
        print("La tabla de Platos ya existe.")
    else:
        print("La tabla de Platos se ha creado correctamente.")


    conexion.close()
    
# Crear la base de datos
crear_bd()
```

**1.2) Crea una función llamada `agregar_categoria()` que pida al usuario un nombre de categoría y se encargue de crear la categoría en la base de datos (ten en cuenta que si ya existe dará un error, por que el nombre es `UNIQUE`).**

Ahora, crea un pequeño menú de opciones dentro del script, que te de la bienvenida al sistema y te permita Crear una categoría o Salir. Añade las siguientes tres categorías utilizando este menú de opciones:

* Primeros
* Segundos
* Postres

**PASOS A SEGUIR**

1. Definimos la segunda función:

```diff
import sqlite3

def crear_bd():
    # Done

++ def agregar_categoria():
```

2. Conectamos con la base de datos y definimos el cursor:


```diff
import sqlite3

def crear_bd():
    # Done

def agregar_categoria():
++  conexion = sqlite3.connect("restaurante.db")
++  cursor = conexion.cursor()

# Crear la base de datos
crear_bd()
```

3. Cerramos la conexión:

```diff
import sqlite3

def crear_bd():
    # Done

def agregar_categoria():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
++  conexion.close()

# Crear la base de datos
crear_bd()
```

4. Capturamos el primer dato del usuario:

```diff
import sqlite3

def crear_bd():
    # Done

def agregar_categoria():
++  categoria = input("¿Nombre de la nueva categoría?\n> ")
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    conexion.close()
  
# Crear la base de datos
crear_bd()
```

5. Incluimos la gestión de excepciones:

```diff
import sqlite3

def crear_bd():
    # Done

def agregar_categoria():
    categoria = input("¿Nombre de la nueva categoría?\n> ")

    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

++  try:
++      cursor.execute("INSERT INTO categoria VALUES (null, '{}')".format(categoria) )
++  except sqlite3.IntegrityError:
++      print("La categoría '{}' ya existe.".format(categoria))
++  else:
++      print("Categoría '{}' creada correctamente.".format(categoria))

    conexion.close()

# Crear la base de datos
crear_bd()
```

6. Commiteamos los datos:

```diff
import sqlite3

def crear_bd():
    # Done

def agregar_categoria():
    categoria = input("¿Nombre de la nueva categoría?\n> ")

    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    try:
        cursor.execute("INSERT INTO categoria VALUES (null, '{}')".format(categoria) )
    except sqlite3.IntegrityError:
        print("La categoría '{}' ya existe.".format(categoria))
    else:
        print("Categoría '{}' creada correctamente.".format(categoria))

++  conexion.commit()
    conexion.close()

# Crear la base de datos
crear_bd()
```

7. Creamos el menú de selección:

```diff
import sqlite3

def crear_bd():
    # Done

def agregar_categoria():
    # Done

# Crear la base de datos
crear_bd()

# Menú de opciones del programa
++ while True:
++     print("\nBienvenido al gestor del restaurante!")
++     opcion = input(
++         "\nIntroduce una opción:" \
++         "\n[1] Agregar una categoría" \
++         "\n[4] Salir del programa\n\n> ")

++     if opcion == "1":
++         agregar_categoria()

++     elif opcion == "4":
++         print("Nos vemos!")
++         break

++     else:
++         print("Opción incorrecta")
```

El código final será así:

```python
import sqlite3

def crear_bd():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    try:
        cursor.execute('''CREATE TABLE categoria(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL)''')
    except sqlite3.OperationalError:
        print("La tabla de Categorías ya existe.")
    else:
        print("La tabla de Categorías se ha creado correctamente.")

    try:
        cursor.execute('''CREATE TABLE plato(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL, 
                categoria_id INTEGER NOT NULL,
                FOREIGN KEY(categoria_id) REFERENCES categoria(id))''')
    except sqlite3.OperationalError:
        print("La tabla de Platos ya existe.")
    else:
        print("La tabla de Platos se ha creado correctamente.")


    conexion.close()


def agregar_categoria():
    categoria = input("¿Nombre de la nueva categoría?\n> ")

    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    try:
        cursor.execute("INSERT INTO categoria VALUES (null, '{}')".format(categoria) )
    except sqlite3.IntegrityError:
        print("La categoría '{}' ya existe.".format(categoria))
    else:
        print("Categoría '{}' creada correctamente.".format(categoria))

    conexion.commit()
    conexion.close()

# Crear la base de datos
crear_bd()

# Menú de opciones del programa
while True:
    print("\nBienvenido al gestor del restaurante!")
    opcion = input(
        "\nIntroduce una opción:" \
        "\n[1] Agregar una categoría" \
        "\n[4] Salir del programa\n\n> ")

    if opcion == "1":
        agregar_categoria()

    elif opcion == "4":
        print("Nos vemos!")
        break

    else:
        print("Opción incorrecta")
```

**1.3) Crea una función llamada `agregar_plato()` que muestre al usuario las categorías disponibles y le permita escoger una (escribiendo un número).**

Luego le pedirá introducir el nombre del plato y lo añadirá a la base de datos, teniendo en cuenta que la categoria del plato concuerde con el id de la categoría y que el nombre del plato no puede repetirse (no es necesario comprobar si la categoría realmente existe, en ese caso simplemente no se insertará el plato).

Agrega la nueva opción al menú de opciones y añade los siguientes platos:

* **Primeros**: Ensalada del tiempo / Zumo de tomate
* **Segundos**: Estofado de pescado / Pollo con patatas
* **Postres**: Flan con nata / Fruta del tiempo

**PASOS A SEGUIR**

1. Definimos la tercera función:

```diff
import sqlite3

def crear_bd():
    # Done

def agregar_categoria():
    # Done

++ def agregar_plato():

# Crear la base de datos
crear_bd()

# Menú de opciones del programa
while True:
        # Done
```

2. Conectamos con la Base de datos, definimos el cursor y cerramos la conexión:

```diff
import sqlite3

def crear_bd():
    # Done

def agregar_categoria():
    # Done

def agregar_plato():
++   conexion = sqlite3.connect("restaurante.db")
++   cursor = conexion.cursor()

++  conexion.close()

# Crear la base de datos
crear_bd()

# Menú de opciones del programa
while True:
        # Done
```

3. Buscamos todas las categorías existentes, y las recorremos mostrándolas:

```diff
import sqlite3

def crear_bd():
    # Done

def agregar_categoria():
    # Done

def agregar_plato():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

++  categorias = cursor.execute("SELECT * FROM categoria").fetchall()
++  print("Selecciona una categoría para añadir el plato:")
++  for categoria in categorias:
++      print("[{}] {}".format(categoria[0], categoria[1]))

    conexion.close()

# Crear la base de datos
crear_bd()

# Menú de opciones del programa
while True:
        # Done
```

4. Capturamos la categoría de nuestro nuevo plato:

```diff
import sqlite3

def crear_bd():
    # Done

def agregar_categoria():
    # Done

def agregar_plato():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    categorias = cursor.execute("SELECT * FROM categoria").fetchall()
    print("Selecciona una categoría para añadir el plato:")
    for categoria in categorias:
        print("[{}] {}".format(categoria[0], categoria[1]))

++  categoria_usuario = int(input("> "))

    conexion.close()

# Crear la base de datos
crear_bd()

# Menú de opciones del programa
while True:
        # Done
```

5. Capturamos el nombre de nuestro nuevo plato:

```diff
import sqlite3

def crear_bd():
    # Done

def agregar_categoria():
    # Done

def agregar_plato():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    categorias = cursor.execute("SELECT * FROM categoria").fetchall()
    print("Selecciona una categoría para añadir el plato:")
    for categoria in categorias:
        print("[{}] {}".format(categoria[0], categoria[1]))

    categoria_usuario = int(input("> "))

++  plato = input("¿Nombre del nuevo plato?\n> ")

    conexion.close()

# Crear la base de datos
crear_bd()

# Menú de opciones del programa
while True:
        # Done
```

6. Definimos la excepción que introduzca el dato en la bd:

```diff
import sqlite3

def crear_bd():
    # Done

def agregar_categoria():
    # Done

def agregar_plato():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    categorias = cursor.execute("SELECT * FROM categoria").fetchall()
    print("Selecciona una categoría para añadir el plato:")
    for categoria in categorias:
        print("[{}] {}".format(categoria[0], categoria[1]))

    categoria_usuario = int(input("> "))

    plato = input("¿Nombre del nuevo plato?\n> ")

++  try:
++      cursor.execute("INSERT INTO plato VALUES (null, '{}', {})".format(
++          plato, categoria_usuario) )
++  except sqlite3.IntegrityError:
++      print("El plato '{}' ya existe.".format(plato))
++  else:
++      print("Plato '{}' creado correctamente.".format(plato))


    conexion.commit()
    conexion.close()

# Crear la base de datos
crear_bd()

# Menú de opciones del programa
while True:
        # Done
```

7. Comiteamos el dato:

```diff
import sqlite3

def crear_bd():
    # Done

def agregar_categoria():
    # Done

def agregar_plato():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    categorias = cursor.execute("SELECT * FROM categoria").fetchall()
    print("Selecciona una categoría para añadir el plato:")
    for categoria in categorias:
        print("[{}] {}".format(categoria[0], categoria[1]))

    categoria_usuario = int(input("> "))

    plato = input("¿Nombre del nuevo plato?\n> ")

    try:
        cursor.execute("INSERT INTO plato VALUES (null, '{}', {})".format(
            plato, categoria_usuario) )
    except sqlite3.IntegrityError:
        print("El plato '{}' ya existe.".format(plato))
    else:
        print("Plato '{}' creado correctamente.".format(plato))

++  conexion.commit()
    conexion.close()

# Crear la base de datos
crear_bd()

# Menú de opciones del programa
while True:
        # Done
```

8. Modificamos el `while` que gestiona el menú para incluir la opción de incluir plato:

```diff
import sqlite3

def crear_bd():
    # Done

def agregar_categoria():
    # Done

def agregar_plato():
    # Done

# Crear la base de datos
crear_bd()

# Menú de opciones del programa
while True:
    print("\nBienvenido al gestor del restaurante!")
    opcion = input(
        "\nIntroduce una opción:" \
        "\n[1] Agregar una categoría" \
++      "\n[2] Agregar un plato" \
        "\n[4] Salir del programa\n\n> ")

    if opcion == "1":
        agregar_categoria()

++  elif opcion == "2":
++      agregar_plato()

    elif opcion == "4":
        print("Nos vemos!")
        break

    else:
        print("Opción incorrecta")
```

El código final será así:

```python
import sqlite3

def crear_bd():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    try:
        cursor.execute('''CREATE TABLE categoria(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL)''')
    except sqlite3.OperationalError:
        print("La tabla de Categorías ya existe.")
    else:
        print("La tabla de Categorías se ha creado correctamente.")

    try:
        cursor.execute('''CREATE TABLE plato(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL, 
                categoria_id INTEGER NOT NULL,
                FOREIGN KEY(categoria_id) REFERENCES categoria(id))''')
    except sqlite3.OperationalError:
        print("La tabla de Platos ya existe.")
    else:
        print("La tabla de Platos se ha creado correctamente.")


    conexion.close()


def agregar_categoria():
    categoria = input("¿Nombre de la nueva categoría?\n> ")

    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    try:
        cursor.execute("INSERT INTO categoria VALUES (null, '{}')".format(
            categoria) )
    except sqlite3.IntegrityError:
        print("La categoría '{}' ya existe.".format(categoria))
    else:
        print("Categoría '{}' creada correctamente.".format(categoria))

    conexion.commit()
    conexion.close()


def agregar_plato():

    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    categorias = cursor.execute("SELECT * FROM categoria").fetchall()
    print("Selecciona una categoría para añadir el plato:")
    for categoria in categorias:
        print("[{}] {}".format(categoria[0], categoria[1]))

    categoria_usuario = int(input("> "))

    plato = input("¿Nombre del nuevo plato?\n> ")

    try:
        cursor.execute("INSERT INTO plato VALUES (null, '{}', {})".format(
            plato, categoria_usuario) )
    except sqlite3.IntegrityError:
        print("El plato '{}' ya existe.".format(plato))
    else:
        print("Plato '{}' creado correctamente.".format(plato))


    conexion.commit()
    conexion.close()


# Crear la base de datos
crear_bd()

# Menú de opciones del programa
while True:
    print("\nBienvenido al gestor del restaurante!")
    opcion = input(
        "\nIntroduce una opción:" \
        "\n[1] Agregar una categoría" \
        "\n[2] Agregar un plato" \
        "\n[4] Salir del programa\n\n> ")

    if opcion == "1":
        agregar_categoria()

    elif opcion == "2":
        agregar_plato()

    elif opcion == "4":
        print("Nos vemos!")
        break

    else:
        print("Opción incorrecta")
```

**1.4) Crea una función llamada `mostrar_menu()` que muestre el menú con todos los platos de forma ordenada: los primeros, los segundos y los postres. Optativamente puedes adornar la forma en que muestras el menú por pantalla.**

**PASOS A SEGUIR**

1. Definimos la cuarta función:

```diff
import sqlite3

def crear_bd():
    # Done

def agregar_categoria():
    # Done

def agregar_plato():
    # Done

++ def mostrar_menu():

# Crear la base de datos
crear_bd()

# Menú de opciones del programa
while True:
    # Done
```

2. Conectamos con la Base de datos, definimos el cursor y cerramos la conexión:

```diff
import sqlite3

def crear_bd():
    # Done

def agregar_categoria():
    # Done

def agregar_plato():
    # Done

def mostrar_menu():
++   conexion = sqlite3.connect("restaurante.db")
++   cursor = conexion.cursor()

++  conexion.close()

# Crear la base de datos
crear_bd()

# Menú de opciones del programa
while True:
    # Done
```

3. Incluimos la lógica que busque todos los registros en categoría y los recorra mostrando el nombre junto al listado de sus platos:

```diff
import sqlite3

def crear_bd():
    # Done

def agregar_categoria():
    # Done

def agregar_plato():
    # Done

def mostrar_menu():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
++  categorias = cursor.execute("SELECT * FROM categoria").fetchall()   
++  for categoria in categorias:
++      print(categoria[1])
++      platos = cursor.execute(
++          "SELECT * FROM plato WHERE categoria_id={}".format(categoria[0])).fetchall()
++      for plato in platos:
++          print("\t{}".format(plato[1]))

    conexion.close()

# Crear la base de datos
crear_bd()

# Menú de opciones del programa
while True:
    # Done
```

El código final será así:

```python
import sqlite3

def crear_bd():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    try:
        cursor.execute('''CREATE TABLE categoria(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL)''')
    except sqlite3.OperationalError:
        print("La tabla de Categorías ya existe.")
    else:
        print("La tabla de Categorías se ha creado correctamente.")

    try:
        cursor.execute('''CREATE TABLE plato(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL, 
                categoria_id INTEGER NOT NULL,
                FOREIGN KEY(categoria_id) REFERENCES categoria(id))''')
    except sqlite3.OperationalError:
        print("La tabla de Platos ya existe.")
    else:
        print("La tabla de Platos se ha creado correctamente.")


    conexion.close()


def agregar_categoria():
    categoria = input("¿Nombre de la nueva categoría?\n> ")

    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    try:
        cursor.execute("INSERT INTO categoria VALUES (null, '{}')".format(
            categoria) )
    except sqlite3.IntegrityError:
        print("La categoría '{}' ya existe.".format(categoria))
    else:
        print("Categoría '{}' creada correctamente.".format(categoria))

    conexion.commit()
    conexion.close()


def agregar_plato():

    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    categorias = cursor.execute("SELECT * FROM categoria").fetchall()
    print("Selecciona una categoría para añadir el plato:")
    for categoria in categorias:
        print("[{}] {}".format(categoria[0], categoria[1]))

    categoria_usuario = int(input("> "))

    plato = input("¿Nombre del nuevo plato?\n> ")

    try:
        cursor.execute("INSERT INTO plato VALUES (null, '{}', {})".format(
            plato, categoria_usuario) )
    except sqlite3.IntegrityError:
        print("El plato '{}' ya existe.".format(plato))
    else:
        print("Plato '{}' creado correctamente.".format(plato))


    conexion.commit()
    conexion.close()


def mostrar_menu():

    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()  

    categorias = cursor.execute("SELECT * FROM categoria").fetchall()   
    for categoria in categorias:
        print(categoria[1])
        platos = cursor.execute(
            "SELECT * FROM plato WHERE categoria_id={}".format(categoria[0])).fetchall()
        for plato in platos:
            print("\t{}".format(plato[1]))

    conexion.close()


# Crear la base de datos
crear_bd()

# Menú de opciones del programa
while True:
    print("\nBienvenido al gestor del restaurante!")
    opcion = input(
        "\nIntroduce una opción:" \
        "\n[1] Agregar una categoría" \
        "\n[2] Agregar un plato" \
        "\n[3] Mostrar el menú" \
        "\n[4] Salir del programa\n\n> ")

    if opcion == "1":
        agregar_categoria()

    elif opcion == "2":
        agregar_plato()

    elif opcion == "3":
        mostrar_menu()

    elif opcion == "4":
        print("Nos vemos!")
        break

    else:
        print("Opción incorrecta")
```