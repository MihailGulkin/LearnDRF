import requests

endpoint = "http://localhost:8000/api/products/"

get_response = requests.post(endpoint, json={'tiftle': 'Some'})
print(get_response.json())