import re

# [:] coincide con cualquier caracter dentro de los corchetes

username = "rub.ius_69+$"
pattern = r"^[\w._%+-]+$"

match = re.search(pattern, username)
if match: print("valid", match.group())
else: print("not valid")


# buscar todas las vocales de una palabra


text = "hola mundo"
pattern = r"[aeiou]"
matches = re.findall(pattern, text)
print(matches if matches else "not found")

# [^]: coincide con cualquier caracter que no este dentro

text = "hola mundo"
pattern = r"[^aeiou]"
matches = re.findall(pattern, text)
print(matches if matches else "not found")


# un regex para encontrar las palabras man fan 
# y ban pero ignorar el resto

text = "man ran fan  gan ban"
pattern = r"[mfb]an"
matches = re.findall(pattern, text)
print(matches if matches else "not found")

# nos han complicado el asunto, porque ahora hay palabras 
# que encajan pero no empienzan por esas letras
# solo queremos las palabras man, fan y ban

text = "omniman fantastico man bandana"
pattern = r"\b[mfb]an\b"
matches = re.findall(pattern, text)
print(matches if matches else "not found")

# se pueden rangos!
text = "22"
pattern = r"[1-2]"
matches = re.findall(pattern, text)
print(matches if matches else "not found")

# rangos numericos [1-9]
# rangos alfanumericos [a-z]
# rangos alfanumericos con tilde [A-Za-z0-9áéíóúñ]

