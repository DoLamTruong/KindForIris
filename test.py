# import requests

# body = {'petal_length': 0.75,
#         'petal_width': 0.5,
#         'sepal_length': 0.9,
#         'sepal_width': 0.1}

# url = "http://localhost:8001/predict"

# print(requests.post(url, data=body))
import requests

url = 'http://127.0.0.1:1080/predict'  # localhost and the defined port + endpoint
body = {
    "petal_length": 2,
    "sepal_length": 2,
    "petal_width": 0.5,
    "sepal_width": 3
}
response = requests.post(url, data=body)
print(response.json())
