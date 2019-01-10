# Métodos PUT y DELETE

[Volver al inicio](#-métodos-put-y-delete)

## MÉTODO PUT

---------------------------------------------------------------------------

El método **PUT** se utiliza para enviar datos a un servidor para **crear/actualizar** un recurso.

La diferencia entre **POST** y PUT es que las peticiones **PUT** son idempotentes. Es decir, llamar a la misma petición **PUT** varias veces siempre producirá el mismo resultado. Por el contrario, llamar a una petición POST repetidamente tiene efectos secundarios de crear el mismo recurso varias veces.

Para probar este método rescataremos el útlimo script utilizado:

```python
import requests
import json

if __name__ == '__main__':
  url = 'http://httpbin.org/post'
  payload = { 'nombre':'Eduardo', 'curso': 'python', 'nivel':'intermedio'}
  headers = { 'Content-Type': 'application/json', 'Access-token': '12345678' }
  response = requests.post(url, data=json.dumps(payload), headers=headers)
  print(response.url)
  if response.status_code == 200:
    headers_response = response.headers
    server = headers_response['Server']
    print(server)
```

En el cual cambiaremos, como es de esperar, tanto la url de petición como el método usado con **requests**.

```diff
import requests
import json

if __name__ == '__main__':
--  url = 'http://httpbin.org/post'
++  url = 'http://httpbin.org/put'
    payload = { 'nombre':'Eduardo', 'curso': 'python', 'nivel':'intermedio'}
    headers = { 'Content-Type': 'application/json', 'Access-token': '12345678' }
--  response = requests.post(url, data=json.dumps(payload), headers=headers)
++  response = requests.put(url, data=json.dumps(payload), headers=headers)
    print(response.url)
    if response.status_code == 200:
        headers_response = response.headers
        server = headers_response['Server']
        print(server)
```

Al ejecutarlo obtendremos la siguiente respuesta en formato **json**.

```bash
$ python d:/00.ProyectosWeb/python-by-sample/05_APIS/Examples/main_13_PUT.py
gunicorn/19.9.0
```

Al recibir el **server** empleado sabremos que nuestra petición se está realizando correctamente.

[Volver al inicio](#-métodos-put-y-delete)

## MÉTODO DELETE

---------------------------------------------------------------------------

El método **DELETE** borra el recurso especificado.

Volveremos a cambiar, como es de esperar, tanto la url de petición como el método usado con **requests**.

```diff
import requests
import json

if __name__ == '__main__':
--  url = 'http://httpbin.org/put'
++  url = 'http://httpbin.org/delete'
    payload = { 'nombre':'Eduardo', 'curso': 'python', 'nivel':'intermedio'}
    headers = { 'Content-Type': 'application/json', 'Access-token': '12345678' }
--  response = requests.put(url, data=json.dumps(payload), headers=headers)
++  response = requests.delete(url, data=json.dumps(payload), headers=headers)
    print(response.url)
    if response.status_code == 200:
        headers_response = response.headers
        server = headers_response['Server']
        print(server)
```

Al ejecutarlo obtendremos la siguiente respuesta en formato **json**.

```bash
$ python d:/00.ProyectosWeb/python-by-sample/05_APIS/Examples/main_13_PUT.py
gunicorn/19.9.0
```

Al recibir el **server** empleado sabremos que nuestra petición se está realizando correctamente.

[Volver al inicio](#-métodos-put-y-delete)