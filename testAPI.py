import requests
#response = requests.get('http://127.0.0.1:5000')
response = requests.get('localhost:5000')
tasks = response.json()
print(tasks)