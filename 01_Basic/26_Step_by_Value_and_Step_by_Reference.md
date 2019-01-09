# Paso por valor y paso por referencia

* **Paso por valor**: Se crea una copia local de la variable dentro de la función.
* **Paso por referencia**: Se maneja directamente la variable, los cambios realizados dentro le afectarán también fuera.

Tradicionalmente, los tipos simples se pasan automáticamente por valor y los compuestos por referencia.

* **Simples**: Enteros, flotantes, cadenas, lógicos...
* **Compuestos**: Listas, diccionarios, conjuntos...

[Volver al inicio](#-paso-por-valor-y-paso-por-referencia)

## PASO POR VALOR

---------------------------------------------------------------------------

```python
def doblar_valor(numero):
    numero*=2
n = 10
doblar_valor(n)
n
# 10
```

[Volver al inicio](#-paso-por-valor-y-paso-por-referencia)

## PASO POR REFERENCIA

---------------------------------------------------------------------------

```python
def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2
ns = [10,50,100]
doblar_valores(ns)
ns
# [20, 100, 200]
```

[Volver al inicio](#-paso-por-valor-y-paso-por-referencia)

## TRUCOS

---------------------------------------------------------------------------

Para modificar los tipos simples podemos devolverlos modificados y reasignarlos:

```python
def doblar_valor(numero):
    return numero*2
n = 10
n = doblar_valor(n)
n
# 20
```

Y en el caso de los tipos compuestos, podemos evitar la modificación enviando una copia:

```python
def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2
ns = [10,50,100]
doblar_valores(ns[:])  # Una copia al vuelo de una lista con [:]
ns
# [10, 50, 100]
```

[Volver al inicio](#-paso-por-valor-y-paso-por-referencia)