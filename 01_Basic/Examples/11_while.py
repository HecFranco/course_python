# Creando un menú interactivo
print("Bienvenido al menú interactivo")
while(True):
    print("""¿Qué quieres hacer? Escribe una opción
    1) Saludar
    2) Sumar dos números
    3) Salir""")
    opcion = input()
    if opcion == '1':
        print("Hola, espero que te lo estés pasando bien")
    elif opcion == '2':
        n1 = float(input("Introduce el primer número: "))
        n2 = float(input("Introduce el segundo número: "))
        print("El resultado de la suma es: ",n1+n2)
    elif opcion =='3':
        print("¡Hasta luego! Ha sido un placer ayudarte")
        break
    else:
        print("Comando desconocido, vuelve a intentarlo")
# Bienvenido al menú interactivo
# ¿Qué quieres hacer? Escribe una opción
#     1) Saludar
#     2) Sumar dos números
#     3) Salir
# 1
# Hola, espero que te lo estés pasando bien
# ¿Qué quieres hacer? Escribe una opción
#     1) Saludar
#     2) Sumar dos números
#     3) Salir
# 2
# Introduce el primer número: 10
# Introduce el segundo número: 5
# El resultado de la suma es:  15.0
# ¿Qué quieres hacer? Escribe una opción
#     1) Saludar
#     2) Sumar dos números
#     3) Salir
# kdjsk
# Comando desconocido, vuelve a intentarlo
# ¿Qué quieres hacer? Escribe una opción
#     1) Saludar
#     2) Sumar dos números
#     3) Salir
# 3
# ¡Hasta luego! Ha sido un placer ayudarte