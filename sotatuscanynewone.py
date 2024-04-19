import json
from datetime import datetime
from collections import Counter
import re

def normalize_callsign(callsign):
    # Divide il callsign su "/"
    parts = callsign.split('/')
    # Seleziona la parte più lunga del callsign
    longest_part = max(parts, key=len)
    return longest_part

# Carica i dati JSON
file_path_json = 'firstactivator-v2.json'
with open(file_path_json, 'r') as file:
    data = json.load(file)

# Estrai e normalizza i callsign
activation_calls = [normalize_callsign(entry['ActivationCall']) for entry in data]
counts = Counter(activation_calls)

# Rimuove i callsign che non rispettano la lunghezza minima richiesta (almeno due caratteri)
filtered_counts = {call: count for call, count in counts.items() if len(call) > 1}

# Ordina i dati per TotNewOne in modo decrescente
sorted_counts = [{'ActivationCall': call, 'TotNewOne': str(count)} 
                 for call, count in sorted(filtered_counts.items(), key=lambda x: -x[1])]

# Formatta la data di elaborazione
processing_date = datetime.now().strftime("%d/%m/%Y")

# Percorso per il nuovo file JSON
output_file_path = 'sotatuscanynewone.json'

# Scrive i dati nel nuovo file JSON
with open(output_file_path, 'w') as output_file:
    json.dump(sorted_counts, output_file, indent=4)
