# Sesiones

[Volver al inicio](#-sesiones)

## SCRIPT SESIONES

---------------------------------------------------------------------------

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://developer.github.com/v3/oauth/

import requests

if __name__ == '__main__':
  url = 'https://api.github.com/user'

  session = request.session()
  session.auth = ( 'demon@gmail.com', '1234' )

  response = session.get(url)

  if response.ok:
    response = session.get('https://github.com/demoncfApi')

    if response.ok:
      print(response.cookies)

