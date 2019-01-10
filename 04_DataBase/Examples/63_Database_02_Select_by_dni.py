# Importamos el módulo
import sqlite3
# Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
conexion = sqlite3.connect('usuarios_autoincremental.db')
# Creamos el cursor
cursor = conexion.cursor()
# Recuperamos un registro de la tabla de usuarios
cursor.execute("SELECT nombre, edad, email FROM usuarios WHERE dni='22222222B'")
usuario = cursor.fetchone()
print(usuario)
conexion.close()