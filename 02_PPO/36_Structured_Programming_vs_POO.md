# Programación Estructurada VS POO

No hace falta entender el código, lo aprenderemos en esta unidad.

[Volver al inicio](#-programación-estructurada-vs-poo)

## EJEMPLO DE IMPLEMENTACIÓN CON PROGRAMACIÓN ESTRUCTURADA

---------------------------------------------------------------------------

```python
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
```

[Volver al inicio](#-programación-estructurada-vs-poo)

## EJEMPLO DE IMPLEMENTACIÓN CON PROGRAMACIÓN ORIENTADA A OBJETOS

---------------------------------------------------------------------------

```python
class Cliente:
    def __init__(self, dni, nombre, apellidos):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
    def __str__(self):
        return '{} {}'.format(self.nombre,self.apellidos)
​
class Empresa:
    def __init__(self, clientes=[]):
        self.clientes = clientes
    def mostrar_cliente(self, dni=None):
        for c in self.clientes:
            if c.dni == dni:
                print(c)
                return
        print("Cliente no encontrado")
    def borrar_cliente(self, dni=None):
        for i,c in enumerate(self.clientes):
            if c.dni == dni:
                del(self.clientes[i])
                print(str(c),"> BORRADO")
                return
        print("Cliente no encontrado")
hector = Cliente(dni="11111111A", nombre="Hector", apellidos="Costa Guzman")
hector
# <__main__.Cliente at 0x4b97150>
juan = Cliente("22222222B", "Juan", "Gonzalez Marquez")
empresa = Empresa(clientes=[hector, juan])
empresa.clientes
# [<__main__.Cliente at 0x4b97150>, <__main__.Cliente at 0x4b97890>]
empresa.mostrar_cliente("11111111A")
# Hector Costa Guzman
empresa.borrar_cliente("22222222B")
# Juan Gonzalez Marquez > BORRADO
empresa.clientes
# [<__main__.Cliente at 0x4b97150>]
```

[Volver al inicio](#-programación-estructurada-vs-poo)