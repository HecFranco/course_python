# Importamos el módulo
import sqlite3
# Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
conexion = sqlite3.connect('usuarios_autoincremental.db')
# Creamos el cursor
cursor = conexion.cursor()
# Actualizamos un registro
cursor.execute("UPDATE usuarios SET nombre='Hector Costa' WHERE dni='11111111A'")
# Ahora lo consultamos de nuevo
cursor.execute("SELECT * FROM usuarios WHERE dni='11111111A'")
usuario = cursor.fetchone()
print(usuario)
conexion.commit()
conexion.close()