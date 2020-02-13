# get_data.py

import requests
import json
import statistics

print("REQUESTING SOME DATA FROM THE INTERNET...")

request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/gradebook.json"
print("URL:", request_url)

response = requests.get(request_url)
print(type(response))
#print(dir(response))
print(response.status_code)
#print(response.text)
print(type(response.text))

parsed_response = json.loads(response.text)
print(type(parsed_response)) #> dictionary



grades = [student["finalGrade"] for student in parsed_response["students"]]
print("GRADES", grades)

avg_grade = statistics.mean(grades)
print("AVG GRADE:", avg_grade)
