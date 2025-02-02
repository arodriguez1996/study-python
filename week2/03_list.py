import os
os.system("clear")
###
# Lists
# Secuencias mutables de elementos


print('\nCrear listas')

list2 = ["Manzanas", "Peras", "Platanos", "Melones"]
list3 = [1, "a", 3.14, True]

empty_list = []
list_list = [[1, 2], [3, 4]]
matrix= [[1, 2], [2, 3], [4, 5]]

print(list2)
print(list3)
print(empty_list)
print(list_list)
print(matrix)


# access elements by index

print(list2[0]) # "Manzanas"
print(list2[-1]) # "Melones"
print(list2[-2]) # "Platanos"

print(list_list[1][0])

# list slicing
list1 = [1, 2, 3, 4, 5]
print(list1[1:4]) # 2, 3, 4
print(list1[:3]) # 1, 2, 3
print(list1[2:]) # 3, 4, 5
print(list1[:]) # copy of list1 [1, 2, 3, 4, 5]


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list1[::2])# [1, 3, 5, 7, 9]
print(list1[::3])# [1, 4, 7]
print(list1[::-1]) #revert list

#Modify list

list1[0] = 20
print(list1)

#add more elements

#! less efective, create the new list in memory and concatenate with original list
list1 = list1 + [10, 11, 12]
print(list1)

#* more efective because it concatenate directly
list1 += [13, 14, 15]
print(list1)

#length
print("List length", len(list1)) # 15
