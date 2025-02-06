from os import system
system("clear")
###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
# print("\nEjercicio 1:")

# counter = 10
# while counter > 0:
#     print(counter)
#     counter -= 1

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
# print("\nEjercicio 2:")

# counter = 1
# acc = 0
# while counter <= 20:            
#     acc += counter if counter % 2 == 0 else 0    
#     counter += 1

# print(f"Finish result: {acc}")


# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
# print("\nEjercicio 3:")

# number = -1
# while number < 0:
#     try:
#         number = int(input("type number positive \n"))
#         if number < 0:
#             print("the number is not positive\n")
#     except:
#         print("please enter a number\n")

# acc = 1
# print(f"Calculating !{number}...")
# while number >= 1:
#     acc *= number
#     number -= 1

# print(f"is: {acc}")


# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
# print("\nEjercicio 4:")

# password = ""
# while len(password) < 8:
#     password = input("Please add a password:\n")
#     if(len(password) < 8):
#         print("Password must have 8 or more characteres")

# print("password valid")

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
# print("\nEjercicio 5:")

# number = -1
# while number < 0:
#     try:
#         number = int(input("type number positive \n"))
#         if number < 0:
#             print("the number is not positive\n")
#     except:
#         print("please enter a number\n")

# print(f"Calculating multiples of {number}...")
# count = 1
# while count <= 10:
#     print(f"{number} x {count}: {number * count}")
#     count += 1



# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
# print("\nEjercicio 6:")

# number = -1
# while number < 0:
#     try:
#         number = int(input("type number positive \n"))
#         if number < 0:
#             print("the number is not positive\n")
#     except:
#         print("please enter a number\n")

# print(f"Calculating primos of {number}")

# counter = 1
# while counter <= number:
#     counter2 = 1
#     acc = 0
#     while counter2 <= counter:
#         if counter % counter2 == 0:
#            acc += 1
#         counter2 += 1
#     if acc <= 2:
#         print(counter)
#     counter += 1    

# n = int(input("Introduce un número entero positivo N: "))

# numero = 2
# while numero <= n:
#   es_primo = True  # Asumimos que el número es primo hasta que se demuestre lo contrario
#   divisor = 2
#   while divisor * divisor <= numero:  # Optimizamos: no es necesario probar divisores hasta numero
#     if numero % divisor == 0:
#       es_primo = False  # Si encontramos un divisor, no es primo
#       break  # Salimos del bucle interior
#     divisor += 1
#   if es_primo:
#     print(numero)

#   numero += 1