# El módulo datetime

El módulo de **datetime** proporciona clases para manipular fechas y horas tanto de forma sencilla como compleja. Mientras que la aritmética de fecha y hora es soportada, el foco de la implementación está en la extracción eficiente de atributos para el formateo y manipulación de la salida. Para conocer las funciones relacionadas, consulte también los módulos de hora y calendario.

```python
import datetime
```

[Volver al inicio](#-el-método-datetime)

## OBJETO DATETIME

---------------------------------------------------------------------------

```python
import datetime

dt = datetime.datetime.now() # Ahora
dt
# datetime.datetime(2016, 6, 18, 21, 29, 28, 607208)
dt.year # año
# 2016
dt.month # mes
# 6
dt.day # día
# 18
dt.hour # hora
# 21
dt.minute # minutos
# 29
dt.second # segundos
# 28
dt.microsecond # microsegundos
# 607208
dt.tzinfo # zona horaria, nula por defecto
print("{}:{}:{}".format(dt.hour, dt.minute, dt.second))
# 21:29:28
print("{}/{}/{}".format(dt.day, dt.month, dt.year))
# 18/6/2016
```

[Volver al inicio](#-el-método-datetime)

## CREAR UN DATETIME MANUALMENTE

---------------------------------------------------------------------------

Crear un **datetime** manualmente (year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None)

> **NOTA**: Sólo son obligatorios el año, el mes y el día

```python
import datetime

dt = datetime.datetime(2000,1,1)
dt
# datetime.datetime(2000, 1, 1, 0, 0)
dt.year = 3000 # Error en asignación
# ---------------------------------------------------------------------------
# AttributeError                            Traceback (most recent call last)
# <ipython-input-18-f655491f2afa> in <module>()
# ----> 1 dt.year = 3000
# AttributeError: attribute 'year' of 'datetime.date' objects is not writable
dt = dt.replace(year=3000) # Asignación correcta con .replace()
dt
# datetime.datetime(3000, 1, 1, 0, 0)
```

[Volver al inicio](#-el-método-datetime)

## FORMATEOS

---------------------------------------------------------------------------

El formato automático de **datetime** es ISO (Organización Internacional de Normalización)

```python
import datetime

dt = datetime.datetime.now()

dt.isoformat()
# '2016-06-18T21:37:10.303386'
```

[Volver al inicio](#-el-método-datetime)

## FORMATEO MANUAL

---------------------------------------------------------------------------

> **FUENTE**: Formateo munual (inglés por defecto) [https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)

```python
import datetime

dt.strftime("%A %d %B %Y %I:%M")
# 'Saturday 18 June 2016 09:37'
```

[Volver al inicio](#-el-método-datetime)

## CÓDIGOS DE IDIOMAS

---------------------------------------------------------------------------

> **FUENTE**: Códigos de idiomas [https://msdn.microsoft.com/es-es/es/library/cdax410z.aspx](https://msdn.microsoft.com/es-es/es/library/cdax410z.aspx)

```python
import locale

locale.setlocale(locale.LC_ALL, 'es-ES') # Establece idioma en "es-ES" (español de España)
# 'es-ES'
dt.strftime("%A %d %B %Y %I:%M")
# 'sábado 18 junio 2016 09:37'
dt.strftime("%A %d de %B del %Y - %H:%M") # %I 12h - %H 24h
# 'sábado 18 de junio del 2016 - 21:37'
```

[Volver al inicio](#-el-método-datetime)

## SUMANDO Y RESTANDO TIEMPO CON TIMEDELTA

---------------------------------------------------------------------------

```python
import datetime

dt = datetime.datetime.now()
dt
# datetime.datetime(2016, 6, 18, 21, 47, 13, 504534)
t = datetime.timedelta(days=14, hours=4, seconds=1000)
dentro_de_dos_semanas = dt + t
dentro_de_dos_semanas
# datetime.datetime(2016, 7, 3, 2, 3, 53, 504534)
dentro_de_dos_semanas.strftime("%A %d de %B del %Y - %H:%M")
# 'domingo 03 de julio del 2016 - 02:03'
hace_dos_semanas = dt - t
hace_dos_semanas.strftime("%A %d de %B del %Y - %H:%M")
# 'sábado 04 de junio del 2016 - 17:30'
```

[Volver al inicio](#-el-método-datetime)

## EXTRA: ZONAS HORARIAS CON PYTZ

---------------------------------------------------------------------------

Para ejecutar esta funcionalidad de **Python** es necesario previamente haber instalado el **pip** relacionado `pip3 install pytz`.

```bash
$ pip3 install pytz
```

```python
import pytz

pytz.all_timezones
# ['Africa/Abidjan',
# 'Africa/Accra',
# 'Africa/Addis_Ababa',
# 'Africa/Algiers',
# 'Africa/Asmara',
# 'Africa/Asmera',
# ...
# 'US/Pacific',
# 'US/Pacific-New',
# 'US/Samoa',
# 'UTC',
# 'Universal',
# 'W-SU',
# 'WET',
# 'Zulu']
dt = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
dt.strftime("%A %d de %B del %Y - %H:%M") # %I 12h - %H 24h
# 'domingo 19 de junio del 2016 - 04:52'
```

[Volver al inicio](#-el-método-datetime)