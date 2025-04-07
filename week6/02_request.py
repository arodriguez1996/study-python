# Como hacer peticiones a apis

import urllib.request
import json
import requests

api_post = "https://jsonplaceholder.typicode.com/todos/" 

# dificil y sin dependencias
try:
    response = urllib.request.urlopen(api_post)
    data = response.read()
    json_data = json.loads(data.decode('utf-8'))
    print(json_data)
    response.close()
except urllib.error.URLError as e:
    print(f"Error en la solicitud: {e}")

# con dependencia (requests)


response = requests.get(api_post)
print(response.json())


# un POST

# {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
input = {
    'userId': 1, 
    'id': 1, 
    'title': 'delectus aut autem', 
    'completed': False
}

response = requests.post(api_post, json=input)
print(f"Exitoso {response.status_code} : {response.json()}")


# un PUT

# {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
input = {
    'userId': 1, 
    'id': 1, 
    'title': 'delectus aut autem', 
    'completed': False
}

response = requests.put(f"{api_post}/1", json=input)
print(f"Exitoso {response.status_code} : {response.json()}")


OPENAI_API_KEY =  "sk-XXXxXXxXXXxXX"

def call_openai_gpt(api_key, prompt):
    OPEN_AI_URL = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "user", "content": prompt
            }
        ]
    }

    response = requests.post(OPEN_AI_URL, headers=headers, json=data)
    print(response.json())

api_response = call_openai_gpt(OPENAI_API_KEY, "escribe un poema sobre la programacion")

# print(json.dumps(api_response, indent=2))
print(api_response["choices"][0]["message"]["content"])