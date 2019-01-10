# Archivos XML

XML, o **Extensible Markup Language**, es un lenguaje de marcado que se utiliza comúnmente para estructurar, almacenar y transferir datos entre sistemas. Aunque no es tan común como solía ser, todavía se utiliza en servicios como **RSS** y **SOAP**, así como para estructurar archivos como documentos de Microsoft Office.

Dado que **Python** es un lenguaje popular para la web y el análisis de datos, es probable que necesite leer o escribir datos **XML** en algún momento, en cuyo caso estará de suerte.

A continuación echaremos un vistazo al módulo **ElementTree** para **leer**, **escribir** y **modificar** datos XML. También lo compararemos con el módulo de **minidom** más antiguo en las primeras secciones para que pueda obtener una buena comparación de los dos.

[Volver al inicio](#-archivos-xml)

## LOS MÓDULOS XML

---------------------------------------------------------------------------

El **minidomo**, o **Minimal DOM Implementation**, es una implementación simplificada del **Document Object Model (DOM)**. El **DOM** es una interfaz de programación de aplicaciones que trata **XML** como una estructura de árbol, donde cada nodo del árbol es un objeto. Por lo tanto, el uso de este módulo requiere que estemos familiarizados con su funcionalidad.

El módulo **ElementTree** proporciona una interfaz más **"Pythonic"** para el manejo de **XMl** y es una buena opción para aquellos que no están familiarizados con el **DOM**. También es probable que sea un mejor candidato para ser usado por más programadores novatos debido a su sencilla interfaz, que verá a lo largo de este artículo.

El módulo **ElementTree** se utilizará en todos los ejemplos, mientras que el **minidomo** también se demostrará, pero sólo para contar y leer documentos XML.

[Volver al inicio](#-archivos-xml)

## EJEMPLO DE ARCHIVO XML

---------------------------------------------------------------------------

En los ejemplos siguientes, utilizaremos el siguiente archivo **XML**, que guardaremos como [items.xml](./Examples/items.xml):

```xml
<data>  
    <items>
        <item name="item1">item1abc</item>
        <item name="item2">item2abc</item>
    </items>
</data>  
```

Como puede ver, es un ejemplo XML bastante simple, que sólo contiene unos pocos objetos anidados y un atributo. Sin embargo, debería ser suficiente para demostrar todas las operaciones XML de este artículo.

[Volver al inicio](#-archivos-xml)

## LECTURA DE DOCUMENTOS XML

--------------------------------------------------------------------------

[Volver al inicio](#-archivos-xml)

### USANDO MINIDOM

--------------------------------------------------------------------------

Para poder analizar un documento **XML** usando **minidom**, primero debemos importarlo desde el módulo `xml.dom`. Este módulo utiliza la función de análisis para crear un objeto DOM a partir de nuestro archivo `XML`. La función de análisis tiene la siguiente sintaxis:

```python
xml.dom.minidom.parse(filename_or_file[, parser[, bufsize]])  
```

Aquí el nombre del archivo puede ser una cadena que contiene la ruta del archivo o un objeto de tipo archivo. La función devuelve un documento, que puede tratarse como un tipo XML. Así, podemos usar la función `getElementByTagName()` para encontrar una etiqueta específica.

Dado que cada nodo puede ser tratado como un objeto, podemos acceder a los atributos y al texto de un elemento utilizando las propiedades del objeto. En el siguiente ejemplo, hemos accedido a los atributos y texto de un nodo específico y de todos los nodos juntos.

```python
from xml.dom import minidom

# analizar un archivo xml por nombre
mydoc = minidom.parse('items.xml')

items = mydoc.getElementsByTagName('item')

# un atributo de artículo específico
print('Item #2 attribute:')  
print(items[1].attributes['name'].value)

# todos los atributos del artículo
print('\nAll attributes:')  
for elem in items:  
    print(elem.attributes['name'].value)

# los datos de una posición específica
print('\nItem #2 data:')  
print(items[1].firstChild.data)  
print(items[1].childNodes[0].data)

# todos los datos de posición
print('\nAll item data:')  
for elem in items:  
    print(elem.firstChild.data)
```

El resultado sería el siguiente:

```bash
$ python minidomparser.py 
# Item #2 attribute:  
# item2

# All attributes:  
# item1  
# item2

# Item #2 data:  
# item2abc  
# item2abc

# All item data:  
# item1abc  
# item2abc  
```
 
Si queríamos usar un archivo ya abierto, podemos pasar nuestro objeto de archivo a analizar así:

```python
datasource = open('items.xml')
# parse an open file
mydoc = parse(datasource)

mydoc2 = parseString('<myxml>Some data<empty/> some more data</myxml>')
```  

Además, si los datos XML ya estaban cargados como una cadena, podríamos haber usado la función `parseString()` en su lugar.

[Volver al inicio](#-archivos-xml)

### USANDO ELEMENTTREE

--------------------------------------------------------------------------

ElementTree nos presenta una forma muy sencilla de procesar archivos XML. Como siempre, para poder utilizarlo primero debemos importar el módulo. 

```python
import xml.etree.ElementTree as ET
```

En nuestro código utilizamos el comando de importación con la palabra clave "como", lo que nos permite utilizar un nombre simplificado (`ET` en este caso) para el módulo en el código.

Tras la importación, creamos una estructura de árbol con la función de análisis, y obtenemos su elemento raíz. Una vez que tenemos acceso al nodo raíz podemos fácilmente atravesar el árbol, porque un árbol es una gráfica conectada.

Utilizando `ElementTree`, y como en el ejemplo anterior, obtenemos los atributos y el texto del nodo utilizando los objetos relacionados con cada nodo.

Nuestro ejemplo sería así:

```python
import xml.etree.ElementTree as ET  
tree = ET.parse('items.xml')  
root = tree.getroot()

# one specific item attribute
print('Item #2 attribute:')  
print(root[0][1].attrib)

# all item attributes
print('\nAll attributes:')  
for elem in root:  
    for subelem in elem:
        print(subelem.attrib)

# one specific item's data
print('\nItem #2 data:')  
print(root[0][1].text)

# all items data
print('\nAll item data:')  
for elem in root:  
    for subelem in elem:
        print(subelem.text)
```

Y el resultado obtendio el siguiente:

```bash
$ python treeparser.py 
# Item #2 attribute:  
# item2

# All attributes:  
# item1  
# item2

# Item #2 data:  
# item2abc

# All item data:  
# item1abc  
# item2abc  
```

Como puedes ver, esto es muy similar al ejemplo del `minidomo`. Una de las principales diferencias es que el objeto `attrib` es simplemente un objeto diccionario, lo que lo hace un poco más compatible con otro código **Python**. Tampoco necesitamos usar valor para acceder al valor del atributo del elemento como lo hacíamos antes.

Puede que haya notado que el acceso a objetos y atributos con `ElementTree` es un poco más pitónico, como hemos mencionado antes. Esto se debe a que los datos XML se analizan como simples listas y diccionarios, a diferencia de `minidom`, donde los elementos se analizan como `xml.dom.minidom.Attr` y "`DOM Text nodes`" personalizados.

[Volver al inicio](#-archivos-xml)

## CONTAR LOS ELEMENTOS DE UN DOCUMENTO XML

--------------------------------------------------------------------------

[Volver al inicio](#-archivos-xml)

### USANDO MINIDOM

--------------------------------------------------------------------------

Como en el caso anterior, el `minidomo` debe ser importado desde el módulo `dom`. Este módulo proporciona la función `getElementsByTagName`, que usaremos para encontrar el elemento `tag`. Una vez obtenido, utilizamos el método `len()` integrado para obtener el número de subítems conectados a un nodo. El resultado obtenido a partir del código que figura a continuación se muestra.

```python
from xml.dom import minidom

# parse an xml file by name
mydoc = minidom.parse('items.xml')

items = mydoc.getElementsByTagName('item')

# total amount of items
print(len(items))  
```

El resultado obtenido será el siguiente:

```bash
$ python counterxmldom.py
# 2  
```

Tenga en cuenta que esto sólo contará el número de ítems hijo bajo la nota en la que ejecute en `len()`, que en este caso es el nodo raíz. Si quieres encontrar todos los subelementos en un árbol mucho más grande, tendrás que atravesar todos los elementos y contar a cada uno de sus hijos.

[Volver al inicio](#-archivos-xml)

### USANDO ELEMENTTREE

--------------------------------------------------------------------------

Del mismo modo, el módulo `ElementTree` nos permite calcular la cantidad de nodos conectados a un nodo.

Ejemplo de código:

```python
import xml.etree.ElementTree as ET  
tree = ET.parse('items.xml')  
root = tree.getroot()

# total amount of items
print(len(root[0]))  
```

Obtendremos el siguiente resultado

```bash
$ python counterxml.py
# 2  
```

[Volver al inicio](#-archivos-xml)

## ENCONTRANDO XML ELEMENTS

--------------------------------------------------------------------------

[Volver al inicio](#-archivos-xml)

### USANDO ELEMENTTREE

--------------------------------------------------------------------------

El módulo `ElementTree` ofrece la función `findall()`, que nos ayuda a encontrar elementos específicos en el árbol. Devuelve todas las posiciones con la condición especificada. Además, el módulo tiene la función `find()`, que devuelve sólo el primer subelemento que cumple los criterios especificados. La sintaxis de ambas funciones es la siguiente:

```python 
findall(match, namespaces=None)  
find(match, namespaces=None)  
```

Para ambas funciones, el parámetro `match` puede ser un nombre de etiqueta XML o una ruta. La función `findall()` devuelve una lista de elementos, y find devuelve un solo objeto de tipo Element.

Además, hay otra función de ayuda que devuelve el texto del primer nodo que coincide con el criterio dado:

```python
findtext(match, default=None, namespaces=None)  
```

Aquí hay un código de ejemplo para mostrarle exactamente cómo funcionan estas funciones:

```python
import xml.etree.ElementTree as ET  
tree = ET.parse('items.xml')  
root = tree.getroot()

# find the first 'item' object
for elem in root:  
    print(elem.find('item').get('name'))

# find all "item" objects and print their "name" attribute
for elem in root:  
    for subelem in elem.findall('item'):

        # if we don't need to know the name of the attribute(s), get the dict
        print(subelem.attrib)      

        # if we know the name of the attribute, access it directly
        print(subelem.get('name'))
```

Y aquí está el resultado de ejecutar este código:

```bash
$ python findtree.py 
item1  
{'name': 'item1'}
item1  
{'name': 'item2'}
item2  
```

![Fuente: https://stackabuse.com/reading-and-writing-xml-files-in-python/](https://stackabuse.com/reading-and-writing-xml-files-in-python/)