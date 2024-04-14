import requests
import json

# Definindo a URL da API
url = "https://nominatim.openstreetmap.org/search"

# Definindo os parâmetros da requisição 
parameters = {
    "q": "Suzano Papel e Celulose",
    "limit": 1,
    "format": "jsonv2"
}

# Definindo o header da requisição
headers = {"User-Agent": "app"}

# Faz uma requisição GET para a URL especificada com os parametros e headers
response = requests.get(url=url, params=parameters)

response_json = response.json()

print(response.status_code)

# Imprime o conteúdo da resposta no formato JSON e com identação adequada
print(json.dumps(response_json, indent=2, ensure_ascii=False))