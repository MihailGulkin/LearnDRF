import requests

endpoint = "http://localhost:8000/api/products/"

get_response = requests.post(endpoint, json={'title': 'Some'})
print(get_response.json())
