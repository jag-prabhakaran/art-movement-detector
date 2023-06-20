import requests

API_URL = "https://api-inference.huggingface.co/models/Jagannath/artDetection"
headers = {"Authorization": "Bearer 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"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

