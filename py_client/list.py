from dataclasses import dataclass
import requests

endpoint = "http://localhost:8000/api/products/"
data = {
    "title":"Second Title",
    "price":9.99
}
get_response = requests.get(
    endpoint
    )

print(get_response.json())