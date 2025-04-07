"""
    Why learn Regex

    - Advanced search
    - Data validation
    - Extract, replace and modify text
"""

#1. import regex module
import re

#2. create pattern
pattern = r"Hola"
#3. text
text = "Holamundo, Hola como estas"
#4. use re
result = re.search(pattern, text)

print("Pattern found" if result else "Pattern not found")


# .group() devuelve el string que coincide con el pattern
print(result.group())

# .start() devolver la posición inicial de la coincidencia
print(result.start())
# .end() devolver la posición final de la coincidencia
print(result.end())


#

text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver cómo la puede cagar con las regex para ir con cuidado"
pattern = r"IA"
result = re.search(pattern, text)
print(f"has IA start in {result.start()} and end in {result.end()}" if result else "Not found pattern")


#-----------
pattern = "python"
text = "me gusta python, python es lo maximo, aunque python no es tan dificil, ojo con python"
matches = re.findall(pattern, text)
print(matches)

#........ iter()

pattern = "python"
text = "me gusta python, python es lo maximo, aunque python no es tan dificil, ojo con python"
matches = re.finditer(pattern, text)

for match in matches:
    print(match.group(), match.start(), match.end())

pattern = "midu"
text = "Este curso de python de midudev. subscribete a midudev si te gustra este contenido, midu"
matches = re.finditer(pattern, text)

for match in matches:
    print(match.start(), match.end())


#-------------

text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver cómo la puede cagar con las iA regex para ir Ia con cuidado"
pattern = r"ia"
result = re.findall(pattern, text, re.IGNORECASE) # IGNORECASE is for ignore lower or upper case
if result:
    print(result)
# print(f"has IA start in {result.start()} and end in {result.end()}" if result else "Not found pattern")

## replace

text = "Hola, mundo! Hola de nuevo."
pattern = "Hola"
replacement = "Adiós"


new_text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
print(new_text)