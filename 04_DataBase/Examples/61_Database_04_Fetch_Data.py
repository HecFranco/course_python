# Importamos el módulo
import sqlite3
# Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
conexion = sqlite3.connect('ejemplo.db')
# Creamos el cursor
cursor = conexion.cursor()
# Recuperamos los registros de la tabla de usuarios
cursor.execute("SELECT * FROM usuarios")
# Mostrar el cursos a ver que hay ?
print(cursor)
# Recorremos el primer registro con el método fetchone, devuelve una tupla
usuario = cursor.fetchone()
print(usuario)
conexion.close()