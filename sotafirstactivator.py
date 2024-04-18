"""
.\venv\Scripts\activate
"""


"""

import requests
import json

# Disabilita i warning SSL, non raccomandato per la produzione
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

# Funzione per ottenere l'ID della cima
def get_summit_id(summit_code):
    url = f"https://api-db.sota.org.uk/admin/find_summit?search={summit_code}"
    response = requests.get(url, verify=False)  # SSL verify is set to False, use with caution
    data = response.json()
    return data[0]["SummitId"] if data else None

# Funzione per ottenere la storia delle attivazioni di una cima
def get_summit_activation_history(summit_id):
    url = f"https://api-db.sota.org.uk/admin/summit_history?summitID={summit_id}"
    response = requests.get(url, verify=False)  # SSL verify is set to False, use with caution
    data = response.json()
    return data

# Esempio di uso
summit_code = "ZL3/OT-371"  # Sostituire con il codice della cima desiderata
summit_id = get_summit_id(summit_code)

if summit_id:
    activation_history = get_summit_activation_history(summit_id)
    print(json.dumps(activation_history, indent=4))  # Stampa il risultato formattato
else:
    print("Summit ID not found.")
"""
import requests
import json
from datetime import datetime

# Disabilita i warning SSL, non raccomandato per la produzione
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

# Funzione per ottenere l'ID della cima
def get_summit_id(summit_code):
    url = f"https://api-db.sota.org.uk/admin/find_summit?search={summit_code}"
    response = requests.get(url, verify=False)
    data = response.json()
    return data[0]["SummitId"] if data else None

# Funzione per ottenere la storia delle attivazioni di una cima
def get_summit_activation_history(summit_id):
    url = f"https://api-db.sota.org.uk/admin/summit_history?summitID={summit_id}"
    response = requests.get(url, verify=False)
    data = response.json()
    return data

# Carica il file json dei summit e processa ciascun summit
def process_summits(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        activations = []

        for item in data:
            if item.get("ActivationCount") != "0":
                summit_id = get_summit_id(item["SummitCode"])
                if summit_id:
                    activation_history = get_summit_activation_history(summit_id)
                    if 'first' in activation_history and activation_history['first']:
                        first_activation = activation_history['first'][0]
                        # Converte la data di attivazione nel formato desiderato
                        activation_date = datetime.strptime(first_activation["ActivationDate"], "%d/%b/%Y").strftime("%d/%m/%Y")
                        activations.append({
                            "SummitCode": item["SummitCode"],
                            "SummitName": item["SummitName"],
                            "ActivationDate": activation_date,
                            "ActivationCall": first_activation["OwnCallsign"]
                        })
                    else:
                        print(f"No first activation details for {item['SummitCode']}.")

        return activations

# Funzione principale che esegue lo script
def main():
    file_path = 'tuscanysummit.json'  # Percorso del file json dei summit
    activations = process_summits(file_path)
    
    # Stampa i risultati o salvali in un file
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result_data = {
        "Timestamp": current_datetime,
        "Activations": activations
    }
    
    with open('firstactivations.json', 'w') as outfile:
        json.dump(result_data, outfile, indent=4)

    print(f"Data elaborazione: {current_datetime}")
    print(f"Totale attivazioni trovate: {len(activations)}")

if __name__ == "__main__":
    main()
