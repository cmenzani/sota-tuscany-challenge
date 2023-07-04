import json

# Apri il file tuscanysummit.json in modalità lettura
with open('tuscanysummit.json', 'r') as file:
    # Carica il contenuto JSON dal file
    data = json.load(file)

    # Crea una lista per gli elementi JSON con "ActivationCount" uguale a "0"
    filtered_data = [item for item in data if item.get("ActivationCount") == "0"]

# Stampa gli elementi filtrati
for item in filtered_data:
    print(item)

# Stampa il totale di elementi trovati
total_elements = len(filtered_data)
print(f"Cime mai attivate: {total_elements}")
