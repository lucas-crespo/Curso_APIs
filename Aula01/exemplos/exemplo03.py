import requests
import json

# Definindo a chave da API
api_key = "c41c34a57796d381eb775ca9088d9c070"

# Definindo a URL da API
url = "https://api.openweathermap.org/data/2.5/weather"

# Definindo os parâmetros da requisição 
parameters = {
    "q": "Suzano, São Paulo, Brasil",
    "appid": api_key,
}

# Definindo o header da requisição
headers = {"User-Agent": "app"}

# Faz uma requisição GET para a URL especificada com os parametros e headers
response = requests.get(url=url, headers=headers, params=parameters)

response_json = response.json()

# Imprime o conteúdo da resposta no formato JSON e com identação adequada
print(json.dumps(response_json, indent=2, ensure_ascii=False))