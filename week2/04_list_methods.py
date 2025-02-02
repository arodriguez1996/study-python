import os
os.system("clear")


list1 = [1, 2, 3, 4]

# Add or inserts elements
list1.append(6)

print(list1)


list1.insert(1, 3)

print(list1)

list1.extend([7, 8, 9])

print(list1)


# delete elements

list1.remove(3) #delete the first coincidence

print(list1)

last = list1.pop() #remove the last element

print(list1)
print(last)

list1.pop(1) #delete the second element

print(list1)
#force deletion
del list1[-1]
print(list1)
# delete all elements
list1.clear()
print(list1)

# delete list by range

list1 = [1, 2, 3, 4, 5, 6]

del list1[2:]

print(list1)

#sort
print('Order lists modify the original')
numbers = [3, 31, 23, 99, 56]
numbers.sort() #this mutates the list
print(numbers)

print('Order lists modify the original')
numbers = [3, 31, 23, 99, 56]
sorted_numbers = sorted(numbers)
print(numbers)
print(sorted_numbers)

print('order strings with lower and uppers')
fruits = ['manzana', 'Pera', 'limon', 'Limon']
sorted_fruits = sorted(fruits)
print(sorted_fruits) #this sort the upper cases first

fruits = ['manzana', 'Pera', 'limon', 'Limon']
fruits.sort(key=str.lower)
print(fruits)

#more methods

letters = ['a', 'b', 'c']
print(len(letters)) # --> 3
print(letters.count('b')) # --> 1
print( 'b' in letters ) # -> True
print( 'z' in letters ) # -> False
