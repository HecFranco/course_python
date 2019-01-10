# http://pockeapi.co
import requests
import json

if __name__ == '__main__':
  url = 'http://pokeapi.co/api/v2/pokemon-form/'
  response = requests.get(url) 
  if response.status_code == 200:
    payload = response.json()
    results = payload.get('results', []) # si no obtenemos el parámetro 'results' dentro del resultado me devuelves []
    if results:
      for pokemon in results:
          name = pokemon['name']
          print(name)