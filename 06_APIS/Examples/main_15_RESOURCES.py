import requests
import json

if __name__ == '__main__':
  url = 'http://i.imgur.com/n9z3sLg.jpg'
  response = requests.get(url, stream=True) # realiza la petición sin descargar el contenido
  with open('./05_APIS/Examples/image.jpg', 'wb') as file: # escritura binaria 'wb'
      for chunk in response.iter_content(): # Descarga el contenido pesado poco a poco
        file.write(chunk) # guardamos la porción de archivo en descarga
  response.close() # cerramos la conexión