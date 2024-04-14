import requests
import json

# Definindo a URL da API
url = "https://nominatim.openstreetmap.org/reverse"

# Definindo os parâmetros da requisição 
parameters = {
    "lat": "-19.92275",
    "lon": "-43.94517",
    "zoom": "18",
    "format": "jsonv2"
}

# Definindo o header da requisição
headers = {"User-Agent": "app"}

# Faz uma requisição GET para a URL especificada com os parametros e headers
response = requests.get(url=url, headers=headers, params=parameters)
response_json = response.json()

# # Imprime o conteúdo da resposta no formato JSON e com identação adequada
print(json.dumps(response_json, indent=2, ensure_ascii=False))