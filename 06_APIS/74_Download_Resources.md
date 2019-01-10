# Descarga de Recursos

En numerosas ocasiones nos encontraremos en la necesidad de descargar recursos relativamente pesados, tales como vídeos, pdf, img, ...

Para ello, tendremos que una vez realizada la conexión con el servidor para la petición que llevemos a cabo, no cerrarla de inmediato hasta que no se descargue el recurso completamente. Utilizando el atributo `stream=True` en la petición realizada, `response = requests.get(url, stream=True)`.

Además utilizaremos un ciclo que irá almacenando la información en el archivo designado:

```python
for chunk in response.iter_content(): # Descarga el contenido pesado poco a poco
    file.write(chunk) # guardamos la porción de archivo en descarga
```

Finalmente cerraremos la conexión mediante el método interno de response, `close()`.

Quedaría así nuestra petición de descarga de recursos.

```python
import requests
import json

if __name__ == '__main__':
  url = 'http://i.imgur.com/n9z3sLg.jpg'
  response = requests.get(url, stream=True) # realiza la petición sin descargar el contenido
  with open('./05_APIS/Examples/image.jpg', 'wb') as file: # escritura binaria 'wb'
      for chunk in response.iter_content(): # Descarga el contenido pesado poco a poco
        file.write(chunk) # guardamos la porción de archivo en descarga
  response.close() # cerramos la conexión
```

[Volver al inicio](#-descarga-de-recursos)
