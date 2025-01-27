## casting types

## transform a type to an other


# string to integer
print(type("100"))
print(type(int("100")))


#print("100" + 2) #! --> error
#print(2 + "100") #! --> error
print("100" + str(2)) 
print(2 + int("100")) 


print(type(float("100.5")))

#* this not round, only remove the decimal part
print(int(3.1416))

print(round(3.5)) #* 4 round to the nearest pairt  number
print(round(2.5)) #* 2 round to the nearest pair number

print(bool(3)) # True
#* the only number that is False is 0
print(bool(0)) # False
print(bool(-1)) # True

print(bool(" ")) # True
print(bool("")) # False
print(bool("False")) # True


#print(int("Hola mundo")) #! --> error