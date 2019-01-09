# Funciones integradas comunes

[Volver al inicio](#-funciones-integradas-comunes)

## INT()

---------------------------------------------------------------------------

`int()`: Transforma una cadena a un entero (si no es posible da error)

```python
n = int("10")
n
# 10
```

[Volver al inicio](#-funciones-integradas-comunes)

## FLOAT()

---------------------------------------------------------------------------

`float()`: Transforma una cadena a un flotante (si no es posible da error)

```python
f = float("10.5")
f
10.5
```

[Volver al inicio](#-funciones-integradas-comunes)

## STR()

---------------------------------------------------------------------------

`str()`: Transforma cualquier valor a una cadena

```python
c = "Un texto y un número " + str(10) + " " + str(3.14)
c
# 'Un texto y un número 10 3.14'
```

[Volver al inicio](#-funciones-integradas-comunes)

## BIN()

---------------------------------------------------------------------------

`bin()`: Conversión de entero a binario

```python
bin(10)
# '0b1010'
```

[Volver al inicio](#-funciones-integradas-comunes)

## HEX()

---------------------------------------------------------------------------

`hex()`: Conversión de entero a hexadecimal

```python
hex(10)
# '0xa'
```

[Volver al inicio](#-funciones-integradas-comunes)

## INT() CON BASE

---------------------------------------------------------------------------

`int()` con base: Reconversión a entero (base 10)

```python
int('0b1010',2)
# 10
int('0xa',16)
# 10
```

[Volver al inicio](#-funciones-integradas-comunes)

## ABS()

---------------------------------------------------------------------------

`abs()`: Valor absoluto de un número (distancia)

```python
abs(-10)
# 10
abs(10)
# 10
```

[Volver al inicio](#-funciones-integradas-comunes)

## ROUND()

---------------------------------------------------------------------------

`round()`: Redondeo de un flotante a entero, menor de .5 a la baja, mayor o igual a .5 al alza

```python
round(5.5)
# 6
round(5.4)
# 5
```

[Volver al inicio](#-funciones-integradas-comunes)

## EVAL()

---------------------------------------------------------------------------

`eval()`: Evalúa una cadena como una expresión, acepta variables si se han definido anteriormente

```python
eval('2+5')
# 7
#n = 10
eval('n*10 - 5')
# 95
```

[Volver al inicio](#-funciones-integradas-comunes)

## LEN()

---------------------------------------------------------------------------

`len()`: Longitud de una colección o cadena

```python
len("Una cadena")
# 10
len([])
# 0
```

[Volver al inicio](#-funciones-integradas-comunes)

## HELP()

---------------------------------------------------------------------------

`help`(): Invocar el menú de ayuda del intérprete de Python

```python
help()
# Welcome to Python 3.5's help utility!

# If this is your first time using Python, you should definitely check out
# the tutorial on the Internet at http://docs.python.org/3.5/tutorial/.

# Enter the name of any module, keyword, or topic to get help on writing
# Python programs and using Python modules.  To quit this help utility and
# return to the interpreter, just type "quit".

# To get a list of available modules, keywords, symbols, or topics, type
# "modules", "keywords", "symbols", or "topics".  Each module also comes
# with a one-line summary of what it does; to list the modules whose name
# or summary contain a given string such as "spam", type "modules spam".

# help> topics

# Here is a list of available topics.  Enter any topic name to get more help.

# ASSERTION           DELETION            LOOPING             SHIFTING
# ASSIGNMENT          DICTIONARIES        MAPPINGMETHODS      SLICINGS
# ATTRIBUTEMETHODS    DICTIONARYLITERALS  MAPPINGS            SPECIALATTRIBUTES
# ATTRIBUTES          DYNAMICFEATURES     METHODS             SPECIALIDENTIFIERS
# AUGMENTEDASSIGNMENT ELLIPSIS            MODULES             SPECIALMETHODS
# BASICMETHODS        EXCEPTIONS          NAMESPACES          STRINGMETHODS
# BINARY              EXECUTION           NONE                STRINGS
# BITWISE             EXPRESSIONS         NUMBERMETHODS       SUBSCRIPTS
# BOOLEAN             FLOAT               NUMBERS             TRACEBACKS
# CALLABLEMETHODS     FORMATTING          OBJECTS             TRUTHVALUE
# CALLS               FRAMEOBJECTS        OPERATORS           TUPLELITERALS
# CLASSES             FRAMES              PACKAGES            TUPLES
# CODEOBJECTS         FUNCTIONS           POWER               TYPEOBJECTS
# COMPARISON          IDENTIFIERS         PRECEDENCE          TYPES
# COMPLEX             IMPORTING           PRIVATENAMES        UNARY
# CONDITIONAL         INTEGER             RETURNING           UNICODE
# CONTEXTMANAGERS     LISTLITERALS        SCOPING             
# CONVERSIONS         LISTS               SEQUENCEMETHODS     
# DEBUGGING           LITERALS            SEQUENCES           

# help> ATRIBUTES
# No Python documentation found for 'ATRIBUTES'.
# Use help() to get the interactive help utility.
# Use help(str) for help on the str class.

# help> ATTRIBUTES
# Attribute references
# ********************

# An attribute reference is a primary followed by a period and a name:

#    attributeref ::= primary "." identifier

# The primary must evaluate to an object of a type that supports
# attribute references, which most objects do.  This object is then
# asked to produce the attribute whose name is the identifier.  This
# production can be customized by overriding the "__getattr__()" method.
# If this attribute is not available, the exception "AttributeError" is
# raised.  Otherwise, the type and value of the object produced is
# determined by the object.  Multiple evaluations of the same attribute
# reference may yield different objects.

# Related help topics: getattr, hasattr, setattr, ATTRIBUTEMETHODS
```

[Volver al inicio](#-funciones-integradas-comunes)