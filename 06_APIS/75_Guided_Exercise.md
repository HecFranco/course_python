# Ejercicio Guiado

Para este ejemplo realizaremos una petición estándar a la url [http://pokeapi.co/api/v2/pokemon-form/](http://pokeapi.co/api/v2/pokemon-form/).

Al acceder a dicha url se nos mostrará algo como esto:

```json
{
  "count": 1068,
  "next": null,
  "previous": null,
  "results": [
    {
      "name": "bulbasaur",
      "url": "https://pokeapi.co/api/v2/pokemon-form/1/"
    },
    {
      "name": "ivysaur",
      "url": "https://pokeapi.co/api/v2/pokemon-form/2/"
    },
    {
      "name": "venusaur",
      "url": "https://pokeapi.co/api/v2/pokemon-form/3/"
    },
    {
      "name": "charmander",
      "url": "https://pokeapi.co/api/v2/pokemon-form/4/"
    },
    {
      "name": "charmeleon",
      "url": "https://pokeapi.co/api/v2/pokemon-form/5/"
    },
    {
      "name": "charizard",
      "url": "https://pokeapi.co/api/v2/pokemon-form/6/"
    },
    //...
}
```

Iniciaremos nuestro script con el siguiente código:

```python
import requests

if __name__ == '__main__':
  url = 'http://pokeapi.co/api/v2/pokemon-form/'
  response = requests.get(url)
```

Como en ejemplo anterior si obtenemos respuesta, `response.status_code == 200`, mostraremos los resultados convirtiéndolos a **json** mediante el método `.json()`, `payload = response.json()`. Este método devolverá un diccionario del cual extraeremos el argumento `result` en caso de existir, y en el caso de no existir devolveremos `[]`, `results = payload.get('results', [])`. Finalmente si el resultado contiene elementos, `if results:`, recorreremos el resultado, `for pokemon in results:`, mostrando unicamente el nombre de cada pockemon, `print(pokemon['name'])`.

```diff
import requests

if __name__ == '__main__':
    url = 'http://pokeapi.co/api/v2/pokemon-form/'
    response = requests.get(url) 
++  if response.status_code == 200:
++      payload = response.json()
++      results = payload.get('results', []) # si no obtenemos el parámetro 'results' dentro del resultado me devuelves []
++      if results:
++          for pokemon in results:
++              name = pokemon['name']
++              print(name)
```

[Volver al inicio](#-ejercicio-guiado)

## USANDO ARGUMENTOS EN LA API

---------------------------------------------------------------------------

Esta api permite gestionar la búsqueda para mostrar un resultado menor mediante el parámetro `offset`.

```diff
import requests

if __name__ == '__main__':
    url = 'http://pokeapi.co/api/v2/pokemon-form/'
++  args = {'offset': 0} if offset else {}
--  response = requests.get(url)
++  response = requests.get(url, params=args)
    if response.status_code == 200:
        payload = response.json()
        results = payload.get('results', []) # si no obtenemos el parámetro 'results' dentro del resultado me devuelves []
        if results:
            for pokemon in results:
                name = pokemon['name']
                print(name)
```

Con esta modificación recibiremos tan sólo los siguientes 20 resultados a partir del número indicado en el parámetro `offset`.

[Volver al inicio](#-ejercicio-guiado)

## REFACTORIZAR

---------------------------------------------------------------------------

En el siguiente paso refactorizaremos nuestro script incluyendo el código en una función llamada `get_pokemons()`.

```diff
import requests
++ def get_pokemons( url='http://pokeapi.co/api/v2/pokemon-form/' , offset=0 ):
++  args = {'offset': offset} if offset else {}
++  response = requests.get(url, params=args) 
++  if response.status_code == 200:
++      payload = response.json()
++      results = payload.get('results', []) # si no obtenemos el parámetro 'results' dentro del resultado me devuelves []
++      if results:
++          for pokemon in results:
++              name = pokemon['name']
++              print(name)

if __name__ == '__main__':
--  url = 'http://pokeapi.co/api/v2/pokemon-form/'
--  args = {'offset': 0} if offset else {}
--  response = requests.get(url, params=args)
--  if response.status_code == 200:
--      payload = response.json()
--      results = payload.get('results', []) # si no obtenemos el parámetro 'results' dentro del resultado me devuelves []
--      if results:
--          for pokemon in results:
--              name = pokemon['name']
--              print(name)
++    get_pokemons()
```

En el siguiente paso incluiremos al final del código la opción de seguir mostrando listado o no:

```diff
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://pockeapi.co
import requests

def get_pokemons( url='http://pokeapi.co/api/v2/pokemon-form/' , offset=0 ):
    args = {'offset': offset} if offset else {}
    response = requests.get(url, params=args) 
    if response.status_code == 200:
        payload = response.json()
        results = payload.get('results', []) # si no obtenemos el parámetro 'results' dentro del resultado me devuelves []
        if results:
            for pokemon in results:
                name = pokemon['name']
                print(name)

++  next = input("¿Continuar listando? [Y/N]").lower()
++  if next == 'y':
++    get_pokemons(offset=offset+20)

if __name__ == '__main__':
    get_pokemons()
```

[Volver al inicio](#-ejercicio-guiado)
