from os import system
system('clear')
"""
¿Está en Equilibrio la Alianza entre Reed Richards y Johnny Storm?

En el universo de los 4 Fantásticos, la unión y el equilibrio entre los poderes es fundamental para enfrentar cualquier desafío. 
En este problema, nos centraremos en dos de sus miembros:

Reed Richards (Mr. Fantastic), representado por la letra R.
Johnny Storm (La Antorcha Humana), representado por la letra J.

Objetivo:

Crea una función en Python que reciba una cadena de texto. 
Esta función debe contar cuántas veces aparece la letra R (para Reed Richards) y 
cuántas veces aparece la letra J (para Johnny Storm) en la cadena.

- Si la cantidad de R y la cantidad de J son iguales, 
    se considera que la alianza entre la mente y el fuego está en equilibrio y la función debe retornar True.
- Si las cantidades no son iguales, la función debe retornar False.
- En el caso de que no aparezca ninguna de las dos letras en la cadena, 
    se entiende que el equilibrio se mantiene (0 = 0), por lo que la función debe retornar True.
"""

text = "RRRRJJJjjjrrr"


def aliance(text: str) -> bool:
    text = text.upper()
    r_count = text.count('R')
    j_count = text.count('J')

    # r_count = 0
    # j_count = 0

    # for t in text:
    #     if t.lower() == "r" :
    #         r_count += 1
    #     elif t.lower() == 'j':
    #         j_count += 1

    print(f'r_count: {r_count}')
    print(f'j_count: {j_count}')

    return r_count == j_count



print(f'Hay alianza? : {aliance(text)}')