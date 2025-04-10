import requests 

class Car:
    type = "cuatro ruedas"

    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def arrancar(self):
        print(f"El coche {self.marca} {self.modelo} arrancó!")


coche1 = Car("Toyota", "Corolla", "Rojo")
coche2 = Car("Ford", "Fiesta", "Azul")


coche1.arrancar()
coche2.arrancar()

class API:
    def __init__(self, api_key, url, model):
        self.api_key = api_key
        self.url = url
        self.model = model
    
    
    
    def __call__(self, prompt):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        data = {
            "model": self.model,
            "messages": [
                {
                    "role": "user", "content": prompt
                }
            ]
        }

        response = requests.post(self.url, headers=headers, json=data)
        return response.json()
    


OPEN_AI_URL = "https://api.openai.com/v1/chat/completions"
OPENAI_API_KEY =  "sk-XXXxXXxXXXxXX"
openai_api = API(OPENAI_API_KEY, OPEN_AI_URL, "gpt-4o-mini")

openai_api.call("Escribe un breve poema sobre la programacion")