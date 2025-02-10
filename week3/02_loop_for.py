from os import system
system('clear')
#Loop for


fruits = ['apple', 'banana', 'orange']

# for fruit in fruits:
#     print(fruit)


#iterate in iterable for example, strings

# name = "angelrodriguez"
# for c in name:
#     print(c)

# enumerate()
for index, fruit in enumerate(fruits):
    print(f" index: {index}, fruit:{fruit}")
 
# nested loops

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
for letter in letters:
    for number in numbers:
        print(f'{letter}{number}'.upper())


animals = ["dog", "cat", "mouse", "elefant", "butterfly", "fish"]
for idx, animal in enumerate(animals):
    if animal == "elefant":
        print(f'it in the index: {idx}')
        break;

for idx, animal in enumerate(animals):
    if animal == "elefant":        
        continue;
    print(animal)

# list comprehension
animals = ["dog", "cat", "mouse", "elefant", "butterfly", "fish"]
animals_upper = [animal.upper() for animal in animals]
print(animals_upper)


name = "angelrodriguez"
name_list = [c for c in name]
print(name_list)

pares = [ num for num in [1,2,3,4,5,6,7,8,9] if num % 2 == 0 ]
print(pares)