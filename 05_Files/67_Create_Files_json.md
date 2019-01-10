# Archivos JSON

Durante los últimos 5-10 años, el formato **JSON** ha sido una de las formas más populares, si no la más popular, de serializar datos. Especialmente en el mundo del desarrollo web, es probable que encuentre a **JSON** a través de una de las muchas **APIs** de **REST**, configuración de aplicaciones, o incluso almacenamiento de datos simples.

Dada su prevalencia e impacto en la programación, en algún momento de su desarrollo probablemente querrá aprender a leer **JSON** desde un archivo o escribir JSON en un archivo. Ambas tareas son bastante fáciles de realizar con Python, como verás en las siguientes secciones.

[Volver al inicio](#-archivos-json)

## ESCRIBIR JSON EN UN ARCHIVO

---------------------------------------------------------------------------

La forma más fácil de escribir sus datos en formato **JSON** en un archivo utilizando Python es almacenar sus datos en un objeto `dict`, que puede contener otros `dicts` anidados, arrays, booleans, u otros tipos primitivos como enteros y cadenas. Puede encontrar una lista más detallada de los tipos de datos soportados aquí.

El paquete `json` incorporado tiene el código mágico que transforma su objeto **Python** `dict` en la cadena **JSON serializada**.

```python
import json

data = {}  
data['people'] = []  
data['people'].append({  
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({  
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({  
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

with open('data.json', 'w') as outfile:  
    json.dump(data, outfile)
```

Después de importar la librería **json**, construimos unos datos sencillos para escribir en nuestro archivo. La parte importante viene al final cuando usamos la sentencia `with` para abrir nuestro archivo de destino, luego usamos `json.dump` para escribir el objeto de datos en el archivo **outfile**.

Cualquier objeto similar a un archivo se puede pasar al segundo argumento, incluso si no es un archivo real. Un buen ejemplo de esto sería un socket, que puede ser abierto, cerrado y escrito como un archivo. Con **JSON** siendo popular en toda la web, este es otro caso de uso que puede encontrar.

Una ligera variación del método json.dump que vale la pena mencionar es json.dumps, que devuelve la cadena **JSON** real en lugar de enviarla directamente a un objeto escribible. Esto puede darle más control si necesita hacer algunos cambios en la cadena **JSON** (como encriptarla, por ejemplo).

[Volver al inicio](#-archivos-json)

## LEER JSON DESDE UN ARCHIVO

---------------------------------------------------------------------------

Por otro lado, leer los datos JSON desde un archivo es tan fácil como escribirlos en un archivo. Utilizando de nuevo el mismo paquete json, podemos extraer y analizar la cadena JSON directamente desde un objeto de archivo. En el siguiente ejemplo, hacemos exactamente eso y luego imprimimos los datos que obtuvimos:

```python
import json

with open('data.json') as json_file:  
    data = json.load(json_file)
    for p in data['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')
```

`json.load` es el método importante a tener en cuenta aquí. Lee la cadena del archivo, analiza los datos de JSON, rellena un dictado de **Python** con los datos y se los devuelve.

Al igual que `json.dum`p, `json.load` tiene un método alternativo que le permite manejar cadenas directamente ya que muchas veces probablemente no tendrá un objeto similar a un archivo que contenga su **JSON**. Como probablemente adivinó, este método es `json.loads`.

Considere el caso en el que está llamando a un endpoint **REST** del tipo **GET** que devuelve **JSON**. Estos datos vienen a usted como una cadena, la cual puede pasar a `json.loads` directamente en su lugar.

> **NOTA**: al tratarse de un array de objetos podemos también imprimir el objeto que deseemos:

```python
import json

with open('data.json') as json_file:  
    data = json.load(json_file)
    p = data['people'][1]
    print('Name: ' + p['name'])
    print('Website: ' + p['website'])
    print('From: ' + p['from'])
    print('')
```

[Volver al inicio](#-archivos-json)

## OPTIONS

---------------------------------------------------------------------------

Al serializar sus datos a **JSON** con **Python**, el resultado será en el formato estándar y no muy legible ya que se eliminan los espacios en blanco. Aunque este es el comportamiento ideal para la mayoría de los casos, a veces puede ser necesario hacer pequeños cambios, como añadir espacios en blanco para que sea legible para el ser humano. Tanto `json.dump` como `json.load` ofrecen varias opciones para una mayor flexibilidad, algunas de las cuales se describen a continuación.

[Volver al inicio](#-archivos-json)

### PRETTY-PRINTING

---------------------------------------------------------------------------

Hacer que **JSON** sea legible para el ser humano (también conocido como "`pretty printing`") es tan fácil como pasar un valor entero para el parámetro de sangría:

```python
import json
data = {'people':[{'name': 'Scott', 'website': 'stackabuse.com', 'from': 'Nebraska'}]}
json.dumps(data, indent=4)
# {
#     "people": [
#         {
#             "website": "stackabuse.com", 
#             "from": "Nebraska", 
#             "name": "Scott"
#         }
#     ]
# }
```

Esto es realmente muy útil ya que a menudo tendrá que leer los datos de **JSON** durante el desarrollo. Otra opción es usar la herramienta de línea de comandos, `json.tool`. Así que si sólo quieres imprimir **JSON** en la línea de comandos puedes hacer algo como esto:

```bash 
$ echo '{"people":[{"name":"Scott", "website":"stackabuse.com", "from":"Nebraska"}]}' | python -m json.tool
# {
#     "people": [
#         {
#             "website": "stackabuse.com", 
#             "from": "Nebraska", 
#             "name": "Scott"
#         }
#     ]
# }
```

[Volver al inicio](#-archivos-json)

### SORTING

---------------------------------------------------------------------------

En JSON, un objeto se define como: **Un objeto es un conjunto desordenado de pares nombre/valor.**

Así que el estándar dice que el orden de las llaves no está garantizado, pero es posible que lo necesite para sus propios fines internamente. Para lograr el orden, puede pasar Fiel a la opción `sort_keys` cuando utilice `json.dump` o `json.dumps`.

```python 
import json
data = {'people':[{'name': 'Scott', 'website': 'stackabuse.com', 'from': 'Nebraska'}]}
json.dumps(data, sort_keys=True, indent=4)
# {
#     "people": [
#         {
#             "from": "Nebraska", 
#             "name": "Scott"
#             "website": "stackabuse.com", 
#         }
#     ]
# }
```

[Volver al inicio](#-archivos-json)

### ASCII TEXT

---------------------------------------------------------------------------

Por defecto, `json.dump` se asegurará de que todo el texto del diccionario **Python** esté codificado en **ASCII**. Si hay caracteres no **ASCII** presentes, se escapan automáticamente, como se muestra en el siguiente ejemplo:

```python 
import json
data = {'item': 'Beer', 'cost':'£4.00'}
jstr = json.dumps(data, indent=4)
print(jstr)
# {
#     "item": "Beer",
#     "cost": "\u00a34.00"
# }
```

Esto no siempre es aceptable, y en muchos casos puede que quieras mantener tus caracteres Unicode sin tocar. Para ello, establezca la opción ensure_ascii en False.

```python 
import json
data = {'item': 'Beer', 'cost':'£4.00'}
jstr = json.dumps(data, ensure_ascii=False, indent=4)
print(jstr)
# {
#     "item": "Beer",
#     "cost": "£4.00"
# }
```

[Volver al inicio](#-archivos-json)