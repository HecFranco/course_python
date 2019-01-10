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