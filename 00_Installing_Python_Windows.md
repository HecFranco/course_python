# Instalación de Python en Windows

Podemos instalar **Python** directamente accediendo a su web, [https://www.python.org/](https://www.python.org/), y pulsando en la opción de descargar, [https://www.python.org/downloads/](https://www.python.org/downloads/), según nuestro S.O.

[Volver al inicio](#-instalación-de-python-en-windows)

## USANDO PYTHON SHELL

---------------------------------------------------------------------------

Al igual que otros lenguajes, **Python** dispone de una **Shell** (terminal) propia en la que poder trabajar. Para acceder a ella en windows podremos buscarla como **Python Shell**.

Una vez abierta la terminal, podremos ejecutar nuestro primer programa en **Python** mediante el comando de consola `print("Hello World")`.

```shell
Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print ("Hello World")
Hello World
>>>
```

[Volver al inicio](#-instalación-de-python-en-windows)

## USANDO PYTHON EN LA CMD DE WINDOWS

---------------------------------------------------------------------------

> **NOTA**: Previamente deberemos conocer la ubicación de nuestra instalación de **Python**. Deberá ser algo parecido a: [C:\Users\usuario\AppData\Local\Programs\Python\Python37-32](C:\Users\usuario\AppData\Local\Programs\Python\Python37-32)

Para ello deberemos acceder a la configuración de **variables de entorno** de nuestra instalación de **Windows**. La forma más rápida y sencilla de acceder a la configuración de las **Variables de entorno** de windows es escribiendo en el buscador (Cortana) mediante las keywords, **Variables Entorno**.

Una vez abierta la configruación accederemos a **Variables de Entorno** >> **Variables de usuario para <username>** >> **Path** >> **Editar**, aquí añadiremos la dirección de la instalación de **Python**.

Deberemos abrir una nueva terminal **CMD** de windows para poder tener **Python** Operativo.

```bash
Microsoft Windows [Versión 10.0.17134.407]
(c) 2018 Microsoft Corporation. Todos los derechos reservados.

C:\Users\usuario>python
Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

[Volver al inicio](#-instalación-de-python-en-windows)

## INSTALANDO PIP EN WINDOWS

---------------------------------------------------------------------------

**PIP** es un sistema de gestión de paquetes utilizado para instalar y administrar paquetes de software escritos en Python. 

> **NOTA**: Previamente deberemos conocer la ubicación de nuestra instalación de **Python** y **PIP**. Deberá ser algo parecido a: [C:\Users\usuario\AppData\Local\Programs\Python\Python37-32](C:\Users\usuario\AppData\Local\Programs\Python\Python37-32) y [C:\Users\usuario\AppData\Local\Programs\Python\Python37-32\Scripts](C:\Users\usuario\AppData\Local\Programs\Python\Python37-32\Scripts).

Para utilizarlo deberemos añadirlo en nuestras variables de entorno al igual que en el ejemplo anterior. 

Para ello deberemos acceder a la configuración de **variables de entorno** de nuestra instalación de **Windows**. La forma más rápida y sencilla de acceder a la configuración de las **Variables de entorno** de windows es escribiendo en el buscador (Cortana) mediante las keywords, **Variables Entorno**.

Una vez abierta la configruación accederemos a **Variables de Entorno** >> **Variables de usuario para <username>** >> **Path** >> **Editar**, aquí añadiremos la dirección de la instalación de **Python**.

Deberemos abrir una nueva terminal **CMD** de windows para poder tener **Python** Operativo.

```bash
Microsoft Windows [Versión 10.0.17134.407]
(c) 2018 Microsoft Corporation. Todos los derechos reservados.

C:\Users\usuario>pip

Usage:
  pip <command> [options]

Commands:
  install                     Install packages.
  download                    Download packages.
  uninstall                   Uninstall packages.
  freeze                      Output installed packages in requirements format.
  list                        List installed packages.
  show                        Show information about installed packages.
  check                       Verify installed packages have compatible dependencies.
  config                      Manage local and global configuration.
  search                      Search PyPI for packages.
  wheel                       Build wheels from your requirements.
  hash                        Compute hashes of package archives.
  completion                  A helper command used for command completion.
  help                        Show help for commands.

General Options:
  -h, --help                  Show help.
  --isolated                  Run pip in an isolated mode, ignoring environment variables and user configuration.
  -v, --verbose               Give more output. Option is additive, and can be used up to 3 times.
  -V, --version               Show version and exit.
  -q, --quiet                 Give less output. Option is additive, and can be used up to 3 times (corresponding to
                              WARNING, ERROR, and CRITICAL logging levels).
  --log <path>                Path to a verbose appending log.
  --proxy <proxy>             Specify a proxy in the form [user:passwd@]proxy.server:port.
  --retries <retries>         Maximum number of retries each connection should attempt (default 5 times).
  --timeout <sec>             Set the socket timeout (default 15 seconds).
  --exists-action <action>    Default action when a path already exists: (s)witch, (i)gnore, (w)ipe, (b)ackup,
                              (a)bort).
  --trusted-host <hostname>   Mark this host as trusted, even though it does not have valid or any HTTPS.
  --cert <path>               Path to alternate CA bundle.
  --client-cert <path>        Path to SSL client certificate, a single file containing the private key and the
                              certificate in PEM format.
  --cache-dir <dir>           Store the cache data in <dir>.
  --no-cache-dir              Disable the cache.
  --disable-pip-version-check
                              Don't periodically check PyPI to determine whether a new version of pip is available for
                              download. Implied with --no-index.
  --no-color                  Suppress colored output
```

> **NOTA**: Utilizaremos el comando `python -m pip install --upgrade pip` para actualizar nuestra versión de **PIP** si fuera necesario.

[Volver al inicio](#-instalación-de-python-en-windows)

## EJECUTAR NUESTRO PRIMER SCRIPT DE PYTHON EN CONSOLA

---------------------------------------------------------------------------

Para ejecutar nuestro primer **Script** de **Python** en consola crearemos un archivo con extensión python, `*.py`, el cual ejecutaremos. Este archivo además contendrá el siguiente código.

```python
# 00_first_example.py
print("Hello World")
```

Para ejecutarlo, dentro de la carpeta del proyecto llamaremos al archivo precedido del comando **python**, `python <file-name>`, tal que así:

```bash
$ python 00_first_example.py
Hello World
```

[Volver al inicio](#-instalación-de-python-en-windows)

## COMENTARIOS EN PYTHON

---------------------------------------------------------------------------

En **Python** existen dos tipos de comentarios:

* **Línea única**, se designará mediante el caracter `#`, por ejemplo `# Esto es un comentario`.
* **Línea múltiple**, se designará mediante una triple comilla `'''Esto es un comentario múltiple'''`, por ejemplo:

```python
'''Esto es un comentario
de múltiples líneas'''
```

## ESCRIBIR EN VARIAS LÍNEAS EN LA CONSOLA DE VISUAL STUDIO CODE

---------------------------------------------------------------------------

Para saltar de línea en el código de la consola de **Visual Studio Code** sin que se ejecute el código utilizaremos la combinacion de teclas `shift + intro`.

[Volver al inicio](#-instalación-de-python-en-windows)