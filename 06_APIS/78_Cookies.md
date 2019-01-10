# Cookies

[Volver al inicio](#-cookies)

## COOKIES

---------------------------------------------------------------------------

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

if __name__ == '__main__':
  url = 'http://httpbin.org/cookies'
  response = requests.get(url)
  if response.ok:
    cookies = response.cookies
    print(cookies)

    print("El contenido es: ")
    print(response.content)
```

```bash
$ python d:/00.ProyectosWeb/python-by-sample/06_APIS/Examples/
78_01.py
<RequestsCookieJar[]>
El contenido es:
b'{\n  "cookies": {}\n}\n'
```

```diff
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

if __name__ == '__main__':
  url = 'http://httpbin.org/cookies'
++  cookies = {'my-cookie': 'true'}

-- response = requests.get(url)
++ response = requests.get(url, cookies = cookies)
  if response.ok:
    cookies = response.cookies
    print(cookies)

    print("El contenido es: ")
    print(response.content)
```

```bash
$ python d:/00.ProyectosWeb/python-by-sample/06_APIS/Examples/
78_02.py
<RequestsCookieJar[]>
El contenido es:
b'{\n  "cookies": { "my-cookie": "true"}\n}\n'
```

Estamos enviando las cookies de forma correcta ya que obtenemos la respuesta, sin embargo el objeto `<RequestsCookieJar[]>` aún se encuentra vacío y eso se debe a que el servidor **httpbin.org** no nos está mandando ningún tipo de cookie por lo regular las cookies nos la van a mandar cuando nosotros estemos autenticados es decir cuando tengamos una sesión.

[Volver al inicio](#-cookies)