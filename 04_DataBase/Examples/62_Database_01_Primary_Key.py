# Importamos el módulo
import sqlite3
# Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
conexion = sqlite3.connect('usuarios.db')
# Creamos el cursor
cursor = conexion.cursor()
# Creamos un campo dni como clave primaria
cursor.execute('''CREATE TABLE usuarios (
                    dni VARCHAR(9) PRIMARY KEY,
                    nombre VARCHAR(100), 
                    edad INTEGER,
                    email VARCHAR(100))''')
usuarios = [('11111111A', 'Hector', 27, 'hector@ejemplo.com'),
            ('22222222B', 'Mario', 51, 'mario@ejemplo.com'),
            ('33333333C', 'Mercedes', 38, 'mercedes@ejemplo.com'),
            ('44444444D', 'Juan', 19, 'juan@ejemplo.com')]
cursor.executemany("INSERT INTO usuarios VALUES (?,?,?,?)", usuarios)
conexion.commit()
conexion.close()