import requests

endpoints = "http://httpbin.org/status/200/"
endpoints = "http://httpbin.org/anything"

get_request = requests.get(endpoints)
print(get_request.text)



