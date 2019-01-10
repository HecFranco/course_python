# Importamos el módulo
import sqlite3
# Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
conexion = sqlite3.connect('usuarios.db')
# Creamos el cursor
cursor = conexion.cursor()
# Las cláusulas not null indican que no puede ser campos vacíos
cursor.execute('''CREATE TABLE productos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nombre VARCHAR(100) NOT NULL, 
                    marca VARCHAR(50) NOT NULL, 
                    precio FLOAT NOT NULL)''')
conexion.close()