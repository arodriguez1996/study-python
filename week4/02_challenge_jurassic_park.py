from os import system
system('clear')


"""
En Jurassic Park, se ha observado que los dinosaurios carnívoros, como el temible T-Rex, 
depositan un número par de huevos. 
Imagina que tienes una lista de números enteros en la que cada número
representa la cantidad de huevos puestos por un dinosaurio en el parque.

Importante: Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) aquellos números que son pares.

Objetivo:
Escribe una función en Python que reciba una lista de números enteros y 
devuelva la suma total de los huevos que pertenecen a 
los dinosaurios carnívoros (es decir, la suma de todos los números pares en la lista).
"""

def sum_huevo_carnivoro(arr):
    acc = 0
    for num in arr:
        if num % 2 == 0:
            acc += num
    return acc


a = [2, 3, 4, 5, 6, 7, 8, 9]
print(f'Cantidad de huevos de carnivoros: {sum_huevo_carnivoro(a)}')
