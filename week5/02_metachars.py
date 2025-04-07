import re


text = "Hola mundo, H0la de nuevo, H$la otra vez"
pattern = "H.la" # Hola, H0la, H$la

result = re.findall(pattern, text)

print(result if result else "not found")


text = "casa caasa cosa cisa cesa causa"
pattern = "c.sa"
matches = re.findall(pattern, text)
print(matches if matches else "not found")

#/---------------


text = "Hola mundo, H0la de nuevo H%la otra vez"
pattern = r"H.la"
result = re.findall(pattern, text)

print(result if result else "not found")


text = "Mi casa es blanca. Y el coche es negro."
pattern = r"\."
result = re.findall(pattern, text)

print(result if result else "not found")


#-----------------

#\d: coincide con cualquier digito 0-9

text = "El número de teléfono es 123456789"
found = re.findall(r'\d{9}', text)
print(found)

text = "El número de teléfono es 123456789"
found = re.findall(r'\d+', text)
print(found)


# detectar si hay un numero de Perú

text = "Mi numero es +51 999123890, anotalo va ?"
pattern = r"\+51 \d{9}"
found = re.search(pattern, text)
print(f"number: {found.group()}" if found else "not found")


#\w coincide con cualquier caracter alfanumerico (a-z, A-Z, 0-9, _)
text = "@@@@el_rubius_69)(&@)"
pattern = r"\w"
found = re.findall(pattern, text)
print(found)

# \s: coincide con cualuqier espacio en blanco

text = "Hola mundo \n como estas \t"
pattern = r"\s"
matches = re.findall(pattern, text)
print(matches)

# ^: coincide con el principio de una cadena

text = "%@123_name"
pattern = r"^\w" #validar nombre de usuario
valid = re.search(pattern, text)

if valid : print("userName valid")
else: print("userName invalid")


phone =  "+33 123456789"
pattern = r"^\+\d{2,3} "

valid  = re.search(pattern, phone)

if valid: print("valid")
else: print("invalid")

#$: coincide con el final de una cadena

text = "hola mundo."
pattern = r"mundo$"

valid  = re.search(pattern, text)

if valid: print("valid")
else: print("invalid")

# Valida que sea un correo de gmail

text = "arodriguezv22@gmail.com"
pattern = r"^\w+@gmail.com$"
valid  = re.search(pattern, text)

if valid: print("valid")
else: print("invalid")

# saber los nombres que tengan la extension .txt

files = "file1.txt file2.pdf midu-of.webp secret.txt"
#pattern = r"\w+\.txt"
pattern = r"\.txt$"
matches = re.findall(pattern, files)
print(matches)


# \b: coincide con el principio o final de una palabra

text = "casa coche perro acasa acasado casada"
pattern = r"\bcasa\b"
found = re.findall(pattern, text)
print(found)


# |: coincidir con una opcion u otra

fruits = "manzana platano, palta y pera, aguacate"
pattern = r"palta|aguacate"
found = re.findall(pattern, fruits)
print(found)