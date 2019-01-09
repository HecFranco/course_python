clientes= [
    {'Nombre': 'Hector',  'Apellidos':'Costa Guzman',      'dni':'11111111A'},
    {'Nombre': 'Juan',    'Apellidos':'González Márquez',  'dni':'22222222B'} 
]
clientes
# [{'Apellidos': 'Costa Guzman', 'Nombre': 'Hector', 'dni': '11111111A'},
# {'Apellidos': 'González Márquez', 'Nombre': 'Juan', 'dni': '22222222B'}]
def mostrar_cliente(clientes, dni):
    for c in clientes:
        if (dni == c['dni']):
            print('{} {}'.format(c['Nombre'],c['Apellidos']))
            return
    print('Cliente no encontrado')
mostrar_cliente(clientes, '11111111A')
# Hector Costa Guzman
mostrar_cliente(clientes, '11111111Z')
# Cliente no encontrado
def borrar_cliente(clientes, dni):
    for i,c in enumerate(clientes):
        if (dni == c['dni']):
            del( clientes[i] )
            print(str(c),"> BORRADO")
            return
    print('Cliente no encontrado')
borrar_cliente(clientes, '22222222V')
# Cliente no encontrado
borrar_cliente(clientes, '22222222B')
# {'Apellidos': 'González Márquez', 'Nombre': 'Juan', 'dni': '22222222B'} > BORRADO
clientes
# [{'Apellidos': 'Costa Guzman', 'Nombre': 'Hector', 'dni': '11111111A'}]