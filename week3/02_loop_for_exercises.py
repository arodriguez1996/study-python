from os import system
system("clear")
###
# EJERCICIOS (for)
###

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
# print("\nEjercicio 1:")

# for number in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:
#     if number % 2 == 0:
#         print(number)

# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
# print("\nEjercicio 2:")

# acc = 0
# for number in numeros:
#     acc += number

# print(f'la media es {acc / len(numeros)}')


# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
# print("\nEjercicio 3:")

# max = 0

# for number in numeros:
#     if(number > max):
#         max = number

# print(f'The max number is {max}')

# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
# print("\nEjercicio 4:")

# new_list = [p for p in palabras if len(p) > 5]

# print(new_list)

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
# print("\nEjercicio 5:")

palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
letter = input('ingresa una letra: \n').lower()
words = [p for p in palabras if p[0].lower().startswith(letter)]

print(f' words : {len(words)}')

