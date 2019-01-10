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