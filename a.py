import requests

def call_api():
    url = "https://api.example.com/data"
    headers = {"Authorization": "Bearer YOUR_API_KEY"}

    response = requests.get(url, headers=headers)
    data = response.json()

    return data

def process_data():
    data = call_api()

    processed_data = []
    for item in data:
        processed_item = {
            "id": item["id"],
            "name": item["name"],
            "description": item["description"],
            "date": item["date"],
            "value": item["value"]
        }
        processed_data.append(processed_item)

    return processed_data

def save_data():
    data = process_data()

    with open("data.json", "w") as file:
        json.dump(data, file)

save_data()
