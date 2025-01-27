##
# 04 Variables
# this is for save data in memory

#* asigning a value to a variable

my_name = "Angel"
print(my_name)

age = 25
print(age)
age = 28
print(age)

#* dynamic typing: the type of the variable is determined by the value assigned to it
name = "Angel"
print(type(name))

name = 32
print(type(name))

#* strong typing: the type of the variable is enforced
# print("My name is " + 32) #! this line will throw an error

#* f-strings
# only available in python 3.6 and later
print(f"hola {my_name}, tengo {age + 5 - 5}")

#! not recomended
name, age, city = "Angel", 28, "Lima"
print(name, age, city)

# convention for variable names
#* snake_case

hello_world_variable = "Hello World"

#! no recomendable
HelloWorldVariable = "Hello World" # PascalCase
helloworldvariable = "Hello World" 

#* constants

# UPPER_CASE to constants, but python doesn't have constants

PI = 3.1416
GRAVITY = 9.8

#! error 12312312_variable = "ok" 
#! error my-variable = "ok" 
#! error my variable = "ok" 
#! error 12312312 = "ok"
#! error True = False 


#* types annotations, is only for documentation, in execution 
#* time python doesn't care about the type of the variable
is_user_logged_in: bool = True
print(is_user_logged_in)

#* activate typecheck in VScode
#! this mark error now 
# is_user_logged_in = "Hola"
print(is_user_logged_in)
