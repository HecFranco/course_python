# Importamos el módulo
import sqlite3
# Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
conexion = sqlite3.connect('usuarios.db')
# Creamos el cursor
cursor = conexion.cursor()
# Añadimos un usuario con el mismo DNI
cursor.execute("INSERT INTO usuarios VALUES ('11111111A', 'Fernando', 31, 'fernando@ejemplo.com')")
conexion.commit()
conexion.close()