from dataclasses import dataclass
import requests

endpoint = "http://localhost:8000/api/products/"
data = {
    "title":"This field is Done",
    "price":33.99
}
get_response = requests.post(
    endpoint,
    json=data
    )

print(get_response.json())