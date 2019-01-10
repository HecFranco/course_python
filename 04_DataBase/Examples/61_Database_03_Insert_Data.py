# Importamos el módulo
import sqlite3
# Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
conexion = sqlite3.connect('ejemplo.db')
# Creamos el cursor
cursor = conexion.cursor()
# Insertamos un registro en la tabla de usuarios
cursor.execute("INSERT INTO usuarios VALUES ('Hector', 27, 'hector@ejemplo.com')")
# Guardamos los cambios haciendo un commit
conexion.commit()
conexion.close()