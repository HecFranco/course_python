# http://pockeapi.co
import requests
import json

if __name__ == '__main__':
  url = 'http://pokeapi.co/api/v2/pokemon-form/'
  response = requests.get(url) 