from os import system
system("clear")
# Range



nums = range(5) #! ITS NOT A LIST
print(type(nums)) #* range
print(type([1, 2, 3])) #* list

# sintax: range(number start = dafult 0, number end, step)

for num in range(0, 10):
    print(num)

for num in range(0, 10, 2):
    print(num)

for num in range(-5, 0):
    print(num)

for num in range(10, 0, -1):
    print(num)


nums = range(10)
list_of_numbs = list(nums)
print(list_of_numbs)

counter = 0
while counter < 5:
    print('hello')
    counter += 1


# this is better

for _ in range(5):
    print(" hello ")