#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://pockeapi.co
import requests
import json

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

    next = input("¿Continuar listando? [Y/N]").lower()
    if next == 'y':
      get_pokemons(offset=offset+20)

if __name__ == '__main__':
  get_pokemons()
