# OAuth

[Volver al inicio](#-oauth)

## VENTAJAS DEL SISTEMA OAUTH

---------------------------------------------------------------------------

* Ahorrar tiempo en el registro
* Estarás seguro de que tu password no se va a almacenar dentro del sitio web o la aplicación debido a que estás utilizando un servicio de un tercero

[Volver al inicio](#-oauth)

## REGISTRO APLICACIÓN

---------------------------------------------------------------------------

En los siguientes puntos veremos como utilizar la api de **GitHub**, no nos vamos a enfocar en explicar todos los **endpints**.

Accederemos a esta url [https://github.com/settings/applications/new](https://github.com/settings/applications/new) dónde podremos darnos de alta como usuarios de la api.

![sources/01.jpg](sources/01.jpg)

Este formulario nos permitirá generar nuestra primera aplicación **OAuth** en los servidores de **GitHub**.

Será necesario incluir:

* Nombre de Aplicación
* Url de la aplicación.
* Descripción de la aplicación.
* Url de acceso a la aplicación una vez authentificado.

> **NOTA**: **Open Authorization (OAuth)** es un estándar abierto que permite flujos simples de autorización para sitios web o aplicaciones informáticas. Se trata de un protocolo propuesto por Blaine Cook y Chris Messina, que permite autorización segura de una API de modo estándar y simple para aplicaciones de escritorio, móviles y web. **Este tipo de conexiones son típicas en muchas conexiones con API.**

**¿Cuando estamos usando este tipo de conexión?** Por ejemplo cuando nos registramos en una web y lo hacemos por medio de nuestras redes sociales, lo hacemos mediante **OAuth**.

![sources/02.jpg](sources/02.jpg)

Ahora se nos generarían dos nuevos valores alfanuméricos un **CLIENT ID** y un **CLIENT SECRET** (habrá que guardar estos datos de acceso en lugares seguros, nunca en el propio código)

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://developer.github.com/v3/oauth/

import requests

client_id = '369215fa00432fd6b039'
client_secret = 'rgknw34kln23l45kn234l5kn32l4k5n23lk45n23lk4522345'
# https://github.com/login/oauth/authorize
if __name__ == '__main__':
  pass
```

Para loguearnos nuestra **endpoint** será el siguiente [https://github.com/login/oauth/authorize](https://github.com/login/oauth/authorize), el cual hemos conocido dentro de la documentación oficial de la **API** [https://developer.github.com/apps/building-oauth-apps/authorizing-oauth-apps/](https://developer.github.com/apps/building-oauth-apps/authorizing-oauth-apps/)

Accederemos (según la documentación oficial) a esta url [https://github.com/login/oauth/authorize?client_id=369215fa00432fd6b039&scope=respo](https://github.com/login/oauth/authorize?client_id=369215fa00432fd6b039&scope=respo). Esta url incluye dos parámetros **Get** `cliend_id`y `scope`.

![sources/03.jpg](sources/03.jpg)

Dentro de esa url encontraremos un formulario, en el cual al loguearnos se nos redirigirá a nuestra ubicación callback definida incluyendo una variable en la url `code` la cual desiganará nuestro **access token**, por ejemplo [https://urlcallback.com/?code=213412341234](https://urlcallback.com/?code=213412341234).

> **NOTA**: Un token de acceso es un objeto que encapsula la identidad de seguridad de un proceso o hilo. Un token se utiliza para tomar decisiones de seguridad y para almacenar información a prueba de manipulaciones sobre alguna entidad del sistema. Aunque un token se utiliza generalmente para representar sólo información de seguridad, es capaz de contener datos adicionales de formato libre que pueden adjuntarse mientras se crea el token. Los tokens pueden duplicarse sin privilegios especiales, por ejemplo, para crear un nuevo token con niveles más bajos de derechos de acceso para restringir el acceso de una aplicación lanzada. Windows utiliza un token de acceso cuando un proceso o hilo intenta interactuar con objetos que tienen descriptores de seguridad (objetos securizables). Un token de acceso está representado por el objeto de sistema del tipo Token.

Ese codigo `access token` dentro de la url callback podríamos guardarla dentro de nuestro código:

```diff
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://developer.github.com/v3/oauth/

import requests

client_id = '369215fa00432fd6b039'
client_secret = 'rgknw34kln23l45kn234l5kn32l4k5n23lk45n23lk4522345'
++ code = '213412341234'
# https://github.com/login/oauth/authorize
if __name__ == '__main__':
  pass
```

Ahora añadimos la url o **endpoint**, su **playload** y el **header** de acceso:

```diff
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://developer.github.com/v3/oauth/

import requests

client_id = '369215fa00432fd6b039'
client_secret = 'rgknw34kln23l45kn234l5kn32l4k5n23lk45n23lk4522345'

code = '213412341234'

# https://github.com/login/oauth/authorize
if __name__ == '__main__':
-- pass
++ url = 'https://github.com/login/oauth/access_token'
++ payload = {'client_id': client_id, 'client_secret': client_secret, 'code': code}
++ headers = {'Accept': 'application/json'}
```

Realizamos la petición y alojamos la respuesta en una variable:

```diff
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://developer.github.com/v3/oauth/

import requests

client_id = '369215fa00432fd6b039'
client_secret = 'rgknw34kln23l45kn234l5kn32l4k5n23lk45n23lk4522345'

code = '213412341234'

# https://github.com/login/oauth/authorize
if __name__ == '__main__':
  url = 'https://github.com/login/oauth/access_token'
  payload = {'client_id': client_id, 'client_secret': client_secret, 'code': code}
  headers = {'Accept': 'application/json'}

++ response = requests.post(url, json=payload, headers=headers)
```

Y un condicional que difiera entra las opciones de respuesta, **200** -> **correct status**:

```diff
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://developer.github.com/v3/oauth/

import requests

client_id = '369215fa00432fd6b039'
client_secret = 'rgknw34kln23l45kn234l5kn32l4k5n23lk45n23lk4522345'

code = '213412341234'

# https://github.com/login/oauth/authorize
if __name__ == '__main__':
  url = 'https://github.com/login/oauth/access_token'
  payload = {'client_id': client_id, 'client_secret': client_secret, 'code': code}
  headers = {'Accept': 'application/json'}

  response = requests.post(url, json=payload, headers=headers)

++ if response.status_code = 200:
++    response_json = response.json()

++    access_token = responsse_json['access_token']
++    print(access_token)
```

Si ejecutasemos el script obtendríamos una respuesta como esta:

```bash
$ python main.py
12451234521345k123n45lk1n345lk1n2345kln132ñ4k5jñ1klj2345n
```

Ahora podríamos guardar este `access_token` en nuestro código:

```diff
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://developer.github.com/v3/oauth/

import requests

client_id = '369215fa00432fd6b039'
client_secret = 'rgknw34kln23l45kn234l5kn32l4k5n23lk45n23lk4522345'

code = '213412341234'
++ access_token = '12451234521345k123n45lk1n345lk1n2345kln132ñ4k5jñ1klj2345n'

# https://github.com/login/oauth/authorize
if __name__ == '__main__':
  url = 'https://github.com/login/oauth/access_token'
  payload = {'client_id': client_id, 'client_secret': client_secret, 'code': code}
  headers = {'Accept': 'application/json'}

  response = requests.post(url, json=payload, headers=headers)

  if response.status_code = 200:
    response_json = response.json()

    access_token = responsse_json['access_token']
    print(access_token)
```

Ahora seguiendo la documentación de la **Api** de **Github** podremos obtener datos como:

* username
* avatar
* biografía
* algunos repositorios

[Volver al inicio](#-oauth)