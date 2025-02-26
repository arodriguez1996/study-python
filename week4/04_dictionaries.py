from os import system
system('clear')
## Diccionarios

persona = {
    'nombre': 'angel',
    'edad': 25,
    'es_estudiante': True,
    'calificaciones': [1, 2, 3, 4, 5],
    'socials': {
        'twitter': 'a',
        'instagram': 'b',
        'facebook': 'c'
    }   
}


print(persona['nombre'])
print(persona['calificaciones'][2])
print(persona['socials']['twitter'])


persona['nombre'] = 'Victor Enrique'

print(persona)

del persona['edad']

print(persona)

es_estudiante = persona.pop('es_estudiante') #tambien lo elimina

print(es_estudiante)

#sobrescribir un diccionario con otro diccionario

a = { 'nombre': 'angel', 'edad': 25}
b = { 'nombre': 'victor', 'es_estudiante': True}

a.update(b)

print(a)

print('name' in persona) # False
print('nombre' in persona) # True

print(persona.keys())

print(persona.values())

print(persona.items())

for key, value in persona.items():
    print(key)
    print(value)
