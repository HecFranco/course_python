# BLOQUE 14: Bases de datos con SQLite (Enunciados)

> **NOTA**: Estos ejercicios son optativos para hacer al final de la unidad y están pensados para apoyar tu aprendizaje.

> **NOTA IMPORTANTE**: Todos los ejercicios deberás realizarlos en scripts creados en el mismo directorio donde trabajarás con las bases de datos.

**1.1) A lo largo de estos ejercicios vamos a crear un pequeño sistema para gestionar los platos del menú de un restaurante. Por ahora debes empezar creando un script llamado restaurante.py y dentro una función crear_bd() que creará una pequeña base de datos restaurante.db con las siguientes dos tablas:**

* **Si ya existen deberá tratar la excepción y mostrar que las tablas ya existen. En caso contrario mostrará que se han creado correctamente.**

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

> **NOTA:** La línea `FOREIGN KEY(categoria_id) REFERENCES categoria(id)` indica un tipo de clave especial (foránea), por la cual se crea una relación entre la categoría de un plato con el registro de categorías.

**Llama a la función y comprueba que la base de datos se crea correctamente.**

**1.2) Crea una función llamada `agregar_categoria()` que pida al usuario un nombre de categoría y se encargue de crear la categoría en la base de datos (ten en cuenta que si ya existe dará un error, por que el nombre es `UNIQUE`).**

Ahora, crea un pequeño menú de opciones dentro del script, que te de la bienvenida al sistema y te permita Crear una categoría o Salir. Añade las siguientes tres categorías utilizando este menú de opciones:

* Primeros
* Segundos
* Postres

**1.3) Crea una función llamada `agregar_plato()` que muestre al usuario las categorías disponibles y le permita escoger una (escribiendo un número).**

Luego le pedirá introducir el nombre del plato y lo añadirá a la base de datos, teniendo en cuenta que la categoria del plato concuerde con el id de la categoría y que el nombre del plato no puede repetirse (no es necesario comprobar si la categoría realmente existe, en ese caso simplemente no se insertará el plato).

Agrega la nueva opción al menú de opciones y añade los siguientes platos:

* **Primeros**: Ensalada del tiempo / Zumo de tomate
* **Segundos**: Estofado de pescado / Pollo con patatas
* **Postres**: Flan con nata / Fruta del tiempo

**1.4)** Crea una función llamada `mostrar_menu()` que muestre el menú con todos los platos de forma ordenada: los primeros, los segundos y los postres. Optativamente puedes adornar la forma en que muestras el menú por pantalla.