import re

# *: puede aparecer 0 o mas veces

text = "aaaba"
pattern = r"a*"
matches = re.findall(pattern, text)
print(matches)


# cuantas palabras tienen de 0 a más "a" y despues una b?



#+: una o más veces
text = "ddddd aaa ccc bb"
pattern = r"a+"
matches = re.findall(pattern, text)
print(matches)


# ?: Cero o una vez

text = "aaabacbcanab"
pattern = r"a?b"
matches = re.findall(pattern, text)
print(matches)

# Haz opcional que aparezca un +34 en el siguiente texto

phone = "+34 123456789"
pattern = r"[\+34 ]?\d{9}"
valid = re.search(pattern, phone)

if valid: print("is valid")
else: print("is invalid")

# {n}: exactamente n veces

text = "aaaaaa      aa      aaaaa"
pattern = r"a{3}"
matches = re.findall(pattern, text)
print(matches)


#{n, m}: de n a m veces
text = "u uu uuu u"
pattern = r"u{2,3}"
matches = re.findall(pattern, text)
print(matches)


words = "ala casa arbol leon cinco murcielago"
pattern = r"\b\w{4,6}\b"
matches = re.findall(pattern, words)
print(matches)

#encuentra las palabras de mas de 6 letras

words = "ala fantastico casa arbol leon cinco murcielago"
pattern = r"\b\w{6,}\b"
matches = re.findall(pattern, words)
print(matches)
