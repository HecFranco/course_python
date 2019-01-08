# Entradas por teclado

Ya conocemos la función `input()` que lee una cadena por teclado. Su único inconveniente es que debemos transformar el valor a numérico si deseamos hacer operaciones con él:

```python
decimal = float( input("Introduce un número decimal con punto: ") )
# Introduce un número decimal con punto: 3.14
valores = []
print("Introduce 3 valores")
for x in range(3):
    valores.append( input("Introduce un valor >") )
# Introduce 3 valores
# Introduce un valor >10
# Introduce un valor >sdkjsdk
# Introduce un valor >skdjs
valores
# ['10', 'sdkjsdk', 'skdjs']
```

[Volver al inicio](#-entradas-por-teclado)