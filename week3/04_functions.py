from os import system
system('clear')


""" Definicion de una funcion

def function_name(param1, param2...):
    #docstring
    #function code
    return valor_de_retorno #optional
"""


def hello():
    print('hello')

hello()
hello()


def hello_to(name):
    print(f"Hello : {name}")

hello_to('a')
hello_to('b')
hello_to('c')
hello_to('d')

def sumar(a, b):
    return a + b

print(sumar(123123, 213123))


# Documentation docstring

def restar(a, b):
    """Resta dos numeros y devuelve el resultado"""

    return a - b


print(restar(123, 321))
print(restar.__doc__)
# help(restar)


# default params

def multiplicar( a, b = 3):
    return a * b


print(multiplicar(10, 2))



def describe_person(name, age, gender):
    print(f'Hello i am {name}, i have {age} years old and im {gender}')

describe_person('Angel', 28, 'male')

# named params
def describe_person2(name="", gender="", age=0):
    print(f'Hello i am {name}, i have {age} years old and im {gender}')

describe_person2(age=28, gender="male", name="Angel")


def sumar_numeros(*args):
    suma = 0
    for numero in args:
        suma += numero
    return suma


print(sumar_numeros(1, 2, 3, 4, 5, 6, 7))


def show_information(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

show_information(name="angel", age=25, gender="male")
show_information(name="angel", age=25, country="Peru")
show_information(a="a", b="b", c="c")


def mixed(*args, **kwargs):
    for a in args:
        print(f'arg: {a}')

    for key, value in kwargs.items():
        print(f'kwarg: key={key} value={value}')


mixed(1, 2, 'hola', 'pedro', 1, hola="mundo", mundo="felix")