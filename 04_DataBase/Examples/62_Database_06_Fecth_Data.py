# Importamos el módulo
import sqlite3
# Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
conexion = sqlite3.connect('usuarios.db')
# Creamos el cursor
cursor = conexion.cursor()
# Recuperamos los registros de la tabla de usuarios
cursor.execute("SELECT * FROM productos")
# Recorremos todos los registros con fetchall, y los volvamos en una lista de usuarios
productos = cursor.fetchall()
# Ahora podemos recorrer todos los productos
for producto in productos:
    print(producto)
conexion.close()