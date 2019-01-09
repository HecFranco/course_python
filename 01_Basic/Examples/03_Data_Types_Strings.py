print('Hola Mundo')
# 'Hola Mundo'
print("Hola Mundo")
# 'Hola Mundo'
print('Este texto incluye unas " " ')
# 'Este texto incluye unas " " '
print("Esta 'palabra' se encuentra escrita entre comillas simples")
# "Esta 'palabra' se encuentra escrita entre comillas simples"
print("Esta \"palabra\" se encuentra escrita entre comillas dobles")
# 'Esta "palabra" se encuentra escrita entre comillas dobles'
print('Esta \'palabra\' se encuentra escrita entre comillas dobles')
# "Esta 'palabra' se encuentra escrita entre comillas dobles"
print("Una cadena")
# 'Una cadena'
print('otra cadena')
# 'otra cadena'
print('otra cadena más')
# 'otra cadena más'
print("Un texto\tuna tabulación")
# Un texto	una tabulación
print("Un texto\nuna nueva línea")
# Un texto
# una nueva línea
print("C:\nombre\directorio")
# C:
# ombre\directorio
print(r"C:\nombre\directorio")  # r => raw (cruda)
# C:\nombre\directorio
print("""Una línea
otra línea
otra línea\tuna tabulación""")
# Una línea
# otra línea
# otra línea	una tabulación
c = "Esto es una cadena\ncon dos líneas"
c
# 'Esto es una cadena\ncon dos líneas'
print(c)
# Esto es una cadena
# con dos líneas
c = "Esto es una cadena\ncon dos líneas"
c + c
# 'Esto es una cadena\ncon dos líneasEsto es una cadena\ncon dos líneas'
c = "Esto es una cadena\ncon dos líneas"
print(c+c)
# Esto es una cadena
# con dos líneasEsto es una cadena
# con dos líneas
s = "Una cadena" " compuesta de dos cadenas"
print(s)
# Una cadena compuesta de dos cadenas
c1 = "Una cadena"
c2 = "otra cadena"
print("Una cadena " + c2)
# Una cadena otra cadena
# También es posible utilizar la multiplicación de cadenas
diez_espacios = " " * 10
print(diez_espacios + "un texto a diez espacios")
#          un texto a diez espacios
palabra = "Python"
palabra[0] # carácter en la posición 0
# 'P'
palabra[3]
# 'h'
palabra[-1]
# 'n'
palabra[-0]
# 'P'
palabra[-2]
# 'o'
palabra[-6]
# 'P'
palabra[5]
# 'n'
palabra = "Python"
print('palabra = "Python"')
palabra[0:2]
# 'Py'
palabra[2:]
# 'thon'
palabra[:2]
# 'Py'
palabra[:99]
# 'Python'
palabra[99:]
# ''
palabra = "N" + palabra[1:]
print('palabra = "N" + palabra[1:]')
palabra
print(palabra)
# 'Nython'
palabra = "Python"
print('palabra = "Python"')
len(palabra)
print(len(palabra))
# 6