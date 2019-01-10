# Importamos el módulo
import sqlite3
# Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
conexion = sqlite3.connect('usuarios.db')
# Creamos el cursor
cursor = conexion.cursor()
productos = [('Teclado', 'Logitech', 19.95),
             ('Pantalla 19"' 'LG', 89.95),]
cursor.executemany("INSERT INTO productos VALUES (?,?,?)", productos)
conexion.commit()
conexion.close()