# Consumir Apis

[Volver al inicio](#-consumir-apis)

## ¿QUÉ ES HTTP?

---------------------------------------------------------------------------

El protocolo de transferencia de hipertexto (HTTP) está diseñado para permitir las comunicaciones entre clientes y servidores. Así, **HTTP** funciona como un protocolo de solicitud-respuesta entre un cliente y un servidor.

Un navegador web puede ser el cliente, y una aplicación en una computadora que aloja un sitio web puede ser el servidor.

> **EJEMPLO**: Un cliente (navegador) envía una petición HTTP al servidor; a continuación, el servidor devuelve una respuesta al cliente. La respuesta contiene información sobre el estado de la solicitud y también puede contener el contenido solicitado.

**Métodos HTTP**

* **GET**
* **POST**
* **PUT**
* **HEADER**
* **DELETE**
* **DELETE**
* **PATCH**
* **OPTIONS**

Por ello, **Python** dispone de dos librerías fundamentales para consumir APIS, **requests** y **urllib2**.

> **NOTA**: La documentación oficial sobre la librería **requests** se encuentra en [http://docs.python-requests.org/en/master](http://docs.python-requests.org/en/master).

En estos ejemplos veremos como utilizar **requests** ya que es la mas utilizada.

Para esta parte ejecutaremos un ejemplo progresivo que nos permitirá evolucionarlo e ir viendo distintas partes del consumo de APIS.

Utilizaremos la librería [httpbin.org](httpbin.org) la cual nos permitirá de una manera rápida probar las distintas opciones de consumo de APIS.

> **NOTA**: Todas las demos siguientes deberán ser ejecutadas como **scripts**, es decir mediante consola usando el comando que llame al archivo `python <python-file>`.

[Volver al inicio](#-consumir-apis)

## MÉTODO GET

---------------------------------------------------------------------------

El método **GET** se utiliza para solicitar datos de un recurso especificado.

> **NOTA**: **GET** es uno de los métodos HTTP más comunes.

Tenga en cuenta que la cadena de consulta (pares **nombre/valor**) se envía en la URL de una petición GET: [/test/demo_form.php?name1=value1&name2=value2](/test/demo_form.php?name1=value1&name2=value2).

Algunas otras notas sobre las peticiones GET:

* Las peticiones **GET** pueden ser almacenadas en caché
* Las peticiones **GET** permanecen en el historial del navegador
* Las peticiones **GET** pueden marcarse como favoritas
* Las peticiones **GET** nunca deben ser utilizadas cuando se trata de datos sensibles
* Las solicitudes **GET** tienen restricciones de longitud
* Las peticiones **GET** sólo se utilizan para solicitar datos (no para modificarlos).

[Volver al inicio](#-consumir-apis)

### PRIMERA DEMO GET

---------------------------------------------------------------------------

En esta primera demo realizaremos una petición a la url [http://google.com](http://google.com).

```python
import requests

if __name__ == '__main__':
    url = 'https://www.google.com/'
    response = request.get(url)

    print(response)
```

> **NOTA**: Mediante esta simple petición podremos ver el resultado de una petición básica. Si la respuesta es `<Response [200]>` significará que la consulta ha sido satisfactoria.

> **NOTA**: **¿Por qué `__name__ == '__main__'`?**, Esto está ligado al modo de funcionamiento del intérprete Python, cuando el intérprete lee un archivo de código, ejecuta todo el código que se encuentra en él. Todo módulo (archivo de código) en python tiene un atributo especial llamado `__name__` que define el espacio de nombres en el que se está ejecutando. Es usado para identificar de forma única un módulo en el sistema de importaciones.<br>Por su parte `__main__` es el nombre del ámbito en el que se ejecuta el código de nivel superior (tu programa principal).<br>El intérprete pasa el valor del atributo a `'__main__'` si el módulo se está ejecutando como programa principal (cuando lo ejecutas llamando al intérptrete en la terminal con python my_modulo.py, haciendo doble click en él, ejecutandolo en el intérprete interactivo, etc ).<br>Si el módulo no es llamado como programa principal, sino que es importado desde otro módulo, el atributo `__name__` pasa a contener el nombre del archivo en si. <br>[Aquí](https://docs.python.org/3/library/__main__.html) tienes la documentación oficial.

Ahora ampliaremos la demo incluyendo un condicional interno en el cual imprimiremos el atributo `content` de la respuesta siempre que `status_code` sea igual a `200`.

```diff
import requests

if __name__ == '__main__':
    url = 'https://www.google.com/'
    response = request.get(url)
--  print(response)
++  if response.status_code == 200:
++      print(response.content)
```

Ahora si quisieramos almacenar el contenido de la respuesta en un archivo realizaríamos la siguiente modificación. Simplemente crearemos una variable con el contenido `response.content` el cual se grabará dentro del archivo creado `google.html` con permisos de escritura y lectura, `rw`.

```diff
import requests

if __name__ == '__main__':
    url = 'https://www.google.com/'
    response = request.get(url)
    if response.status_code == 200:
--      print(response.content)
++      content = response.content
++      file = open('google.html', 'rw')
++      file.write(content)
++      file.close()
```

[Volver al inicio](#-consumir-apis)

### DEMO GET USANDO [HTTPBIN.ORG](http://httpbin.org)

---------------------------------------------------------------------------

Para esta demo usaremos el método **GET** en la url [http://httpbin.org/get](http://httpbin.org/get), si accediesemos directamente a esa url podríamos ver algo así:

```json
{
  "args": {}, 
  "headers": {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", 
    "Accept-Encoding": "gzip, deflate", 
    "Accept-Language": "es-ES,es;q=0.9,en;q=0.8", 
    "Connection": "close", 
    "Cookie": "_gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1; _gauges_unique_hour=1; _gauges_unique_day=1", 
    "Host": "httpbin.org", 
    "Upgrade-Insecure-Requests": "1", 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"
  }, 
  "origin": "87.220.127.88", 
  "url": "http://httpbin.org/get"
}
```

Comenzaremos con nuestro siguiente script de **Python**:

```python
import requests

if __name__ == '__main__':
    url = 'http://httpbin.org/get'
    response = request.get(url)
    if response.status_code == 200:
      content = response.content
      print(content)
```

Al ejecutarlo obtendremos la siguiente respuesta en formato **json**.

```bash
$ python main_02.py
b'{\n  "args": {}, \n  "headers": {\n    "Accept": "*/*", \n    "Accept-Encoding": "gzip, deflate", \n    "Connection": "close", \n    "Host": "httpbin.org", \n    "User-Agent": "python-requests/2.20.1"\n  }, \n  "origin": "87.220.127.88", \n
"url": "http://httpbin.org/get"\n}\n'
```

> **NOTA**: Recibiremos un menor número de atributos enviados con respecto a lo visualizado en la web, aunque si mantiene los atributos primarios: **args**, **headers** y **origin**.

[Volver al inicio](#-consumir-apis)

#### ENVIAR PARÁMETROS

---------------------------------------------------------------------------

Para poder entender el método de envío de parámetros en una api, primeramente realizaremos en envío mediante la url [http://httpbin.org/get?nombre=ricardo&curso=python](http://httpbin.org/get?nombre=ricardo&curso=python), tras lo cual veremos la siguiente respuesta:

```json
{
  "args": {
    "curso": "python", 
    "nombre": "ricardo"
  }, 
  "headers": {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", 
    "Accept-Encoding": "gzip, deflate", 
    "Accept-Language": "es-ES,es;q=0.9,en;q=0.8", 
    "Connection": "close", 
    "Cookie": "_gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1; _gauges_unique_hour=1; _gauges_unique_day=1", 
    "Host": "httpbin.org", 
    "Upgrade-Insecure-Requests": "1", 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"
  }, 
  "origin": "87.220.127.88", 
  "url": "http://httpbin.org/get?nombre=ricardo&curso=python"
}
```

> **NOTA**: Observaremos que los parámetros enviados aparecen dentro del primer atributo **args**.

Para enviar los parámetros de una forma correcta utilizaremos un **diccionario**, `args = { 'nombre':'Eduardo', 'curso': 'python', 'nivel':'intermedio'}`.

```diff
import requests

if __name__ == '__main__':
    url = 'http://httpbin.org/get'
++  args = { 'nombre':'Eduardo', 'curso': 'python', 'nivel':'intermedio'}  
--  response = request.get(url)
++  response = request.get(url, params=args)
    if response.status_code == 200:
      content = response.content
      print(content)
```

Al ejecutarlo obtendremos la siguiente respuesta en formato **json**.

```bash
$ python main_04.py
http://httpbin.org/get?nombre=Eduardo&curso=python&nivel=intermedio
b'{\n  "args": {\n    "curso": "python", \n    "nivel": "intermedio", \n    "nombre": "Eduardo"\n  }, \n  "headers": {\n    "Accept": "*/*", \n    "Accept-Encoding": "gzip, deflate", \n    "Connection": "close", \n    "Host": "httpbin.org", \n
   "User-Agent": "python-requests/2.20.1"\n  }, \n  "origin": "87.220.127.88", \n  "url": "http://httpbin.org/get?nombre=Eduardo&curso=python&nivel=intermedio"\n}\n'
```

> **NOTA**: Podremos observar que aunque utilizamos el atributo **params** del método **get**, siendo más legible el código, este compone la url para incluir los parámetros definidos.

[Volver al inicio](#-consumir-apis)

#### CONVERTIR RESPUESTA

---------------------------------------------------------------------------

Como hemos podido observar la respuesta obtenida es un objeto **json** el cual puede ser convertido a un **diccionario** de **Python** para gestionar y poder consultar cada atributo de una manera más cómoda.

```diff
import requests

if __name__ == '__main__':
    url = 'http://httpbin.org/get'
    args = { 'nombre':'Eduardo', 'curso': 'python', 'nivel':'intermedio'}  
    response = request.get(url, params=args)
    if response.status_code == 200:
--    content = response.content
--    print(content)
++    response_json = response.json()
++    origin = response_json['origin']
++    print(origin)
```

Al ejecutarlo obtendremos la siguiente respuesta en formato **json**.

```bash
$ python main_05.py
87.220.127.88
```

Además tenemos otra opción alternativa que consiste en usar la librería **json**

```diff
import requests
++ import json
if __name__ == '__main__':
    url = 'http://httpbin.org/get'
    args = { 'nombre':'Eduardo', 'curso': 'python', 'nivel':'intermedio'}  
    response = request.get(url, params=args)
    if response.status_code == 200:
--    response_json = response.json()
++    # response_json = response.json()
++    response_json = json.loads(response.text)
      origin = response_json['origin']
      print(origin)
```

En lo cual al ejecutarlo obtendremos la siguiente respuesta en formato **json**.

```bash
$ python main_06.py
87.220.127.88
```

[Volver al inicio](#-consumir-apis)

## MÉTODO POST

---------------------------------------------------------------------------

El método **POST** se utiliza para enviar datos a un servidor para **crear/actualizar** un recurso. Los datos enviados al servidor con **POST** se almacenan en el **cuerpo de la petición HTTP**:

```bash
POST /test/demo_form.php HTTP/1.1
Anfitrión: demo.com
nombre1=valor1&nombre2=valor2
```

> **NOTA**: **POST** es uno de los métodos HTTP más comunes.

Algunas otras notas sobre las peticiones **POST**:

* Las peticiones **POST** nunca se almacenan en caché
* Las peticiones **POST** no permanecen en el historial del navegador
* Las solicitudes **POST** no pueden marcarse como favoritas
* Las solicitudes **POST** no tienen restricciones en cuanto a la longitud de los datos.

[Volver al inicio](#-consumir-apis)

### DEMO POST USANDO [HTTPBIN.ORG](http://httpbin.org)

---------------------------------------------------------------------------

Comenzaremos con nuestro siguiente script de **Python**:

```python
import requests

if __name__ == '__main__':
    url = 'http://httpbin.org/post'
    args = { 'nombre':'Eduardo', 'curso': 'python', 'nivel':'intermedio'}  
    response = request.post(url, params=args)
    if response.status_code == 200:
      content = response.content
      print(content)
```

> **NOTA**: Veremos que hemos modificado la url al ser necesaria que la url admita el método **POST**, y el método de **request** a **post**, `response = request.post(url, params=args)`.
En lo cual al ejecutarlo obtendremos la siguiente respuesta en formato **json**.

```bash
$ python main_07.py
b'{\n  "args": {}, \n  "data": "{\\"nombre\\": \\"Eduardo\\", \\"curso\\": \\"python\\", \\"nivel\\": \\"intermedio\\"}", \n  "files": {}, \n  "form": {}, \n  "headers": {\n    "Accept": "*/*", \n    "Accept-Encoding": "gzip, deflate", \n    "Connection": "close", \n    "Content-Length": "63", \n    "Content-Type": "application/json", \n    "Host": "httpbin.org", \n    "User-Agent": "python-requests/2.20.1"\n  }, \n  "json": {\n    "curso": "python", \n    "nivel": "intermedio", \n
  "nombre": "Eduardo"\n  }, \n  "origin": "87.220.127.88", \n  "url": "http://httpbin.org/post"\n}\n'
```

Podemos observar que los parámetros al igual que con **GET** se envían dentro del atributo **args**. Con **POST** es necesario en cambio enviarlo dentro del atributo **data**, para ello:

```diff
import requests

if __name__ == '__main__':
    url = 'http://httpbin.org/post'
--  args = { 'nombre':'Eduardo', 'curso': 'python', 'nivel':'intermedio'}  
++  payload = { 'nombre':'Eduardo', 'curso': 'python', 'nivel':'intermedio'}
--  response = request.post(url, params=args)
++  response = request.post(url, json=payload)
    if response.status_code == 200:
      content = response.content
      print(content)
```

> **NOTA**: Ahora los atributos podrán observarse dentro del atributo **data**, además de en **json** de una forma más legible.

```bash
$ python main_07_POST_JSON.py
b'{\n  "args": {}, \n  "data": "{\\"nombre\\": \\"Eduardo\\", \\"curso\\": \\"python\\", \\"nivel\\": \\"intermedio\\"}", \n  "files": {}, \n  "form": {}, \n  "headers": {\n    "Accept": "*/*", \n
   "Accept-Encoding": "gzip, deflate", \n    "Connection": "close", \n    "Content-Length": "63", \n    "Content-Type": "application/json", \n    "Host": "httpbin.org", \n    "User-Agent": "python-requests/2.20.1"\n  }, \n  "json": {\n    "curso": "python", \n    "nivel": "intermedio", \n    "nombre": "Eduardo"\n  }, \n  "origin": "87.220.127.88", \n  "url": "http://httpbin.org/post"\n}\n'
```

Internamente el método **post** coge el diccionario aportado dentro de **json** y lo serializa para convertirlo en dicho formato.

Opcionalmente podríamos incluir los parámetros enviados a la petición dentro de data: `response = request.post(url, data=payload)`, obteniendo como resultado que dichos parámetros se envíen dentro del argumento **forms**

```diff
import requests

if __name__ == '__main__':
    url = 'http://httpbin.org/post'
    payload = { 'nombre':'Eduardo', 'curso': 'python', 'nivel':'intermedio'}
--  response = request.post(url, json=args)
++  response = request.post(url, data=payload)
    if response.status_code == 200:
      content = response.content
      print(content)
```

```bash
$ python main_08_POST_DATA.py
b'{\n  "args": {}, \n  "data": "", \n  "files": {}, \n  "form": {\n    "curso": "python", \n    "nivel": "intermedio", \n    "nombre": "Eduardo"\n  }, \n  "headers": {\n    "Accept": "*/*", \n    "Accept-Encoding": "gzip, deflate", \n    "Connection": "close", \n    "Content-Length": "44", \n    "Content-Type": "application/x-www-form-urlencoded", \n    "Host": "httpbin.org", \n    "User-Agent": "python-requests/2.20.1"\n  }, \n  "json": null, \n  "origin": "87.220.127.88", \n  "url": "http://httpbin.org/post"\n}\n'
```

Si quisiesemos evitar eso simplemente tendríamos que serializar los datos enviados de la siguiente manera:

```diff
import requests
++ import json
if __name__ == '__main__':
    url = 'http://httpbin.org/post'
    payload = { 'nombre':'Eduardo', 'curso': 'python', 'nivel':'intermedio'}
--  response = request.post(url, data=payload)
++  response = request.post(url, data=json.dump(payload))
    if response.status_code == 200:
      content = response.content
      print(content)
```

Ahora al volver a ejecutar el script de python tendremos los parámetros enviados dentro del atributo **data**:

```bash
$ python main_09_POST_DATA_SERIALIZED.py
b'{\n  "args": {}, \n  "data": "{\\"nombre\\": \\"Eduardo\\", \\"curso\\": \\"python\\", \\"nivel\\": \\"intermedio\\"}", \n  "files": {}, \n  "form": {}, \n  "headers": {\n    "Accept": "*/*", \n
   "Accept-Encoding": "gzip, deflate", \n    "Connection": "close", \n    "Content-Length": "63", \n    "Host": "httpbin.org", \n    "User-Agent": "python-requests/2.20.1"\n  }, \n  "json": {\n
"curso": "python", \n    "nivel": "intermedio", \n    "nombre": "Eduardo"\n  }, \n  "origin": "87.220.127.88", \n  "url": "http://httpbin.org/post"\n}\n'
```

**Resumiendo**

* si utilizamos el argumento **json** post se encarga de serializar los parámetros enviados
* si utilizamos el argumento **data** es necesario serializar previamente los datos enviados

[Volver al inicio](#-consumir-apis)