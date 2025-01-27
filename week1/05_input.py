###
# 05 - Input (input()) function
# The input() function is used to get input from the user. 
# The input() function always returns a string.



name = input('What is your name?\n')
print(f'Hello {name}')

age = input('How old are you?\n')
#* always return a string
print(f'You are {age} years old, in 5 years you will be {int(age) + 5} years old')

#obtain multiple values

print("Obtain multiple values")
country, city = input("Enter your country and city: ").split()
print(f'You are from {city}, {country}')