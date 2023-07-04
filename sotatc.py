import csv
import json
import requests

# URL del file CSV
url = "https://storage.sota.org.uk/summitslist.csv"

# Effettua la richiesta GET all'URL
response = requests.get(url)

# Verifica che la richiesta sia andata a buon fine
if response.status_code == 200:
    # Leggi il contenuto del file CSV
    content = response.content.decode('utf-8').splitlines()

    # Crea un oggetto reader per il file CSV
    reader = csv.reader(content)

    # Lista per salvare le righe nel range specificato
    rows_in_range = []

    # Itera sulle righe del file CSV
    for row in reader:
        summit_code = row[0]
        if summit_code.startswith("I/TO-"):
            summit_number = int(summit_code[6:])
            if 1 <= summit_number <= 999:
                # Aggiungi la riga alla lista
                rows_in_range.append(row)

    # Creazione della lista di dizionari con i dati delle righe nel range
    data_list = []
    for row in rows_in_range:
        data_dict = {
            "SummitCode": row[0],
            "AssociationName": row[1],
            "RegionName": row[2],
            "SummitName": row[3],
            "AltM": row[4],
            "AltFt": row[5],
            "GridRef1": row[6],
            "GridRef2": row[7],
            "Longitude": row[8],
            "Latitude": row[9],
            "Points": row[10],
            "BonusPoints": row[11],
            "ValidFrom": row[12],
            "ValidTo": row[13],
            "ActivationCount": row[14],
            "ActivationDate": row[15],
            "ActivationCall": row[16]
        }
        data_list.append(data_dict)

    # Salvataggio della lista di dizionari come file JSON
    with open("tuscanysummit.json", "w") as json_file:
        json.dump(data_list, json_file, indent=4)

else:
    print("Errore nella richiesta all'URL.")
