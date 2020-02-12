# get_data.py

import requests
import json

print("REQUESTING SOME DATA FROM THE INTERNET...")

request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.json"
print("URL:", request_url)

response = requests.get(request_url)
print(type(response))
#print(dir(response))
print(response.status_code)
#print(response.text)
print(type(response.text))

parsed_response = json.loads(response.text)
print(type(parsed_response)) #> list

for any_prod in parsed_response:
    print(any_prod["id"], any_prod["name"])

first_prod = parsed_response[0]
print(first_prod["name"])
