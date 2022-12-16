import requests

payload = {
    "sepal_length": 0.4,
    "sepal_width": 0.8,
    "petal_length": 0.2,
    "petal_width": 0.7
}

print(payload)

response = requests.post(url="http://127.0.0.1:8000/predict_flower", json=payload)

print(response.text)





