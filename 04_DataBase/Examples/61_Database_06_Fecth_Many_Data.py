# Importamos el módulo
import sqlite3
# Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
conexion = sqlite3.connect('ejemplo.db')
# Creamos el cursor
cursor = conexion.cursor()
# Recuperamos los registros de la tabla de usuarios
cursor.execute("SELECT * FROM usuarios")
# Recorremos todos los registros con fetchall, y los volvamos en una lista de usuarios
usuarios = cursor.fetchall()
# Ahora podemos recorrer todos los usuarios
for usuario in usuarios:
    print(usuario)
conexion.close()
# ('Hector', 27, 'hector@ejemplo.com')
# ('Mario', 51, 'mario@ejemplo.com')
# ('Mercedes', 38, 'mercedes@ejemplo.com')
# ('Juan', 19, 'juan@ejemplo.com')