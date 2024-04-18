
import requests
import json

def get_first_activation(summit_code):
    url = f"https://api2.sota.org.uk/api/activations/first/{summit_code}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data:
            return {
                "ActivationDate": data.get("activationDate", "No date available"),
                "ActivationCall": data.get("ownCallsign", "No call sign")
            }
    return {"ActivationDate": "No date available", "ActivationCall": "No call sign"}

def process_summits(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        results = []
        for item in data:
            if item.get("ActivationCount") != "0":
                first_activation = get_first_activation(item["SummitCode"])
                results.append({
                    "SummitCode": item["SummitCode"],
                    "SummitName": item["SummitName"],
                    "ActivationDate": first_activation["ActivationDate"],
                    "ActivationCall": first_activation["ActivationCall"]
                })
        return results

# Assume 'tuscanysummit.json' contains the summit data including 'SummitCode' and 'ActivationCount'
activations = process_summits('tuscanysummit.json')
print(json.dumps(activations, indent=4))

# Save to file
with open('firstactivator-v2.json', 'w') as f:
    json.dump(activations, f, indent=4)


