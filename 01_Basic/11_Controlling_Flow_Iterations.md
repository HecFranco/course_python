# Controlando el Flujo - Iteraciones

Iterar significa realizar una acción varias veces. Cada vez que se repite se denomina iteración.

[Volver al inicio](#-controlando-el-flujo---iteraciones)

## SENTENDIA WHILE

---------------------------------------------------------------------------

La sentencia `While`, (Mientras), se basa en repetir un bloque a partir de evaluar una condición lógica, siempre que ésta sea `True`.

Queda en las manos del programador decidir el momento en que la condición cambie a `False` para hacer que el While finalice.

```python
c = 0
while c <= 5:
    c+=1
    print("c vale",c)
# c vale 1
# c vale 2
# c vale 3
# c vale 4
# c vale 5
# c vale 6
```

[Volver al inicio](#-controlando-el-flujo---iteraciones)

## SENTENDIA ELSE EN BUCLE WHILE

---------------------------------------------------------------------------

La sentencia `Else` en bucle `While`, se encadena al `While` para ejecutar un bloque de código una vez la condición ya no devuelve `True` (normalmente al final).

```python
c = 0
while c <= 5:
    c+=1
    print("c vale",c)
else:
    print("Se ha completado toda la iteración y c vale",c)
# c vale 1
# c vale 2
# c vale 3
# c vale 4
# c vale 5
# c vale 6
# Se ha completado toda la iteración y c vale 6
```

[Volver al inicio](#-controlando-el-flujo---iteraciones)

## INSTRUCCIÓN BREAK

---------------------------------------------------------------------------

La instrucción `break`, sirve para "romper" la ejecución del While en cualquier momento. No se ejecutará el `Else`, ya que éste sólo se llama al finalizar la iteración.

> **NOTA**: `break` pertenece al listado de palabras reservadas del lenguaje **Python**

```python
c = 0
while c <= 5:
    c+=1
    if (c==4):
        print("Rompemos el bucle cuando c vale " + str(c))
        break
    print("c vale",c)
else:
    print("Se ha completado toda la iteración y c vale " + str(c))
# c vale 1
# c vale 2
# c vale 3
# Rompemos el bucle cuando c vale 4
```

[Volver al inicio](#-controlando-el-flujo---iteraciones)

## INSTRUCCIÓN CONTINUE

---------------------------------------------------------------------------

La istrucción `continue`, sirve para "saltarse" la iteración actual sin romper el bucle.

> **NOTA**: `continue` pertenece al listado de palabras reservadas del lenguaje **Python**

```python
c = 0
while c <= 5:
    c+=1
    if c==3 or c==4:
        # print("Continuamos con la siguiente iteración",c)
        continue
    print("c vale",c)
else:
    print("Se ha completado toda la iteración y c vale",c)
# c vale 1
# c vale 2
# c vale 5
# c vale 6
# Se ha completado toda la iteración y c vale 6
```

[Volver al inicio](#-controlando-el-flujo---iteraciones)