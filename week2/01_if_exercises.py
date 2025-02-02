import os
os.system("clear")
###
# EJERCICOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

# number1 = int(input("Enter a number:"))
# number2 = int(input("Enter another number:"))
# if number1 > number2:
#     print(f"{number1} is greater than {number2}")
# elif number1 < number2:
#     print(f"{number2} is greater than {number1}")
# else:
#     print(f"{number1} and {number2} are equal")

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

# number1 = int(input("Enter a number:"))
# number2 = int(input("Enter another number:"))
# operator = input("Enter an operator (+, -, *, /):")

# if operator == "+":
#     print(f"{number1} + {number2} = {number1 + number2}")
# elif operator == "-":
#     print(f"{number1} - {number2} = {number1 - number2}")
# elif operator == "*":
#     print(f"{number1} * {number2} = {number1 * number2}")
# elif operator == "/":
#     if number2 == 0:
#         print("Division by zero is not allowed")
#     else:
#         print(f"{number1} / {number2} = {number1 / number2}")
# else:
#     print("Invalid operator")

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

# year = int(input("Enter a year:"))
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print("es biciesto")
# else:
#     print("no es biciesto")

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

age = int(input("Enter a age:\n"))

if age < 0:
    print("error")
elif age <= 2:
    print("its a baby")
elif age <= 12:
    print("its children")
elif age <= 17:
    print("its teenager")
elif age <= 64:
    print("its adult")
else:
    print("its old adult")