# Importamos el módulo
import sqlite3
# Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
conexion = sqlite3.connect('usuarios_autoincremental.db')
# Creamos el cursor
cursor = conexion.cursor()
# Borramos sin el WHERE
cursor.execute("DELETE FROM usuarios")
# Consultamos de nuevo los usuarios
usuarios = cursor.execute("SELECT * FROM usuarios").fetchall()
print(usuarios)
conexion.commit()
conexion.close()