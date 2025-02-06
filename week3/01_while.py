from os import system
system("clear")

# Loops
print("While:")

# counter = 0
# while counter <= 5:
#     print("Counter: ", counter)
#     counter += 1
    
# counter = 0
# while True:
#     print("Hola")
#     counter += 1
#     if counter >= 5:
#         break


# counter = 0
# while counter <= 10:    
#     counter += 1
#     if counter % 2 == 0:
#         print(counter)

# #With continue
# counter = 0
# while counter <= 10:
#     counter += 1    
#     if counter % 2 != 0:
#         continue
#     print(counter)


# #Else
# counter = 0
# while counter < 5:
#     print(counter)
#     counter += 1
# else:
#     print("loop finished") #! at first false loop condition, execute the else

# #! the else never executes at break

# counter = 0
# while True:
#     print("Hola")
#     counter += 1
#     if counter >= 5:
#         break
# else:
#     print("the loop never execute") #! dead code

# #* this is usefull when I need to execute code when the all while is finished


# number = -1
# while number < 0:
#     number = int(input("type number positive \n"))
#     if number < 0:
#         print("the number is not positive")

# print(f"the number is {number}")


# try - except
number = -1
while number < 0:
    try:
        number = int(input("type number positive \n"))
        if number < 0:
            print("the number is not positive\n")
    except:
        print("please enter a number\n")
print(f"the number is {number}")