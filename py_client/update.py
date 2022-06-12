import requests

endpoint = "http://localhost:8000/api/products/update/1/"


data = {
    'title':"New Hello World ",
    'price':12.00
}
get_response = requests.put(
    endpoint,
    json=data
    )

print(get_response.json())