# Obtener Repositorios

[Volver al inicio](#-obtener-repositorios)

## REPOSITORIOS

---------------------------------------------------------------------------

Ya tenemos nuestro `access token`, lo que nos permite acceder a diferentes datos de la aplicación, entre ellos los repositorios

> **IMPORTANTE**: Por lo regular un `access token` tiene un periodo de vida y que por lo regular en ese periodo de vida es de dos horas una vez ese tiempo haya transcurrido el `access token` deja de ser útil y el servidor empieza a retornar un **error 403** de autorización no válida.

Con los datos obtendios generaremos nuestro **endpoint**, [https://api.github.com/user/repos](https://api.github.com/user/repos) que devuelva los repositorios:

( Source [https://developer.github.com/v3/repos/#get](https://developer.github.com/v3/repos/#get))

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://developer.github.com/v3/oauth/

import requests

client_id = '369215fa00432fd6b039'
client_secret = 'rgknw34kln23l45kn234l5kn32l4k5n23lk45n23lk4522345'

code = '213412341234'
access_token = '12451234521345k123n45lk1n345lk1n2345kln132ñ4k5jñ1klj2345n'

# https://github.com/login/oauth/authorize
if __name__ == '__main__':
  url = 'https://api.github.com/user/repos'
  payload = {'client_id': client_id, 'client_secret': client_secret, 'code': code}
  headers = {'Accept': 'token 12451234521345k123n45lk1n345lk1n2345kln132ñ4k5jñ1klj2345n'}

  response = requests.get(url, headers=headers)

  if response.status_code = 200:
    pass
  else: 
    print(response.content)
```

Si accedemos a la url de la documentación oficial veremos el objeto tipo devuelto:

```json
[
  {
    "id": 1296269,
    "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
    "name": "Hello-World",
    "full_name": "octocat/Hello-World",
    "owner": {
      "login": "octocat",
      "id": 1,
      "node_id": "MDQ6VXNlcjE=",
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "html_url": "https://github.com/octocat",
      "followers_url": "https://api.github.com/users/octocat/followers",
      "following_url": "https://api.github.com/users/octocat/following{/other_user}",
      "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
      "organizations_url": "https://api.github.com/users/octocat/orgs",
      "repos_url": "https://api.github.com/users/octocat/repos",
      "events_url": "https://api.github.com/users/octocat/events{/privacy}",
      "received_events_url": "https://api.github.com/users/octocat/received_events",
      "type": "User",
      "site_admin": false
    },
    //...
  }
]
```

Nosotros trabajaremos con el elemento `name` del objeto:

```diff
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://developer.github.com/v3/oauth/

import requests

client_id = '369215fa00432fd6b039'
client_secret = 'rgknw34kln23l45kn234l5kn32l4k5n23lk45n23lk4522345'

code = '213412341234'
access_token = '12451234521345k123n45lk1n345lk1n2345kln132ñ4k5jñ1klj2345n'

# https://github.com/login/oauth/authorize
if __name__ == '__main__':
  url = 'https://api.github.com/user/repos'
  payload = {'client_id': client_id, 'client_secret': client_secret, 'code': code}
  headers = {'Accept': 'token 12451234521345k123n45lk1n345lk1n2345kln132ñ4k5jñ1klj2345n'}

  response = requests.get(url, headers=headers)

  if response.status_code = 200:
--  pass
++  payload = response.json()

++  for project in payload:
++    name = project['name']
++    print (name)
  else: 
    print(response.content)
```

Al ejecutar el script obtendremos el nombre (**name**) de todos los repositorios del usuario authentificado.

```bash
$ python main.py

course_python
Symfony4-Vue3-Vuex-App-Cinemas
pf_course_s4
PF_Course
kit-starter-symfony-4-docker
vuejs-by-sample
Vue.js
Symfony-4-Supplier_-_Product_Manager
Symfony-4-ERP
Vuex-Supplier_-_Product_Manager
Symfony-4-by-Samples
Javascript-by-Samples
Symfony-3-by-Sample
Symfony-3-Social-Network
Symfony-4-Task-Manager
Symfony-4-Solve-Puzzle
React-Test
Lodash-by-Samples
Symfony-4-register-form
Symfony-4-Test
Symfony-3-ERPMedical
symfony4-vuejs-ssr
Notes
```

[Volver al inicio](#-obtener-repositorios)