# Importamos el módulo
import sqlite3
# Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
conexion = sqlite3.connect('usuarios_autoincremental.db')
# Creamos el cursor
cursor = conexion.cursor()
# Recuperamos un registro de la tabla de usuarios
cursor.execute("SELECT * FROM usuarios WHERE id=1")
usuario = cursor.fetchone()
print(usuario)
conexion.close()