# Encabezados de las peticiones

Los encabezados y parámetros de REST contienen una gran cantidad de información que puede ayudarle a localizar problemas cuando los encuentre. Las cabeceras HTTP son una parte importante de la solicitud y respuesta de la API, ya que representan los metadatos asociados a la solicitud y respuesta de la API. Las cabeceras contienen información para:

* Cuerpo de Solicitudes y Respuestas
* Solicitar autorización
* Caché de respuestas 
* Cookies de respuesta

[Volver al inicio](#-encabezados-de-las-peticiones)

## HEADER API

---------------------------------------------------------------------------

Siguiendo desde el ejemplo anterior:

```python
import requests
import json

if __name__ == '__main__':
  url = 'http://httpbin.org/post'
  payload = { 'nombre':'Eduardo', 'curso': 'python', 'nivel':'intermedio'}
  response = requests.post(url, data=json.dumps(payload))
  print(response.url)
  if response.status_code == 200:
    print(response.content)
```

Realizaremos las modificaciones necesarias para incluir el encabezado de la petición:

```diff
import requests
import json

if __name__ == '__main__':
    url = 'http://httpbin.org/post'
    payload = { 'nombre':'Eduardo', 'curso': 'python', 'nivel':'intermedio'}
++  headers = { 'Content-Type': 'application/json'}
--  response = requests.post(url, data=json.dumps(payload))
++  response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(response.url)
    if response.status_code == 200:
        print(response.content)
```

En este caso hemos definido una variable que contenga un diccionario la cual incluiremos dentro de la petición **post** como un tercer parámetro asociado a la variable interna del método `headers`, `response = requests.post(url, data=json.dumps(payload), headers=headers)`.

Además de dicho encabezado ya utilizado que designa el tipo de contenido, `'Content-Type': 'application/json'`, podemos incluir más configuración dentro de la petición, como sería el caso de **Access-token**, `'Access-token': '12345678'`.

```diff
import requests
import json

if __name__ == '__main__':
    url = 'http://httpbin.org/post'
    payload = { 'nombre':'Eduardo', 'curso': 'python', 'nivel':'intermedio'}
--  headers = { 'Content-Type': 'application/json'}
++  headers = { 'Content-Type': 'application/json', 'Access-token': '12345678' }
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(response.url)
    if response.status_code == 200:
        print(response.content)
```

Si realizasemos ahora la petición veríamos lo siguiente:

```bash
$ python d:/00.ProyectosWeb/python-by-sample/05_APIS/Examples/main_11_HEADER.py
b'{\n  "args": {}, \n  "data": "{\\"nombre\\": \\"Eduardo\\", \\"curso\\": \\"python\\", \\"nivel\\": \\"intermedio\\"}", \n  "files": {}, \n  "form": {}, \n  "headers": {\n    "Accept": "*/*", \n
   "Accept-Encoding": "gzip, deflate", \n    "Access-Token": "12345678", \n    "Connection": "close", \n    "Content-Length": "63", \n    "Content-Type": "application/json", \n    "Host": "httpbin.org", \n    "User-Agent": "python-requests/2.20.1"\n  }, \n  "json": {\n    "curso": "python", \n    "nivel": "intermedio", \n    "nombre": "Eduardo"\n  }, \n  "origin": "87.220.127.88", \n  "url": "http://httpbin.org/post"\n}\n'
```

[Volver al inicio](#-encabezados-de-las-peticiones)

### LEER HEADERS EN UNA RESPONSE

---------------------------------------------------------------------------

Al igual que podemos enviar distintos encabezados, puede ser necesario leer los encabezados enviados por el servidor como respuesta, para ello utilizaremos el siguiente código:

```diff
import requests
import json

if __name__ == '__main__':
    url = 'http://httpbin.org/post'
    payload = { 'nombre':'Eduardo', 'curso': 'python', 'nivel':'intermedio'}
    headers = { 'Content-Type': 'application/json', 'Access-token': '12345678' }
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(response.url)
    if response.status_code == 200:
--      print(response.content)
++      print(response.headers)
```

> **NOTA**: En este caso, nuevamente **`.headers`** es un diccionario, por lo que para acceder a un determinado atributo dentro del diccionario utilizaremos el siguiente código.

```diff
import requests
import json

if __name__ == '__main__':
    url = 'http://httpbin.org/post'
    payload = { 'nombre':'Eduardo', 'curso': 'python', 'nivel':'intermedio'}
    headers = { 'Content-Type': 'application/json', 'Access-token': '12345678' }
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(response.url)
    if response.status_code == 200:
++      headers_response = response.headers
++      server = headers_response['Server']
--      print(response.headers)
++      print(server)
```

Finalmente si ejecutasemos el script recibiríamos la siguiente respuesta:

```bash
$ python d:/00.ProyectosWeb/python-by-sample/05_APIS/Examples/main_12_HEADER.py
gunicorn/19.9.0
```