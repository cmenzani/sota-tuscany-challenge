"""
.\venv\Scripts\activate
"""

import csv
import requests
import json

# URL del file CSV
url = "https://storage.sota.org.uk/summitslist.csv"

# URL dell'endpoint API per ottenere i dati degli attivatori
api_url = "https://api2.sota.org.uk/api/summits/{summitCode}"

# Dizionario per memorizzare i nominativi degli attivatori unici
unique_activators = {}

# Effettua la richiesta GET all'URL del file CSV
response = requests.get(url)

# Verifica che la richiesta sia andata a buon fine
if response.status_code == 200:
    # Leggi il contenuto del file CSV
    content = response.content.decode('utf-8').splitlines()

    # Crea un oggetto reader per il file CSV
    reader = csv.reader(content)

    # Salta la prima riga (intestazione)
    next(reader)

    # Itera sulle righe del file CSV
    for row in reader:
        # Verifica se la riga ha abbastanza elementi
        if len(row) >= 2:
            # Ottieni l'associazione e il codice del riferimento dalla riga
            assoc_code = row[1]
            summit_code = row[0]

            # Verifica se la referenza inizia con "I/TO-"
            if summit_code.startswith("I/TO-"):
                # Costruisci l'URL dell'endpoint API sostituendo i segnaposto con i valori corretti
            #    api_endpoint = api_url.replace("{assocCode}", assoc_code).replace("{summitCode}", summit_code)
                api_endpoint = api_url.replace("{summitCode}", summit_code)

                # Effettua la chiamata GET all'endpoint API
                api_response = requests.get(api_endpoint)

                # Verifica che la chiamata sia andata a buon fine
                if api_response.status_code == 200:
                    # Leggi i dati della risposta come JSON
                    activator_data = api_response.json()

                    # Estrai il nominativo dell'attivatore dalla risposta
                    activator_name = activator_data["name"]

                    # Aggiungi il nominativo dell'attivatore al dizionario dei nominativi unici
                    unique_activators[activator_name] = True

# Crea un elenco di nominativi unici degli attivatori
unique_activator_list = list(unique_activators.keys())

# Salva l'elenco di nominativi unici nel file "TuscanyUniqueActivatorAllTime.json"
with open("TuscanyUniqueActivatorAllTime.json", "w") as file:
    json.dump(unique_activator_list, file)

# Stampa il totale di elementi trovati
total_activators = len(unique_activator_list)
print("Totale elementi trovati:", total_activators)
