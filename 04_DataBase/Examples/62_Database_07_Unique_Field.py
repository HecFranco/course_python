# Importamos el módulo
import sqlite3
# Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
conexion = sqlite3.connect('usuarios_autoincremental.db')
# Creamos el cursor
cursor = conexion.cursor()
# Creamos un campo dni como clave primaria
cursor.execute('''CREATE TABLE usuarios (
                    id INTEGER PRIMARY KEY,
                    dni VARCHAR(9) UNIQUE,
                    nombre VARCHAR(100), 
                    edad INTEGER(3),
                    email VARCHAR(100))''')
usuarios = [('11111111A', 'Hector', 27, 'hector@ejemplo.com'),
            ('22222222B', 'Mario', 51, 'mario@ejemplo.com'),
            ('33333333C', 'Mercedes', 38, 'mercedes@ejemplo.com'),
            ('44444444D', 'Juan', 19, 'juan@ejemplo.com')]
cursor.executemany("INSERT INTO usuarios VALUES (null, ?,?,?,?)", usuarios)
conexion.commit()
conexion.close()